"""Tests for the Diablo III API wrapper.

These tests verify URL routing, query-parameter shape, return-value
pass-through, and the BaseApi security invariant that any caller-supplied
``access_token`` is stripped from query params and forwarded as a Bearer
header. No live HTTP is performed — `requests.Session.get` is patched via
the shared ``mock_get`` fixture in ``tests/conftest.py``.
"""

from __future__ import annotations

from blizzardapi2.diablo3.diablo3_api import Diablo3Api
from blizzardapi2.diablo3.diablo3_community_api import Diablo3CommunityApi
from blizzardapi2.diablo3.diablo3_game_data_api import Diablo3GameDataApi

from tests.conftest import FAKE_TOKEN, prime_token

# ---------------------------------------------------------------------------
# Facade wiring
# ---------------------------------------------------------------------------


def test_facade_exposes_community_and_game_data(fake_credentials):
    """Diablo3Api should compose the two sub-clients with the right types."""
    client_id, client_secret = fake_credentials
    api = Diablo3Api(client_id, client_secret)

    assert isinstance(api.community, Diablo3CommunityApi)
    assert isinstance(api.game_data, Diablo3GameDataApi)


# ---------------------------------------------------------------------------
# Community API
# ---------------------------------------------------------------------------


def test_community_get_act_index_us(fake_credentials, mock_get):
    """get_act_index hits /d3/data/act on the US regional host."""
    client_id, client_secret = fake_credentials
    api = Diablo3CommunityApi(client_id, client_secret)
    prime_token(api)

    payload = {"acts": [{"slug": "act-i"}]}
    mock_get.return_value.json.return_value = payload

    result = api.get_act_index(region="us", locale="en_US")

    assert result == payload
    mock_get.assert_called_once()
    args, kwargs = mock_get.call_args
    assert args[0] == "https://us.api.blizzard.com/d3/data/act"
    assert kwargs["params"] == {"locale": "en_US"}
    assert kwargs["headers"] == {"Authorization": f"Bearer {FAKE_TOKEN}"}
    assert "access_token" not in kwargs["params"]


def test_community_get_act_builds_path_with_id(fake_credentials, mock_get):
    """get_act interpolates the act_id into the resource path."""
    client_id, client_secret = fake_credentials
    api = Diablo3CommunityApi(client_id, client_secret)
    prime_token(api)

    api.get_act(region="eu", locale="en_GB", act_id=2)

    args, kwargs = mock_get.call_args
    assert args[0] == "https://eu.api.blizzard.com/d3/data/act/2"
    assert kwargs["params"] == {"locale": "en_GB"}


def test_community_get_recipe_nested_path(fake_credentials, mock_get):
    """get_recipe builds a nested artisan/recipe path correctly."""
    client_id, client_secret = fake_credentials
    api = Diablo3CommunityApi(client_id, client_secret)
    prime_token(api)

    api.get_recipe(
        region="us",
        locale="en_US",
        artisan_slug="blacksmith",
        recipe_slug="apprentice-flamberge",
    )

    args, kwargs = mock_get.call_args
    assert args[0] == (
        "https://us.api.blizzard.com"
        "/d3/data/artisan/blacksmith/recipe/apprentice-flamberge"
    )
    assert kwargs["params"] == {"locale": "en_US"}


def test_community_profile_endpoint_strips_user_access_token(
    fake_credentials, mock_get
):
    """A caller-supplied access_token must never reach query params.

    The Diablo 3 profile endpoints take an account ID. None of the D3
    methods accept an `access_token` kwarg directly, but BaseApi will
    still pop one out of any query_params dict it receives — verify the
    invariant holds end-to-end by exercising get_resource directly with
    an access_token in the params.
    """
    client_id, client_secret = fake_credentials
    api = Diablo3CommunityApi(client_id, client_secret)
    prime_token(api)

    api.get_resource(
        "/d3/profile/Player-1234/",
        region="us",
        query_params={"locale": "en_US", "access_token": "user-supplied-token"},
    )

    args, kwargs = mock_get.call_args
    assert args[0] == "https://us.api.blizzard.com/d3/profile/Player-1234/"
    assert "access_token" not in kwargs["params"]
    assert kwargs["params"] == {"locale": "en_US"}
    assert kwargs["headers"] == {"Authorization": "Bearer user-supplied-token"}


