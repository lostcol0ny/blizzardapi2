"""Tests for BaseApi — auth, URL construction, and token lifecycle.

BaseApi is the security-critical seam: every request flows through its
URL builders and `_make_request`. These tests verify that user-supplied
OAuth tokens are never leaked into URL query strings, that client
credentials are sent via HTTP Basic auth, and that the 401-retry path
only fires for the client-credentials flow (never for user tokens).
"""

from __future__ import annotations

from datetime import UTC, datetime, timedelta

import pytest

from blizzardapi2.api import BaseApi, LocaleApi
from blizzardapi2.types import Locale, Region
from tests.conftest import CLIENT_ID, CLIENT_SECRET, FAKE_TOKEN, prime_token


@pytest.fixture
def api(fake_credentials) -> BaseApi:
    """A fresh BaseApi instance with no token primed."""
    client_id, client_secret = fake_credentials
    return BaseApi(client_id, client_secret)


# ---------------------------------------------------------------------------
# URL construction
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("region", ["us", "eu", "kr", "tw"])
def test_build_api_url_non_cn_regions(api: BaseApi, region: str) -> None:
    """Non-CN regions resolve to `{region}.api.blizzard.com`."""
    url = api._build_api_url("/data/wow/realm/index", region)
    assert url == f"https://{region}.api.blizzard.com/data/wow/realm/index"


def test_build_api_url_cn_uses_gateway(api: BaseApi) -> None:
    """CN region uses the special gateway host with no region subdomain."""
    url = api._build_api_url("/data/wow/realm/index", "cn")
    assert url == "https://gateway.battlenet.com.cn/data/wow/realm/index"


@pytest.mark.parametrize("region", ["us", "eu", "kr", "tw"])
def test_build_oauth_url_non_cn_regions(api: BaseApi, region: str) -> None:
    """Non-CN OAuth always points to the global oauth.battle.net host."""
    url = api._build_oauth_url("/oauth/token", region)
    assert url == "https://oauth.battle.net/oauth/token"


def test_build_oauth_url_cn_uses_china_gateway(api: BaseApi) -> None:
    """CN OAuth uses the China-specific gateway host."""
    url = api._build_oauth_url("/oauth/token", "cn")
    assert url == "https://www.gateway.battlenet.com.cn/oauth/token"


# ---------------------------------------------------------------------------
# Token expiry checks
# ---------------------------------------------------------------------------


def test_is_token_expired_true_when_no_token(api: BaseApi) -> None:
    """A never-fetched token is treated as expired."""
    assert api._token_expires_at is None
    assert api._is_token_expired() is True


def test_is_token_expired_false_when_fresh(api: BaseApi) -> None:
    """A token comfortably outside the refresh buffer is not expired."""
    prime_token(api, expires_in=86400)
    assert api._is_token_expired() is False


def test_is_token_expired_true_within_refresh_buffer(api: BaseApi) -> None:
    """A token expiring within TOKEN_REFRESH_BUFFER is treated as expired."""
    api._access_token = FAKE_TOKEN
    # Expires in 4 minutes — inside the 5-minute refresh window.
    api._token_expires_at = datetime.now(UTC) + timedelta(minutes=4)
    assert api._is_token_expired() is True


# ---------------------------------------------------------------------------
# _ensure_valid_token
# ---------------------------------------------------------------------------


def test_ensure_valid_token_fetches_when_missing(api: BaseApi, mock_post) -> None:
    """First call lazily POSTs to /oauth/token."""
    api._ensure_valid_token("us")
    assert mock_post.call_count == 1
    assert api._access_token == FAKE_TOKEN
    assert api._token_expires_at is not None


def test_ensure_valid_token_noop_when_fresh(api: BaseApi, mock_post) -> None:
    """A fresh cached token must not trigger another POST."""
    prime_token(api)
    api._ensure_valid_token("us")
    assert mock_post.call_count == 0


# ---------------------------------------------------------------------------
# _get_client_token
# ---------------------------------------------------------------------------


