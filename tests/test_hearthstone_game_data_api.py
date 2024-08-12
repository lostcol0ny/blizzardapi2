from blizzardapi2 import BlizzardApi


class TestHearthstoneGameDataApi:
    def setup_method(self):
        self.api = BlizzardApi("client_id", "client_secret")
        self.api.hearthstone.game_data._access_token = "access_token"

    # Cards

    def test_search_cards(self, success_response_mock):
        self.api.hearthstone.game_data.search_cards("us", "en_US")
        params = {
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/hearthstone/cards", params=params, headers=headers
        )

    def test_get_card(self, success_response_mock):
        self.api.hearthstone.game_data.get_card(
            "us", "en_US", "52119-arch-villain-rafaam"
        )
        params = {
            "locale": "en_US",
            "game_mode": "constructed",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/hearthstone/cards/52119-arch-villain-rafaam",
            params=params, headers=headers,
        )

    # Card Backs

    def test_search_card_backs(self, success_response_mock):
        self.api.hearthstone.game_data.search_card_backs("us", "en_US")
        params = {
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/hearthstone/cardbacks", params=params, headers=headers
        )

    def test_get_card_back(self, success_response_mock):
        self.api.hearthstone.game_data.get_card_back("us", "en_US", "155-pizza-stone")
        params = {
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/hearthstone/cardbacks/155-pizza-stone",
            params=params, headers=headers,
        )

    # Decks

    def test_get_deck(self, success_response_mock):
        self.api.hearthstone.game_data.get_deck("us", "en_US")
        params = {
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/hearthstone/deck", params=params, headers=headers
        )

    # Metadata

    def test_get_metadata(self, success_response_mock):
        self.api.hearthstone.game_data.get_metadata("us", "en_US")
        params = {
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/hearthstone/metadata", params=params, headers=headers
        )

    def test_get_metadata_type(self, success_response_mock):
        self.api.hearthstone.game_data.get_metadata_type("us", "en_US", "sets")
        params = {
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/hearthstone/metadata/sets",
            params=params, headers=headers,
        )
