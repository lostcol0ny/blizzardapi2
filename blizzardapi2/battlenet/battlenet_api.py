"""Battle.net API client.

This module provides access to Battle.net API endpoints,
including OAuth authentication and user information.
"""

from .battlenet_oauth_api import BattlenetOauthApi


class BattlenetApi:
    """Battle.net API client.

    This class provides access to Battle.net API functionality through the Blizzard API,
    including OAuth authentication and user information.

    Example:
        ```python
        # Synchronous usage
        api = BattlenetApi(client_id="your_id", client_secret="your_secret")
        user_info = api.oauth.get_user_info("us", "access_token")

        # Asynchronous usage
        async with BattlenetApi(client_id="your_id", client_secret="your_secret") as api:
            user_info = await api.oauth.get_user_info("us", "access_token")
        ```

    Attributes:
        client_id: The Blizzard API client ID.
        client_secret: The Blizzard API client secret.
        oauth: The Battle.net OAuth API client instance.
    """

    def __init__(self, client_id: str, client_secret: str) -> None:
        """Initialize the Battle.net API client.

        Args:
            client_id: The Blizzard API client ID.
            client_secret: The Blizzard API client secret.

        Raises:
            ValueError: If client_id or client_secret is empty.
        """
        if not client_id or not client_secret:
            raise ValueError("client_id and client_secret must not be empty")
        self.oauth = BattlenetOauthApi(client_id, client_secret)
