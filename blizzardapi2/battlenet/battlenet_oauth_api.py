"""battlenet_oauth_api.py file."""

from ..api import Api


class BattlenetOauthApi(Api):
    """All Battle.net OAuth API methods.

    Attributes:
        client_id (str): A string client ID supplied by Blizzard.
        client_secret (str): A string client secret supplied by Blizzard.
    """

    def __init__(self, client_id: str, client_secret: str) -> None:
        """
        Initialize the BattlenetOauthApi class.

        Args:
            client_id (str): The client ID supplied by Blizzard.
            client_secret (str): The client secret supplied by Blizzard.
        """
        super().__init__(client_id, client_secret)

    def get_user_info(self, region: str, access_token: str) -> dict:
        """
        Return basic information about the user associated with the current bearer token.

        Args:
            region (str): The region to query (e.g., "us", "eu").
            access_token (str): The OAuth access token.

        Returns:
            dict: A dictionary containing user information.
        """
        resource = "/oauth/userinfo"
        query_params = {
            "access_token": access_token,
        }
        return super().get_oauth_resource(resource, region, query_params)
