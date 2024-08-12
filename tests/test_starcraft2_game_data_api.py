from blizzardapi2 import BlizzardApi


class TestStarcraft2GameDataApi:
    def setup_method(self):
        self.api = BlizzardApi("client_id", "client_secret")
        self.api.starcraft2.game_data._access_token = "access_token"

    # Starcraft 2 League API

    def test_get_league_data(self, success_response_mock):
        self.api.starcraft2.game_data.get_league_data("us", 37, 201, 1, 6)
        params = {}
        headers = {
            "Authorization": "Bearer access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/sc2/league/37/201/1/6", params=params, headers=headers
        )
