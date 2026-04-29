"""Tests for the WoW API surface in blizzardapi2.

Each test patches `requests.Session.get` (via the `mock_get` fixture) and
asserts the URL, query-param shape, and Authorization header that BaseApi
constructs. Live HTTP is never made.

The pattern under test is intentionally narrow: WoW exposes hundreds of
endpoints, but they all funnel through `BaseApi._make_request`. Picking
one representative of each *shape* (index, by-id, media, search, classic,
oauth-protected, CN region) is enough to guard against regressions in URL
routing, namespace construction, and token handling.
"""

from __future__ import annotations

import pytest

from blizzardapi2.wow.wow_api import WowApi
from blizzardapi2.wow.wow_game_data_api import WowGameDataApi
from blizzardapi2.wow.wow_profile_api import WowProfileApi
from tests.conftest import FAKE_TOKEN, prime_token

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture
def wow_api(fake_credentials: tuple[str, str]) -> WowApi:
    """A WowApi instance with both sub-clients pre-primed with a fake token.

    Priming on every nested client lets tests skip the OAuth POST round-trip
    and focus solely on the GET assertions.
    """
    client_id, client_secret = fake_credentials
    api = WowApi(client_id, client_secret)
    prime_token(api)
    prime_token(api.game_data)
    prime_token(api.profile)
    return api


# ---------------------------------------------------------------------------
# Facade
# ---------------------------------------------------------------------------


def test_wow_api_exposes_game_data_and_profile(
    fake_credentials: tuple[str, str],
) -> None:
    """The WowApi facade should hand out correctly-typed sub-clients."""
    client_id, client_secret = fake_credentials
    api = WowApi(client_id, client_secret)

    assert isinstance(api.game_data, WowGameDataApi)
    assert isinstance(api.profile, WowProfileApi)


# ---------------------------------------------------------------------------
# Game Data: index / by-id / media / search / classic / CN
# ---------------------------------------------------------------------------


def test_get_achievements_index_uses_static_namespace(
    wow_api: WowApi, mock_get
) -> None:
    """Index endpoints hit the index path with a static-{region} namespace."""
    result = wow_api.game_data.get_achievements_index(region="us", locale="en_US")

    mock_get.assert_called_once()
    args, kwargs = mock_get.call_args
    assert args[0] == "https://us.api.blizzard.com/data/wow/achievement/index"
    assert kwargs["params"] == {"namespace": "static-us", "locale": "en_US"}
    assert kwargs["headers"] == {"Authorization": f"Bearer {FAKE_TOKEN}"}
    assert result == {}


def test_get_achievement_by_id_embeds_id_in_path(wow_api: WowApi, mock_get) -> None:
    """By-id endpoints interpolate the id into the URL path, not the query."""
    wow_api.game_data.get_achievement(region="eu", locale="en_GB", achievement_id=12345)

    args, kwargs = mock_get.call_args
    assert args[0] == "https://eu.api.blizzard.com/data/wow/achievement/12345"
    # Id must NOT appear as a query parameter.
    assert "achievement_id" not in kwargs["params"]
    assert "id" not in kwargs["params"]
    assert kwargs["params"] == {"namespace": "static-eu", "locale": "en_GB"}


def test_get_achievement_media_hits_media_subpath(wow_api: WowApi, mock_get) -> None:
    """Media endpoints route under /data/wow/media/<resource>/<id>."""
    wow_api.game_data.get_achievement_media(
        region="us", locale="en_US", achievement_id=42
    )

    args, kwargs = mock_get.call_args
    assert args[0] == "https://us.api.blizzard.com/data/wow/media/achievement/42"
    assert kwargs["params"] == {"namespace": "static-us", "locale": "en_US"}


def test_search_endpoint_passes_through_kwargs(wow_api: WowApi, mock_get) -> None:
    """Search endpoints accept arbitrary kwargs alongside namespace+locale."""
    wow_api.game_data.search_decor(
        region="us",
        locale="en_US",
        **{"name.en_US": "lantern", "orderby": "id", "_page": 1},
    )

    args, kwargs = mock_get.call_args
    assert args[0] == "https://us.api.blizzard.com/data/wow/search/decor"
    assert kwargs["params"] == {
        "name.en_US": "lantern",
        "orderby": "id",
        "_page": 1,
        "namespace": "static-us",
        "locale": "en_US",
    }


def test_classic_variant_uses_classic_namespace(wow_api: WowApi, mock_get) -> None:
    """`is_classic=True` flips the namespace to static-classic-{region}."""
    wow_api.game_data.get_creature_families_index(
        region="us", locale="en_US", is_classic=True
    )

    args, kwargs = mock_get.call_args
    assert args[0] == "https://us.api.blizzard.com/data/wow/creature-family/index"
    assert kwargs["params"] == {
        "namespace": "static-classic-us",
        "locale": "en_US",
    }


def test_classic_false_uses_retail_namespace(wow_api: WowApi, mock_get) -> None:
    """The default branch of an is_classic-aware endpoint stays on retail."""
    wow_api.game_data.get_creature_family(
        region="eu", locale="en_GB", creature_family_id=7
    )

    args, kwargs = mock_get.call_args
    assert args[0] == "https://eu.api.blizzard.com/data/wow/creature-family/7"
    assert kwargs["params"] == {"namespace": "static-eu", "locale": "en_GB"}


