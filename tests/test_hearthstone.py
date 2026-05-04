"""Tests for the Hearthstone APIs.

These tests verify URL construction, query-parameter shape, and return-value
passthrough through ``HearthstoneApi`` (the facade exposed on
``BlizzardApi.hearthstone``) and its ``game_data`` sub-client. All HTTP is
patched at the ``requests.Session`` boundary via the ``mock_get`` fixture.
"""

from __future__ import annotations

from blizzardapi2.blizzard_api import BlizzardApi
from blizzardapi2.hearthstone.hearthstone_api import HearthstoneApi
from blizzardapi2.hearthstone.hearthstone_game_data_api import HearthstoneGameDataApi
from tests.conftest import prime_token


def test_blizzard_api_exposes_hearthstone_facade(fake_credentials):
    """``BlizzardApi.hearthstone`` should be a ``HearthstoneApi`` instance."""
    client_id, client_secret = fake_credentials
    api = BlizzardApi(client_id, client_secret)

    assert isinstance(api.hearthstone, HearthstoneApi)
    # Facade should carry the same credentials through to the sub-client.
    assert api.hearthstone._client_id == client_id
    assert api.hearthstone._client_secret == client_secret


def test_hearthstone_facade_exposes_game_data(fake_credentials):
    """``HearthstoneApi.game_data`` should be a ``HearthstoneGameDataApi``.

    Issue #42: the game-data client used to be orphaned (not reachable from
    ``BlizzardApi``). It is now exposed under ``.game_data`` for consistency
    with ``wow.game_data``, ``diablo3.game_data``, ``starcraft2.game_data``.
    """
    client_id, client_secret = fake_credentials
    api = HearthstoneApi(client_id, client_secret)
    assert isinstance(api.game_data, HearthstoneGameDataApi)
    assert api.game_data._client_id == client_id
    assert api.game_data._client_secret == client_secret


def test_search_cards_no_filters_builds_bare_cards_url(fake_credentials, mock_get):
    """``search_cards`` with no filters hits ``/hearthstone/cards`` with locale only."""
    client_id, client_secret = fake_credentials
    api = HearthstoneApi(client_id, client_secret)
    prime_token(api.game_data)

    api.game_data.search_cards(region="us", locale="en_US")

    mock_get.assert_called_once()
    args, kwargs = mock_get.call_args
    assert args[0] == "https://us.api.blizzard.com/hearthstone/cards"
    assert kwargs["params"] == {"locale": "en_US"}


def test_get_card_includes_id_in_path_via_game_data(fake_credentials, mock_get):
    """``game_data.get_card`` interpolates the id/slug into the URL path."""
    client_id, client_secret = fake_credentials
    api = HearthstoneApi(client_id, client_secret)
    prime_token(api.game_data)

    api.game_data.get_card("52119-arch-villain-rafaam", region="eu", locale="en_GB")

    args, kwargs = mock_get.call_args
    assert (
        args[0]
        == "https://eu.api.blizzard.com/hearthstone/cards/52119-arch-villain-rafaam"
    )
    assert kwargs["params"] == {"locale": "en_GB", "game_mode": "constructed"}


def test_search_cards_returns_mocked_payload(fake_credentials, mock_get):
    """The dict returned by the client should be exactly what ``json()`` returned."""
    payload = {"cards": [{"id": 1, "name": "Test Card"}], "cardCount": 1}
    mock_get.return_value.json.return_value = payload

    client_id, client_secret = fake_credentials
    api = HearthstoneApi(client_id, client_secret)
    prime_token(api.game_data)

    result = api.game_data.search_cards(region="us", locale="en_US")

    assert result == payload


def test_search_card_backs_uses_cn_gateway(fake_credentials, mock_get):
    """CN region must route to the Chinese gateway, not a regional subdomain."""
    client_id, client_secret = fake_credentials
    api = HearthstoneApi(client_id, client_secret)
    prime_token(api.game_data)

    api.game_data.search_card_backs(region="cn", locale="zh_CN")

    args, kwargs = mock_get.call_args
    assert args[0] == "https://gateway.battlenet.com.cn/hearthstone/cardbacks"
    assert kwargs["params"] == {"locale": "zh_CN"}


def test_search_cards_maps_card_class_to_class_param(fake_credentials, mock_get):
    """``card_class`` kwarg is renamed to ``class`` (Python-keyword workaround)."""
    client_id, client_secret = fake_credentials
    api = HearthstoneGameDataApi(client_id, client_secret)
    prime_token(api)

    api.search_cards(
        card_class="mage",
        region="us",
        locale="en_US",
        manaCost=4,
        attack=3,
    )

    args, kwargs = mock_get.call_args
    assert args[0] == "https://us.api.blizzard.com/hearthstone/cards"
    assert kwargs["params"] == {
        "locale": "en_US",
        "class": "mage",
        "manaCost": 4,
        "attack": 3,
    }


def test_search_cards_omits_class_when_card_class_none(fake_credentials, mock_get):
    """When ``card_class`` is not supplied, no ``class`` param is sent."""
    client_id, client_secret = fake_credentials
    api = HearthstoneGameDataApi(client_id, client_secret)
    prime_token(api)

    api.search_cards(region="us", locale="en_US", set="rise-of-shadows")

    _, kwargs = mock_get.call_args
    assert "class" not in kwargs["params"]
    assert kwargs["params"] == {"locale": "en_US", "set": "rise-of-shadows"}


def test_game_data_get_card_sends_default_game_mode(fake_credentials, mock_get):
    """``HearthstoneGameDataApi.get_card`` defaults ``game_mode`` to constructed."""
    client_id, client_secret = fake_credentials
    api = HearthstoneGameDataApi(client_id, client_secret)
    prime_token(api)

    api.get_card("52119-arch-villain-rafaam", region="us", locale="en_US")

    args, kwargs = mock_get.call_args
    assert (
        args[0]
        == "https://us.api.blizzard.com/hearthstone/cards/52119-arch-villain-rafaam"
    )
    assert kwargs["params"] == {"locale": "en_US", "game_mode": "constructed"}


def test_get_metadata_type_path_includes_type_id(fake_credentials, mock_get):
    """``get_metadata_type`` interpolates the type id into the URL path."""
    client_id, client_secret = fake_credentials
    api = HearthstoneGameDataApi(client_id, client_secret)
    prime_token(api)

    api.get_metadata_type("sets", region="kr", locale="ko_KR")

    args, kwargs = mock_get.call_args
    assert args[0] == "https://kr.api.blizzard.com/hearthstone/metadata/sets"
    assert kwargs["params"] == {"locale": "ko_KR"}


def test_get_deck_preserves_caller_filters(fake_credentials, mock_get):
    """``get_deck`` must forward caller-supplied filters (issue #41).

    The previous implementation silently dropped every kwarg by overwriting
    `query_params = {"locale": locale}` after the **kwargs collection.
    """
    client_id, client_secret = fake_credentials
    api = HearthstoneGameDataApi(client_id, client_secret)
    prime_token(api)

    api.get_deck(
        region="us",
        locale="en_US",
        ids="EX1_046,EX1_054",
        hero="HERO_01",
    )

    args, kwargs = mock_get.call_args
    assert args[0] == "https://us.api.blizzard.com/hearthstone/deck"
    assert kwargs["params"] == {
        "locale": "en_US",
        "ids": "EX1_046,EX1_054",
        "hero": "HERO_01",
    }
