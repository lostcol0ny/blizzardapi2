"""Tests for the Battle.net API surface — facade wiring + OAuth user-token flow.

The Battle.net package is the canonical example of the "user-supplied OAuth
token" pattern: `get_user_info` accepts an `access_token` from the caller
(obtained via authorization-code or implicit flow) and that token must travel
in the `Authorization: Bearer <token>` header — never in the URL query string,
where it would leak into server logs, proxies, and browser history.

These tests assert that security invariant directly against the patched
`requests.Session.get` call.
"""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest

from blizzardapi2.battlenet.battlenet_api import BattlenetApi
from blizzardapi2.battlenet.battlenet_oauth_api import BattlenetOAuthApi
from tests.conftest import FAKE_TOKEN

USER_TOKEN = "user_supplied_oauth_token"


# ---------------------------------------------------------------------------
# Facade
# ---------------------------------------------------------------------------


def test_battlenet_api_instantiates_and_exposes_oauth_client(
    fake_credentials,
) -> None:
    """`BattlenetApi` wires up an `oauth` attribute backed by `BattlenetOAuthApi`."""
    client_id, client_secret = fake_credentials
    api = BattlenetApi(client_id, client_secret)

    assert isinstance(api.oauth, BattlenetOAuthApi)
    # Credentials propagate to the underlying OAuth client.
    assert api.oauth._client_id == client_id
    assert api.oauth._client_secret == client_secret


# ---------------------------------------------------------------------------
# URL routing for get_user_info
# ---------------------------------------------------------------------------


@pytest.fixture
def oauth_api(fake_credentials) -> BattlenetOAuthApi:
    """Fresh `BattlenetOAuthApi` with no client-credentials token primed."""
    client_id, client_secret = fake_credentials
    return BattlenetOAuthApi(client_id, client_secret)


@pytest.mark.parametrize("region", ["us", "eu", "kr", "tw"])
def test_get_user_info_uses_global_oauth_host_for_non_cn_regions(
    oauth_api: BattlenetOAuthApi, mock_get: MagicMock, region: str
) -> None:
    """Non-CN regions hit `https://oauth.battle.net/oauth/userinfo`."""
    oauth_api.get_user_info(region, USER_TOKEN)

    called_url = mock_get.call_args.args[0]
    assert called_url == "https://oauth.battle.net/oauth/userinfo"


def test_get_user_info_uses_china_gateway_for_cn_region(
    oauth_api: BattlenetOAuthApi, mock_get: MagicMock
) -> None:
    """CN region hits the China-specific gateway host."""
    oauth_api.get_user_info("cn", USER_TOKEN)

    called_url = mock_get.call_args.args[0]
    assert called_url == "https://www.gateway.battlenet.com.cn/oauth/userinfo"


# ---------------------------------------------------------------------------
# Security: user-token-in-header invariant
# ---------------------------------------------------------------------------


def test_get_user_info_sends_access_token_in_authorization_header(
    oauth_api: BattlenetOAuthApi, mock_get: MagicMock
) -> None:
    """User-supplied access token MUST travel in the Authorization header.

    This is the canonical assertion for the OAuth user-token security model:
    the bearer token is sensitive and must be delivered via the header.
    """
    oauth_api.get_user_info("us", USER_TOKEN)

    headers = mock_get.call_args.kwargs["headers"]
    assert headers["Authorization"] == f"Bearer {USER_TOKEN}"


def test_get_user_info_does_not_leak_access_token_into_query_params(
    oauth_api: BattlenetOAuthApi, mock_get: MagicMock
) -> None:
    """The `access_token` key MUST NOT appear in the URL query string.

    `BaseApi._make_request` pops `access_token` out of the params dict before
    the request is dispatched. If this regresses, tokens would land in server
    logs, proxy logs, and `Referer` headers — a textbook OAuth leak.
    """
    oauth_api.get_user_info("us", USER_TOKEN)

    params = mock_get.call_args.kwargs["params"]
    assert "access_token" not in params
    # And the token's literal value should not appear among the param values.
    assert USER_TOKEN not in params.values()


# ---------------------------------------------------------------------------
# Token-flow correctness
# ---------------------------------------------------------------------------


def test_get_user_info_uses_user_token_verbatim_and_skips_client_credentials(
    oauth_api: BattlenetOAuthApi, mock_get: MagicMock, mock_post: MagicMock
) -> None:
    """A user-supplied token must NOT trigger the client-credentials POST.

    `_make_request` branches on the presence of `access_token` in params: if
    the caller supplied one, the client-credentials flow (POST /oauth/token)
    is skipped entirely. This protects against accidentally minting an
    application token when the user already provided their own.
    """
    oauth_api.get_user_info("us", USER_TOKEN)

    # No client-credentials POST should have happened.
    mock_post.assert_not_called()

    # The header carries the user's token verbatim — not a client token.
    headers = mock_get.call_args.kwargs["headers"]
    assert headers["Authorization"] == f"Bearer {USER_TOKEN}"
    assert FAKE_TOKEN not in headers["Authorization"]

    # The instance never cached a client token.
    assert oauth_api._access_token is None
    assert oauth_api._token_expires_at is None


def test_get_user_info_returns_session_get_json_payload(
    oauth_api: BattlenetOAuthApi, mock_get: MagicMock
) -> None:
    """Return value is whatever `Session.get(...).json()` produced."""
    expected = {"id": 12345, "battletag": "Test#1234", "sub": "12345"}
    mock_get.return_value.json.return_value = expected

    result = oauth_api.get_user_info("us", USER_TOKEN)

    assert result == expected