def test_get_client_token_uses_basic_auth_and_grant_type(
    api: BaseApi, mock_post
) -> None:
    """POST must use HTTP Basic with credentials and client_credentials grant."""
    api._get_client_token("us")

    mock_post.assert_called_once()
    call = mock_post.call_args
    # URL is positional arg 0
    assert call.args[0] == "https://oauth.battle.net/oauth/token"
    assert call.kwargs["params"] == {"grant_type": "client_credentials"}
    assert call.kwargs["auth"] == (CLIENT_ID, CLIENT_SECRET)


def test_get_client_token_stores_token_and_expiry(api: BaseApi, mock_post) -> None:
    """Response is parsed into _access_token and _token_expires_at."""
    before = datetime.now(UTC)
    api._get_client_token("us")
    after = datetime.now(UTC)

    assert api._access_token == FAKE_TOKEN
    assert api._token_expires_at is not None
    # expires_in is 86400 in the fixture; expiry should sit roughly there.
    expected_min = before + timedelta(seconds=86400)
    expected_max = after + timedelta(seconds=86400)
    assert expected_min <= api._token_expires_at <= expected_max


def test_get_client_token_uses_cn_oauth_url(api: BaseApi, mock_post) -> None:
    """CN region routes through the China gateway host for token POST."""
    api._get_client_token("cn")
    assert (
        mock_post.call_args.args[0]
        == "https://www.gateway.battlenet.com.cn/oauth/token"
    )


# ---------------------------------------------------------------------------
# _make_request — happy path
# ---------------------------------------------------------------------------


def test_make_request_uses_cached_token_in_bearer_header(
    api: BaseApi, mock_get
) -> None:
    """Cached client-credentials token is sent as `Authorization: Bearer ...`."""
    prime_token(api)
    mock_get.return_value.json.return_value = {"ok": True}

    result = api._make_request("https://us.api.blizzard.com/data/wow/realm/index", "us")

    assert result == {"ok": True}
    mock_get.assert_called_once()
    headers = mock_get.call_args.kwargs["headers"]
    assert headers["Authorization"] == f"Bearer {FAKE_TOKEN}"


def test_make_request_passes_query_params_through(api: BaseApi, mock_get) -> None:
    """Non-token query params are forwarded to Session.get untouched."""
    prime_token(api)
    api._make_request(
        "https://us.api.blizzard.com/data/wow/realm/index",
        "us",
        query_params={"locale": "en_US", "namespace": "dynamic-us"},
    )
    assert mock_get.call_args.kwargs["params"] == {
        "locale": "en_US",
        "namespace": "dynamic-us",
    }


# ---------------------------------------------------------------------------
# _make_request — user OAuth token must NEVER hit the URL
# ---------------------------------------------------------------------------


def test_make_request_user_access_token_moves_to_header(
    api: BaseApi, mock_get, mock_post
) -> None:
    """A user-supplied access_token is moved to the Authorization header.

    Critical: it must NOT appear in the URL params, or it would be logged
    by upstream proxies / web server access logs.
    """
    user_token = "user_oauth_token_secret"
    api._make_request(
        "https://us.api.blizzard.com/profile/user/wow",
        "us",
        query_params={"access_token": user_token, "locale": "en_US"},
    )

    call = mock_get.call_args
    # Token went to the header...
    assert call.kwargs["headers"]["Authorization"] == f"Bearer {user_token}"
    # ...and is NOT in the URL params.
    assert "access_token" not in call.kwargs["params"]
    assert call.kwargs["params"] == {"locale": "en_US"}
    # And we did NOT trigger a client-credentials POST for a user-token call.
    assert mock_post.call_count == 0


def test_make_request_user_token_does_not_mutate_caller_dict(
    api: BaseApi, mock_get
) -> None:
    """The popped access_token must not vanish from the caller's dict."""
    caller_params = {"access_token": "user_token", "locale": "en_US"}
    api._make_request(
        "https://us.api.blizzard.com/profile/user/wow", "us", caller_params
    )
    # Caller's dict is preserved (copy() in _make_request).
    assert caller_params == {"access_token": "user_token", "locale": "en_US"}


# ---------------------------------------------------------------------------
# _make_request — 401 retry semantics
# ---------------------------------------------------------------------------


