"""Battle.net OAuth API client.

This module provides access to Battle.net OAuth endpoints,
including user information and authentication.
"""

from typing import Any, Dict

from ..api import BaseApi
from ..types import Locale, Region


class ApiResponse:
    """Wrapper for API responses with metadata."""

    data: Dict[str, Any]
    region: Region
    locale: Locale
    namespace: str


class BattlenetOAuthApi(BaseApi):
    """Battle.net OAuth API client.

    This class provides access to the Battle.net OAuth API endpoints.
    It handles authentication and request formatting for all OAuth related
    endpoints.

    Attributes:
        _client_id: The Blizzard API client ID.
        _client_secret: The Blizzard API client secret.
    """

    def __init__(self, client_id: str, client_secret: str) -> None:
        """Initialize the API client.

        Args:
            client_id: The Blizzard API client ID.
            client_secret: The Blizzard API client secret.
        """
        super().__init__(client_id, client_secret)

    def get_user_info(self, region: Region, access_token: str) -> dict[str, Any]:
        """Get basic information about the user associated with the current bearer token.

        Args:
            region: The region to query (e.g., "us", "eu").
            access_token: The OAuth access token.

        Returns:
            A dictionary containing user information.

        Raises:
            ApiError: If the API request fails.
        """
        resource = "/oauth/userinfo"
        query_params = {
            "access_token": access_token,
        }
        return super().get_oauth_resource(resource, region, query_params)
