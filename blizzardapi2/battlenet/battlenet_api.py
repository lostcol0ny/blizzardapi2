"""battlenet_api.py file."""

from ..endpoint import ApiEndpoint
from .battlenet_oauth_api import BattlenetOAuthApi


class BattlenetApi(ApiEndpoint):
    """Battle.net API class.

    Attributes:
        client_id (str): A string client id supplied by Blizzard.
        client_secret (str): A string client secret supplied by Blizzard.
        region (Region, optional): Default region to use for requests.
        oauth (BattlenetOAuthApi): An instance of the BattlenetOAuthApi class for accessing OAuth endpoints.
    """

    def extend_endpoint(self) -> None:
        """Init BattlenetApi."""
        self.oauth = BattlenetOAuthApi(self.client_id, self.client_secret, self.region)