def test_make_request_401_refreshes_and_retries_for_client_credentials(
    api: BaseApi, mock_get, mock_post
) -> None:
    """A 401 on a client-credentials call triggers one refresh + retry."""
    prime_token(api, token="stale_token")

    stale_response = mock_get.return_value
    stale_response.status_code = 401

    fresh_response = type(stale_response)()
    fresh_response.status_code = 200
    fresh_response.json = lambda: {"ok": True}

    mock_get.side_effect = [stale_response, fresh_response]

    # Have the refresh POST return a NEW token so we can assert the retry
    # used it.
    mock_post.return_value.json.return_value = {
        "access_token": "fresh_token",
        "token_type": "bearer",
        "expires_in": 86400,
    }

    result = api._make_request("https://us.api.blizzard.com/data/wow/realm/index", "us")

    assert result == {"ok": True}
    assert mock_get.call_count == 2
    assert mock_post.call_count == 1
    # Retry must use the freshly-fetched token.
    retry_headers = mock_get.call_args_list[1].kwargs["headers"]
    assert retry_headers["Authorization"] == "Bearer fresh_token"


def test_make_request_401_does_not_retry_for_user_token(
    api: BaseApi, mock_get, mock_post
) -> None:
    """User-supplied tokens must NOT trigger an auto-refresh on 401."""
    mock_get.return_value.status_code = 401

    with pytest.raises(Exception):  # raise_for_status -> HTTPError
        # raise_for_status is a MagicMock — make it raise like requests does.
        mock_get.return_value.raise_for_status.side_effect = __import__(
            "requests"
        ).exceptions.HTTPError("401")
        api._make_request(
            "https://us.api.blizzard.com/profile/user/wow",
            "us",
            query_params={"access_token": "expired_user_token"},
        )

    # Exactly one GET, no token refresh POST.
    assert mock_get.call_count == 1
    assert mock_post.call_count == 0


# ---------------------------------------------------------------------------
# get_resource / get_oauth_resource integration
# ---------------------------------------------------------------------------


def test_get_resource_end_to_end(api: BaseApi, mock_get, mock_post) -> None:
    """get_resource builds API URL, fetches token, and issues GET."""
    mock_get.return_value.json.return_value = {"realms": []}

    result = api.get_resource(
        "/data/wow/realm/index",
        Region.EU,
        query_params={"locale": "en_GB"},
    )

    assert result == {"realms": []}
    # Token POST happened once (lazy fetch).
    assert mock_post.call_count == 1
    # GET hit the EU API host.
    assert (
        mock_get.call_args.args[0] == "https://eu.api.blizzard.com/data/wow/realm/index"
    )
    assert mock_get.call_args.kwargs["params"] == {"locale": "en_GB"}
    assert (
        mock_get.call_args.kwargs["headers"]["Authorization"] == f"Bearer {FAKE_TOKEN}"
    )


def test_get_oauth_resource_end_to_end(api: BaseApi, mock_get, mock_post) -> None:
    """get_oauth_resource builds OAuth URL and forwards user token to header."""
    mock_get.return_value.json.return_value = {"id": 42, "battletag": "x#1"}

    result = api.get_oauth_resource(
        "/oauth/userinfo",
        Region.US,
        query_params={"access_token": "user_token"},
    )

    assert result == {"id": 42, "battletag": "x#1"}
    # No client-credentials POST when a user token is supplied.
    assert mock_post.call_count == 0
    # URL is the OAuth host, not the API host.
    assert mock_get.call_args.args[0] == "https://oauth.battle.net/oauth/userinfo"
    # Token in header, NOT in params.
    assert "access_token" not in mock_get.call_args.kwargs["params"]
    assert mock_get.call_args.kwargs["headers"]["Authorization"] == "Bearer user_token"


# ---------------------------------------------------------------------------
# HTTP timeout (issue #39)
# ---------------------------------------------------------------------------


def test_make_request_passes_get_timeout(api: BaseApi, mock_get) -> None:
    """Every API GET must include `timeout=` to prevent indefinite hangs."""
    prime_token(api)
    api._make_request("https://us.api.blizzard.com/data/wow/realm/index", "us")
    assert mock_get.call_args.kwargs.get("timeout") == BaseApi.DEFAULT_GET_TIMEOUT


