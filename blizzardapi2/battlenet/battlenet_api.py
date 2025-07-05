"""battlenet_api.py file."""

from typing import Any

from .battlenet_oauth_api import BattlenetOAuthApi


class BattlenetApi:
    """Battle.net API class.

    Attributes:
        client_id (str): A string client id supplied by Blizzard.
        client_secret (str): A string client secret supplied by Blizzard.
    """

    def __init__(self, client_id: str, client_secret: str) -> dict[str, Any]:
        """Init BattlenetApi."""
        self.oauth = BattlenetOAuthApi(client_id, client_secret)
