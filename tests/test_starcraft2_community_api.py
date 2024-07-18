from blizzardapi2 import BlizzardApi


class TestStarcraft2CommunityApi:
    def setup_method(self):
        self.api = BlizzardApi("client_id", "client_secret")
        self.api.starcraft2.community._access_token = "access_token"

    # Profile API

    def test_get_static(self, success_response_mock):
        self.api.starcraft2.community.get_static("us", "en_US", 1)
        params = {
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/sc2/static/profile/1",
            params=params
        )

    def test_get_metadata(self, success_response_mock):
        self.api.starcraft2.community.get_metadata("us", "en_US", 1, 1, 11073152)
        params = {
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/sc2/metadata/profile/1/1/11073152",
            params=params
        )

    def test_get_profile(self, success_response_mock):
        self.api.starcraft2.community.get_profile("us", "en_US", 1, 1, 11073152)
        params = {
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/sc2/profile/1/1/11073152",
            params=params
        )
        
    def test_get_ladder_summary(self, success_response_mock):
        self.api.starcraft2.community.get_ladder_summary("us", "en_US", 1, 1, 11073152)
        params = {
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/sc2/profile/1/1/11073152/ladder/summary",
            params=params
        )
        
    def test_get_ladder(self, success_response_mock):
        self.api.starcraft2.community.get_ladder("us", "en_US", 1, 1, 11073152, 5)
        params = {
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/sc2/profile/1/1/11073152/ladder/5",
            params=params
        )
        
    # Ladder API

    def test_get_grandmaster_leaderboard(self, success_response_mock):
        self.api.starcraft2.community.get_grandmaster_leaderboard("us", "en_US",  1)
        params = {
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/sc2/ladder/grandmaster1",
            params=params
        )

    def test_get_season(self, success_response_mock):
        self.api.starcraft2.community.get_season("us", "en_US", 1)
        params = {
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/sc2/ladder/season/1",
            params=params
        )

    # D3 Follower API

    def test_get_player(self, success_response_mock):
        self.api.starcraft2.community.get_player("us", "en_US", 90210)
        params = {
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/sc2/player/90210",
            params=params
        )
