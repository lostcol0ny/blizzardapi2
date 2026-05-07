"""Battle.net OAuth API client.

This module provides access to Battle.net OAuth endpoints,
including user information and authentication.
"""

from typing import Any

from ..api import BaseApi
from ..types import OptionalRegion


class BattlenetOAuthApi(BaseApi):
    """Battle.net OAuth API client.

    This class provides access to the Battle.net OAuth API endpoints.
    It handles authentication and request formatting for all OAuth related
    endpoints.

    Attributes:
        _client_id: The Blizzard API client ID.
        _client_secret: The Blizzard API client secret.
    """

    def get_user_info(
        self, access_token: str, *, region: OptionalRegion = None
    ) -> dict[str, Any]:
        """Get basic information about the user associated with the current bearer token.

        Args:
            access_token: The OAuth access token.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.

        Returns:
            A dictionary containing user information.

        Raises:
            requests.HTTPError: If the API request fails (raised via
                ``response.raise_for_status()`` in ``BaseApi._make_request``).
        """
        resource = "/oauth/userinfo"
        query_params = {
            "access_token": access_token,
        }
        return super().get_oauth_resource(resource, region, query_params)
