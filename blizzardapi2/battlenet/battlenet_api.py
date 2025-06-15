"""Battle.net API client.

This module provides access to Battle.net API endpoints,
including OAuth authentication and user information.
"""

from ..api import BaseApi
from .battlenet_oauth_api import BattlenetOAuthApi


class BattlenetApi(BaseApi):
    """Battle.net API client.

    This class provides access to all Battle.net API endpoints.
    It organizes access to OAuth functionality through the BattlenetOAuthApi
    component.

    Attributes:
        _client_id: The Blizzard API client ID.
        _client_secret: The Blizzard API client secret.
        oauth: Client for OAuth endpoints.
    """

    def __init__(self, client_id: str, client_secret: str) -> None:
        """Initialize the API client.

        Args:
            client_id: The Blizzard API client ID.
            client_secret: The Blizzard API client secret.
        """
        super().__init__(client_id, client_secret)
        self.oauth = BattlenetOAuthApi(client_id, client_secret)
