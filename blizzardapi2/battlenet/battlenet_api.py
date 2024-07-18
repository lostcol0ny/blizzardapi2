"""battlenet_api.py file."""
from typing import Dict, Any
from .battlenet_oauth_api import BattlenetOauthApi


class BattlenetApi:
    """Battle.net API class.

    Attributes:
        client_id: A string client id supplied by Blizzard.
        client_secret: A string client secret supplied by Blizzard.
    """

    def __init__(self, client_id: str, client_secret: str) -> Dict[str, Any]:
        """Init BattlenetApi."""
        self.oauth = BattlenetOauthApi(client_id, client_secret)
