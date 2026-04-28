"""Tests for the Starcraft 2 API surface.

These tests exercise the `Starcraft2Api` facade plus the community and game-data
sub-clients. We patch `requests.Session.get` (via the shared `mock_get` fixture)
and assert URL construction, query-parameter shape, and that the parsed JSON
body is returned to the caller. The `prime_token` helper short-circuits the
OAuth POST so each test only verifies a single GET.
"""

from __future__ import annotations

from blizzardapi2.starcraft2.starcraft2_api import Starcraft2Api
from blizzardapi2.starcraft2.starcraft2_community_api import (
    Starcraft2CommunityApi,
)
from blizzardapi2.starcraft2.starcraft2_game_data_api import (
    Starcraft2GameDataApi,
)

from tests.conftest import FAKE_TOKEN, prime_token


def test_facade_exposes_typed_subclients(fake_credentials):
    """`Starcraft2Api` should wire up community and game_data sub-clients."""
    client_id, client_secret = fake_credentials
    api = Starcraft2Api(client_id, client_secret)

    assert isinstance(api.community, Starcraft2CommunityApi)
    assert isinstance(api.game_data, Starcraft2GameDataApi)


def test_community_get_static_builds_us_url(fake_credentials, mock_get):
    """Community static endpoint hits the regional host with locale param."""
    client_id, client_secret = fake_credentials
    api = Starcraft2Api(client_id, client_secret)
    prime_token(api.community)

    mock_get.return_value.json.return_value = {"achievements": []}

    result = api.community.get_static(region="us", locale="en_US", region_id=1)

    assert result == {"achievements": []}
    args, kwargs = mock_get.call_args
    assert args[0] == "https://us.api.blizzard.com/sc2/static/profile/1"
    assert kwargs["params"] == {"locale": "en_US"}
    assert kwargs["headers"] == {"Authorization": f"Bearer {FAKE_TOKEN}"}


def test_community_get_metadata_builds_eu_url(fake_credentials, mock_get):
    """Metadata endpoint should interpolate region_id, realm_id, profile_id."""
    client_id, client_secret = fake_credentials
    api = Starcraft2Api(client_id, client_secret)
    prime_token(api.community)

    api.community.get_metadata(
        region="eu",
        locale="en_GB",
        region_id=2,
        realm_id=1,
        profile_id=12345,
    )

    args, kwargs = mock_get.call_args
    assert args[0] == "https://eu.api.blizzard.com/sc2/metadata/profile/2/1/12345"
    assert kwargs["params"] == {"locale": "en_GB"}


def test_community_get_profile_merges_extra_query_params(fake_credentials, mock_get):
    """`get_profile` accepts **query_params and merges locale on top."""
    client_id, client_secret = fake_credentials
    api = Starcraft2Api(client_id, client_secret)
    prime_token(api.community)

    api.community.get_profile(
        region="us",
        locale="en_US",
        region_id=1,
        realm_id=1,
        profile_id=999,
        extra="value",
    )

    args, kwargs = mock_get.call_args
    assert args[0] == "https://us.api.blizzard.com/sc2/profile/1/1/999"
    assert kwargs["params"] == {"locale": "en_US", "extra": "value"}


def test_community_get_ladder_summary_returns_mocked_payload(
    fake_credentials, mock_get
):
    """Ladder summary returns whatever `mock_get` was configured to return."""
    client_id, client_secret = fake_credentials
    api = Starcraft2Api(client_id, client_secret)
    prime_token(api.community)

    payload = {"showCaseEntries": [{"teamId": 1}]}
    mock_get.return_value.json.return_value = payload

    result = api.community.get_ladder_summary(
        region="us", locale="en_US", region_id=1, realm_id=1, profile_id=42
    )

    assert result == payload
    args, kwargs = mock_get.call_args
    assert args[0] == "https://us.api.blizzard.com/sc2/profile/1/1/42/ladder/summary"
    assert kwargs["params"] == {"locale": "en_US"}


def test_community_get_grandmaster_leaderboard_url_shape(fake_credentials, mock_get):
    """Note: source concatenates region_id directly to 'grandmaster' (no slash)."""
    client_id, client_secret = fake_credentials
    api = Starcraft2Api(client_id, client_secret)
    prime_token(api.community)

    api.community.get_grandmaster_leaderboard(region="us", locale="en_US", region_id=1)

    args, kwargs = mock_get.call_args
    # This mirrors the source as written: f"/sc2/ladder/grandmaster{region_id}"
    assert args[0] == "https://us.api.blizzard.com/sc2/ladder/grandmaster1"
    assert kwargs["params"] == {"locale": "en_US"}


def test_community_cn_region_uses_gateway_host(fake_credentials, mock_get):
    """CN region must route through the China gateway, not {region}.api.blizzard.com."""
    client_id, client_secret = fake_credentials
    api = Starcraft2Api(client_id, client_secret)
    prime_token(api.community)

    api.community.get_player(region="cn", locale="zh_CN", account_id=7)

    args, kwargs = mock_get.call_args
    assert args[0] == "https://gateway.battlenet.com.cn/sc2/player/7"
    assert kwargs["params"] == {"locale": "zh_CN"}


def test_game_data_get_league_data_no_query_params(fake_credentials, mock_get):
    """Game-data league endpoint sends no query params (locale not used)."""
    client_id, client_secret = fake_credentials
    api = Starcraft2Api(client_id, client_secret)
    prime_token(api.game_data)

    mock_get.return_value.json.return_value = {"tier": []}

    result = api.game_data.get_league_data(
        region="us",
        season_id=37,
        queue_id=201,
        team_type=0,
        league_id=2,
    )

    assert result == {"tier": []}
    args, kwargs = mock_get.call_args
    assert args[0] == "https://us.api.blizzard.com/data/sc2/league/37/201/0/2"
    # `get_league_data` passes no query_params, so BaseApi sends an empty dict.
    assert kwargs["params"] == {}


def test_subclients_have_independent_token_state(fake_credentials, mock_get):
    """Community and game_data are separate BaseApi instances with their own tokens."""
    client_id, client_secret = fake_credentials
    api = Starcraft2Api(client_id, client_secret)

    # Prime only the community client.
    prime_token(api.community)

    assert api.community._access_token == FAKE_TOKEN
    assert api.game_data._access_token is None