def test_cn_region_uses_gateway_host(wow_api: WowApi, mock_get) -> None:
    """CN region must route through gateway.battlenet.com.cn (no subdomain)."""
    wow_api.game_data.get_achievements_index(region="cn", locale="zh_CN")

    args, kwargs = mock_get.call_args
    assert args[0] == "https://gateway.battlenet.com.cn/data/wow/achievement/index"
    # Must NOT have constructed the default {region}.api.blizzard.com host.
    assert "cn.api.blizzard.com" not in args[0]
    assert kwargs["params"] == {"namespace": "static-cn", "locale": "zh_CN"}


def test_dynamic_namespace_endpoint(wow_api: WowApi, mock_get) -> None:
    """Auction commodities use a dynamic-{region} namespace, not static."""
    wow_api.game_data.get_commodities(region="us", locale="en_US")

    args, kwargs = mock_get.call_args
    assert args[0] == "https://us.api.blizzard.com/data/wow/auctions/commodities"
    assert kwargs["params"] == {"namespace": "dynamic-us", "locale": "en_US"}


# ---------------------------------------------------------------------------
# Profile: OAuth-protected endpoints
# ---------------------------------------------------------------------------


def test_oauth_token_goes_to_header_not_query(wow_api: WowApi, mock_get) -> None:
    """SECURITY: a user access_token must end up in the Authorization header
    and never leak into the URL query string.

    BaseApi._make_request enforces this by popping `access_token` from
    `query_params` before calling Session.get. This is the test that would
    fail loudly if that pop is ever removed or refactored away.
    """
    user_token = "user_oauth_token_xyz"
    wow_api.profile.get_account_profile_summary(
        region="us", locale="en_US", access_token=user_token
    )

    args, kwargs = mock_get.call_args
    # /profile/user/wow lives on the regional API host, not oauth.battle.net
    # — the OAuth host only serves /oauth/* endpoints.
    assert args[0] == "https://us.api.blizzard.com/profile/user/wow"
    # Token in header, with Bearer prefix, using the *user* token (not the
    # primed client-credentials token).
    assert kwargs["headers"] == {"Authorization": f"Bearer {user_token}"}
    # And critically NOT in params.
    assert "access_token" not in kwargs["params"]
    assert kwargs["params"] == {"namespace": "profile-us", "locale": "en_US"}


def test_oauth_protected_character_uses_user_token(wow_api: WowApi, mock_get) -> None:
    """A second OAuth-protected endpoint to guard against per-method drift."""
    user_token = "another_user_token"
    wow_api.profile.get_protected_character_profile_summary(
        region="eu",
        locale="en_GB",
        access_token=user_token,
        realm_id=1234,
        character_id=5678,
    )

    args, kwargs = mock_get.call_args
    assert (
        args[0]
        == "https://eu.api.blizzard.com/profile/user/wow/protected-character/1234-5678"
    )
    assert kwargs["headers"] == {"Authorization": f"Bearer {user_token}"}
    assert "access_token" not in kwargs["params"]
    assert kwargs["params"] == {"namespace": "profile-eu", "locale": "en_GB"}


# ---------------------------------------------------------------------------
# Profile: client-credentials endpoints (no user token)
# ---------------------------------------------------------------------------


def test_character_profile_summary_uses_client_token(wow_api: WowApi, mock_get) -> None:
    """Profile endpoints without an access_token param fall back to the
    client-credentials token (primed on the fixture)."""
    wow_api.profile.get_character_profile_summary(
        region="us",
        locale="en_US",
        realm_slug="stormrage",
        character_name="dwarfprist",
    )

    args, kwargs = mock_get.call_args
    assert (
        args[0]
        == "https://us.api.blizzard.com/profile/wow/character/stormrage/dwarfprist"
    )
    assert kwargs["params"] == {"namespace": "profile-us", "locale": "en_US"}
    assert kwargs["headers"] == {"Authorization": f"Bearer {FAKE_TOKEN}"}


def test_guild_endpoint_uses_data_path_with_profile_namespace(
    wow_api: WowApi, mock_get
) -> None:
    """Guild endpoints sit under /data/wow/guild but use a profile-{region}
    namespace -- worth pinning since it's a routing oddity."""
    wow_api.profile.get_guild_roster(
        region="us",
        locale="en_US",
        realm_slug="stormrage",
        name_slug="example-guild",
    )

    args, kwargs = mock_get.call_args
    assert (
        args[0]
        == "https://us.api.blizzard.com/data/wow/guild/stormrage/example-guild/roster"
    )
    assert kwargs["params"] == {"namespace": "profile-us", "locale": "en_US"}


# ---------------------------------------------------------------------------
# Return-value pass-through
# ---------------------------------------------------------------------------


def test_method_returns_decoded_json_body(wow_api: WowApi, mock_get) -> None:
    """Every method should return whatever response.json() returned."""
    payload = {"id": 99, "name": "Test Achievement"}
    mock_get.return_value.json.return_value = payload

    result = wow_api.game_data.get_achievement(
        region="us", locale="en_US", achievement_id=99
    )

    assert result == payload
