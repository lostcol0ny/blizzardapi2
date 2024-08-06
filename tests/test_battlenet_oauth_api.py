from blizzardapi2 import BlizzardApi
from time import time


class TestBattlenetOauthApi:
    def setup_method(self):
        self.api = BlizzardApi("client_id", "client_secret")
        self.api.battlenet.oauth._token_expiration = time() + 3600
        self.api.battlenet.oauth._access_token = "access_token"

    # User Authentication

    def test_get_user_info(self, success_response_mock):
        self.api.battlenet.oauth.get_user_info("us", "new_access_token")
        params = {
            "access_token": "new_access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.battle.net/oauth/userinfo", params=params
        )