def test_get_client_token_passes_post_timeout(api: BaseApi, mock_post) -> None:
    """Token POST must include `timeout=`."""
    api._get_client_token("us")
    assert mock_post.call_args.kwargs.get("timeout") == BaseApi.DEFAULT_POST_TIMEOUT


def test_401_retry_get_also_passes_timeout(api: BaseApi, mock_get, mock_post) -> None:
    """The retry GET in the 401-refresh path must also carry a timeout."""
    prime_token(api, token="stale")

    stale = mock_get.return_value
    stale.status_code = 401

    fresh = type(stale)()
    fresh.status_code = 200
    fresh.json = lambda: {"ok": True}

    mock_get.side_effect = [stale, fresh]
    mock_post.return_value.json.return_value = {
        "access_token": "fresh",
        "expires_in": 86400,
    }

    api._make_request("https://us.api.blizzard.com/x", "us")

    assert mock_get.call_count == 2
    assert (
        mock_get.call_args_list[0].kwargs.get("timeout") == BaseApi.DEFAULT_GET_TIMEOUT
    )
    assert (
        mock_get.call_args_list[1].kwargs.get("timeout") == BaseApi.DEFAULT_GET_TIMEOUT
    )


def test_subclass_can_override_default_timeout(mock_get, fake_credentials) -> None:
    """Subclasses override DEFAULT_*_TIMEOUT to customize per-instance."""

    class FastApi(BaseApi):
        DEFAULT_GET_TIMEOUT = 5.0

    client_id, client_secret = fake_credentials
    api = FastApi(client_id, client_secret)
    prime_token(api)
    api._make_request("https://us.api.blizzard.com/x", "us")
    assert mock_get.call_args.kwargs["timeout"] == 5.0


# ---------------------------------------------------------------------------
# Default values execution in get_resource / get_oauth_resource
# ---------------------------------------------------------------------------


@pytest.fixture
def with_defaults_api(fake_credentials) -> LocaleApi:
    """A fresh LocaleApi instance with no token primed."""
    client_id, client_secret = fake_credentials
    return LocaleApi(client_id, client_secret, region=Region.KR, locale=Locale.ES_MX)


def test_get_resource_with_defaults(
    with_defaults_api: LocaleApi, mock_get, mock_post
) -> None:
    """get_resource builds API URL, fetches token, and issues GET using default values."""
    mock_get.return_value.json.return_value = {"realms": []}

    result = with_defaults_api.get_resource("/data/wow/realm/index")

    assert result == {"realms": []}
    # Token POST happened once (lazy fetch).
    assert mock_post.call_count == 1
    # GET hit the KR API host.
    assert (
        mock_get.call_args.args[0] == "https://kr.api.blizzard.com/data/wow/realm/index"
    )
    assert mock_get.call_args.kwargs["params"] == {"locale": "es_MX"}
    assert (
        mock_get.call_args.kwargs["headers"]["Authorization"] == f"Bearer {FAKE_TOKEN}"
    )


def test_get_resource_with_overridden_defaults(
    with_defaults_api: LocaleApi, mock_get, mock_post
) -> None:
    """get_resource builds API URL, fetches token, and issues GET using explicitly provided values."""
    mock_get.return_value.json.return_value = {"realms": []}

    result = with_defaults_api.get_resource(
        "/data/wow/realm/index", region=Region.EU, locale=Locale.EN_GB
    )

    assert result == {"realms": []}
    # Token POST happened once (lazy fetch).
    assert mock_post.call_count == 1
    # GET hit the KR API host.
    assert (
        mock_get.call_args.args[0] == "https://eu.api.blizzard.com/data/wow/realm/index"
    )
    assert mock_get.call_args.kwargs["params"] == {"locale": "en_GB"}
    assert (
        mock_get.call_args.kwargs["headers"]["Authorization"] == f"Bearer {FAKE_TOKEN}"
    )


