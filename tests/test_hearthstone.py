"""Tests for the Hearthstone APIs.

These tests verify URL construction, query-parameter shape, and return-value
passthrough for both ``HearthstoneApi`` (the facade exposed on
``BlizzardApi.hearthstone``) and ``HearthstoneGameDataApi``. All HTTP is
patched at the ``requests.Session`` boundary via the ``mock_get`` fixture.
"""

from __future__ import annotations

from blizzardapi2.blizzard_api import BlizzardApi
from blizzardapi2.hearthstone.hearthstone_api import HearthstoneApi
from blizzardapi2.hearthstone.hearthstone_game_data_api import (
    HearthstoneGameDataApi,
)

from tests.conftest import prime_token


def test_blizzard_api_exposes_hearthstone_facade(fake_credentials):
    """``BlizzardApi.hearthstone`` should be a ``HearthstoneApi`` instance."""
    client_id, client_secret = fake_credentials
    api = BlizzardApi(client_id, client_secret)

    assert isinstance(api.hearthstone, HearthstoneApi)
    # Facade should carry the same credentials through to the sub-client.
    assert api.hearthstone._client_id == client_id
    assert api.hearthstone._client_secret == client_secret


def test_get_cards_builds_us_url_with_locale(fake_credentials, mock_get):
    """``get_cards`` hits ``/hearthstone/cards`` with the locale param."""
    client_id, client_secret = fake_credentials
    api = HearthstoneApi(client_id, client_secret)
    prime_token(api)

    api.get_cards("us", "en_US")

    mock_get.assert_called_once()
    args, kwargs = mock_get.call_args
    assert args[0] == "https://us.api.blizzard.com/hearthstone/cards"
    assert kwargs["params"] == {"locale": "en_US"}


def test_get_card_includes_id_in_path(fake_credentials, mock_get):
    """``get_card`` interpolates the card id into the URL path."""
    client_id, client_secret = fake_credentials
    api = HearthstoneApi(client_id, client_secret)
    prime_token(api)

    api.get_card("eu", "en_GB", "52119-arch-villain-rafaam")

    args, kwargs = mock_get.call_args
    assert (
        args[0]
        == "https://eu.api.blizzard.com/hearthstone/cards/52119-arch-villain-rafaam"
    )
    assert kwargs["params"] == {"locale": "en_GB"}


def test_get_cards_returns_mocked_payload(fake_credentials, mock_get):
    """The dict returned by the client should be exactly what ``json()`` returned."""
    payload = {"cards": [{"id": 1, "name": "Test Card"}], "cardCount": 1}
    mock_get.return_value.json.return_value = payload

    client_id, client_secret = fake_credentials
    api = HearthstoneApi(client_id, client_secret)
    prime_token(api)

    result = api.get_cards("us", "en_US")

    assert result == payload


def test_get_card_backs_uses_cn_gateway(fake_credentials, mock_get):
    """CN region must route to the Chinese gateway, not a regional subdomain."""
    client_id, client_secret = fake_credentials
    api = HearthstoneApi(client_id, client_secret)
    prime_token(api)

    api.get_card_backs("cn", "zh_CN")

    args, kwargs = mock_get.call_args
    assert args[0] == "https://gateway.battlenet.com.cn/hearthstone/cardbacks"
    assert kwargs["params"] == {"locale": "zh_CN"}


def test_search_cards_maps_card_class_to_class_param(fake_credentials, mock_get):
    """``card_class`` kwarg is renamed to ``class`` (Python-keyword workaround)."""
    client_id, client_secret = fake_credentials
    api = HearthstoneGameDataApi(client_id, client_secret)
    prime_token(api)

    api.search_cards(
        "us",
        "en_US",
        card_class="mage",
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

    api.search_cards("us", "en_US", set="rise-of-shadows")

    _, kwargs = mock_get.call_args
    assert "class" not in kwargs["params"]
    assert kwargs["params"] == {"locale": "en_US", "set": "rise-of-shadows"}


def test_game_data_get_card_sends_default_game_mode(fake_credentials, mock_get):
    """``HearthstoneGameDataApi.get_card`` defaults ``game_mode`` to constructed."""
    client_id, client_secret = fake_credentials
    api = HearthstoneGameDataApi(client_id, client_secret)
    prime_token(api)

    api.get_card("us", "en_US", "52119-arch-villain-rafaam")

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

    api.get_metadata_type("kr", "ko_KR", "sets")

    args, kwargs = mock_get.call_args
    assert args[0] == "https://kr.api.blizzard.com/hearthstone/metadata/sets"
    assert kwargs["params"] == {"locale": "ko_KR"}
