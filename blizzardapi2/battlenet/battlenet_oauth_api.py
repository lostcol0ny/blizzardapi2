"""Battle.net OAuth API client.

This module provides access to Battle.net OAuth endpoints,
including user information and authentication.
"""

from typing import Any

from ..api import Api, Region


class BattlenetOauthApi(Api):
    """Battle.net OAuth API client.

    This class provides access to Battle.net OAuth functionality through the Blizzard API,
    including user information and authentication.

    Example:
        ```python
        # Synchronous usage
        api = BattlenetOauthApi(client_id="your_id", client_secret="your_secret")
        user_info = api.get_user_info("us", "access_token")

        # Asynchronous usage
        async with BattlenetOauthApi(client_id="your_id", client_secret="your_secret") as api:
            user_info = await api.get_user_info("us", "access_token")
        ```

    Attributes:
        client_id: The Blizzard API client ID.
        client_secret: The Blizzard API client secret.
    """

    def __init__(self, client_id: str, client_secret: str) -> None:
        """Initialize the Battle.net OAuth API client.

        Args:
            client_id: The Blizzard API client ID.
            client_secret: The Blizzard API client secret.

        Raises:
            ValueError: If client_id or client_secret is empty.
        """
        if not client_id or not client_secret:
            raise ValueError("client_id and client_secret must not be empty")
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