# ---------------------------------------------------------------------------
# Game Data API
# ---------------------------------------------------------------------------


def test_game_data_get_season_index_no_query_params(fake_credentials, mock_get):
    """get_season_index sends no query params (no locale, no namespace)."""
    client_id, client_secret = fake_credentials
    api = Diablo3GameDataApi(client_id, client_secret)
    prime_token(api)

    payload = {"seasons": [1, 2, 3]}
    mock_get.return_value.json.return_value = payload

    result = api.get_season_index(region="us")

    assert result == payload
    args, kwargs = mock_get.call_args
    assert args[0] == "https://us.api.blizzard.com/data/d3/season/"
    assert kwargs["params"] == {}
    assert "access_token" not in kwargs["params"]


def test_game_data_get_era_leaderboard_path(fake_credentials, mock_get):
    """get_era_leaderboard composes era_id and leaderboard_id into the path."""
    client_id, client_secret = fake_credentials
    api = Diablo3GameDataApi(client_id, client_secret)
    prime_token(api)

    api.get_era_leaderboard(region="eu", era_id=10, leaderboard_id=42)

    args, kwargs = mock_get.call_args
    assert args[0] == ("https://eu.api.blizzard.com/data/d3/era/10/leaderboard/42")
    assert kwargs["params"] == {}


# ---------------------------------------------------------------------------
# Region routing
# ---------------------------------------------------------------------------


def test_cn_region_uses_gateway_host(fake_credentials, mock_get):
    """CN region must route to gateway.battlenet.com.cn, not {region}.api.*."""
    client_id, client_secret = fake_credentials
    api = Diablo3GameDataApi(client_id, client_secret)
    prime_token(api)

    api.get_season(region="cn", season_id=27)

    args, kwargs = mock_get.call_args
    assert args[0] == "https://gateway.battlenet.com.cn/data/d3/season/27"
    assert kwargs["headers"] == {"Authorization": f"Bearer {FAKE_TOKEN}"}


def test_cn_community_endpoint_uses_gateway_host(fake_credentials, mock_get):
    """A community endpoint should also honor the CN gateway."""
    client_id, client_secret = fake_credentials
    api = Diablo3CommunityApi(client_id, client_secret)
    prime_token(api)

    api.get_character_class(region="cn", locale="zh_CN", class_slug="barbarian")

    args, kwargs = mock_get.call_args
    assert args[0] == ("https://gateway.battlenet.com.cn/d3/data/hero/barbarian")
    assert kwargs["params"] == {"locale": "zh_CN"}


# ---------------------------------------------------------------------------
# Token acquisition
# ---------------------------------------------------------------------------


def test_missing_token_triggers_oauth_post(fake_credentials, mock_get, mock_post):
    """When no token is primed, BaseApi must POST to /oauth/token first."""
    client_id, client_secret = fake_credentials
    api = Diablo3GameDataApi(client_id, client_secret)
    # Note: NOT calling prime_token — force the OAuth round-trip.

    api.get_era_index(region="us")

    mock_post.assert_called_once()
    post_args, post_kwargs = mock_post.call_args
    assert post_args[0] == "https://oauth.battle.net/oauth/token"
    assert post_kwargs["params"] == {"grant_type": "client_credentials"}
    assert post_kwargs["auth"] == (client_id, client_secret)

    args, kwargs = mock_get.call_args
    assert args[0] == "https://us.api.blizzard.com/data/d3/era/"
    assert kwargs["headers"] == {"Authorization": f"Bearer {FAKE_TOKEN}"}