def test_get_oauth_resource_with_defaults(
    with_defaults_api: LocaleApi, mock_get, mock_post
) -> None:
    """get_oauth_resource builds OAuth URL and forwards user token to header."""
    mock_get.return_value.json.return_value = {"id": 42, "battletag": "x#1"}

    result = with_defaults_api.get_oauth_resource(
        "/oauth/userinfo",
        query_params={"access_token": "user_token"},
    )

    assert result == {"id": 42, "battletag": "x#1"}
    # No client-credentials POST when a user token is supplied.
    assert mock_post.call_count == 0
    # URL is the OAuth host, not the API host.
    assert mock_get.call_args.args[0] == "https://oauth.battle.net/oauth/userinfo"
    # Token in header, NOT in params.
    assert "access_token" not in mock_get.call_args.kwargs["params"]
    assert mock_get.call_args.kwargs["headers"]["Authorization"] == "Bearer user_token"


def test_get_oauth_resource_with_overridden_defaults(
    with_defaults_api: LocaleApi, mock_get, mock_post
) -> None:
    """get_oauth_resource builds OAuth URL and forwards user token to header."""
    mock_get.return_value.json.return_value = {"id": 42, "battletag": "x#1"}

    result = with_defaults_api.get_oauth_resource(
        "/oauth/userinfo",
        Region.CN,
        query_params={"access_token": "user_token"},
    )

    assert result == {"id": 42, "battletag": "x#1"}
    # No client-credentials POST when a user token is supplied.
    assert mock_post.call_count == 0
    # URL is the OAuth host, not the API host.
    assert (
        mock_get.call_args.args[0]
        == "https://www.gateway.battlenet.com.cn/oauth/userinfo"
    )
    # Token in header, NOT in params.
    assert "access_token" not in mock_get.call_args.kwargs["params"]
    assert mock_get.call_args.kwargs["headers"]["Authorization"] == "Bearer user_token"


@pytest.fixture
def without_defaults_api(fake_credentials) -> LocaleApi:
    """A fresh LocaleApi instance with no token primed."""
    client_id, client_secret = fake_credentials
    return LocaleApi(client_id, client_secret)


def test_get_resource_failure_without_default_region(
    without_defaults_api: LocaleApi, mock_get, mock_post
) -> None:
    """get_resource builds API URL, fetches token, and issues GET."""
    with pytest.raises(ValueError, match="Region"):
        without_defaults_api.get_resource("/data/wow/realm/index", locale=Locale.EN_GB)


def test_get_resource_failure_with_invalid_region(
    without_defaults_api: LocaleApi, mock_get, mock_post
) -> None:
    """get_resource builds API URL, fetches token, and issues GET."""
    with pytest.raises(ValueError, match="Region"):
        without_defaults_api.get_resource(
            "/data/wow/realm/index", region="invalid", locale=Locale.EN_GB  # type: ignore
        )


def test_get_resource_failure_without_default_locale(
    without_defaults_api: LocaleApi, mock_get, mock_post
) -> None:
    """get_resource builds API URL, fetches token, and issues GET."""
    with pytest.raises(ValueError, match="Locale"):
        without_defaults_api.get_resource("/data/wow/realm/index", region=Region.CN)


def test_get_resource_failure_with_invalid_locale(
    without_defaults_api: LocaleApi, mock_get, mock_post
) -> None:
    """get_resource builds API URL, fetches token, and issues GET."""
    with pytest.raises(ValueError, match="Locale"):
        without_defaults_api.get_resource(
            "/data/wow/realm/index", region=Region.CN, locale="invalid"  # type: ignore
        )


def test_get_resource_with_locale_in_query_params(
    without_defaults_api: LocaleApi, mock_get, mock_post
) -> None:
    """get_resource builds API URL, fetches token, and issues GET using explicitly provided values."""
    mock_get.return_value.json.return_value = {"realms": []}

    result = without_defaults_api.get_resource(
        "/data/wow/realm/index", region=Region.EU, query_params={"locale": "my_stuff"}
    )

    assert (
        mock_get.call_args.args[0] == "https://eu.api.blizzard.com/data/wow/realm/index"
    )
    assert mock_get.call_args.kwargs["params"] == {"locale": "my_stuff"}
