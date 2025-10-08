"""api.py file."""

from datetime import UTC, datetime, timedelta
from typing import Any, Optional

import requests


class BaseApi:
    """Base API class for Blizzard API clients.

    Provides common functionality for authentication, token management,
    and HTTP requests to Blizzard APIs.

    Attributes:
        _client_id: Blizzard API client ID.
        _client_secret: Blizzard API client secret.
        _access_token: Current access token for API requests.
        _access_token_expiration_datetime: Token expiration timestamp.
        _session: HTTP session for making requests.
    """

    def __init__(self, client_id: str, client_secret: str) -> None:
        """Initialize the API client.

        Args:
            client_id: Blizzard API client ID.
            client_secret: Blizzard API client secret.
        """
        self._client_id = client_id
        self._client_secret = client_secret
        self._access_token: Optional[str] = None
        self._access_token_expiration_datetime: Optional[str] = None
        self._session = requests.Session()

    def _is_token_expired(self) -> bool:
        """Check if the token is expiring within next 5 minutes."""
        # If we don't have an expiration datetime, consider the token expired
        if self._access_token_expiration_datetime is None:
            return True

        current_time = (
            datetime.now(UTC).isoformat(timespec="milliseconds").replace("+00:00", "Z")
        )
        datetime_format = "%Y-%m-%dT%H:%M:%S.%fZ"
        blizz_expire_obj = datetime.strptime(
            self._access_token_expiration_datetime, datetime_format
        )
        current_datetime_obj = datetime.strptime(current_time, datetime_format)

        time_difference = abs(blizz_expire_obj - current_datetime_obj)

        return time_difference <= timedelta(minutes=5)

    def _get_client_token(self, region: str) -> dict[str, Any]:
        """Fetch an access token based on client id and client secret credentials.

        Args:
            region:
                A string containing a region.
        """
        url = self._format_oauth_url("/oauth/token", region)
        query_params = {"grant_type": "client_credentials"}

        response = self._session.post(
            url,
            params=query_params,
            auth=(self._client_id, self._client_secret),
        )

        json_response = self._response_handler(response)
        self._access_token = json_response["access_token"]

        return json_response

    def _ensure_valid_token(self, region: str) -> None:
        """Ensure that the token is valid."""
        if self._access_token is None or self._is_token_expired():
            self._get_client_token(region)

    def _response_handler(self, response: requests.Response) -> dict[str, Any]:
        """Handle the response."""
        response.raise_for_status()
        return response.json()

    def _make_request(
        self, url: str, region: str, query_params: Optional[dict[str, Any]] = None
    ) -> dict[str, Any]:
        """Make an authenticated request to the API.

        Args:
            url: The complete URL to request.
            region: The region for token management.
            query_params: Optional query parameters.

        Returns:
            The API response as a dictionary.
        """
        self._ensure_valid_token(region)

        # Prepare query parameters
        if query_params is None:
            query_params = {}
        else:
            query_params = query_params.copy()

        # Remove access_token from query_params if it exists (for OAuth endpoints)
        query_params.pop("access_token", None)

        headers = {"Authorization": f"Bearer {self._access_token}"}

        # Make the request
        response = self._session.get(url, params=query_params, headers=headers)

        # Update token expiration if provided in response headers
        self._update_token_expiration(response)

        # Handle token refresh if needed
        if response.status_code == 401 or self._is_token_expired():
            self._get_client_token(region)
            headers["Authorization"] = f"Bearer {self._access_token}"
            response = self._session.get(url, params=query_params, headers=headers)

        return self._response_handler(response)

    def _update_token_expiration(self, response: requests.Response) -> None:
        """Update token expiration from response headers.

        Args:
            response: The HTTP response object.
        """
        blizzard_token_expires = response.headers.get("blizzard-token-expires")
        if blizzard_token_expires is not None:
            self._access_token_expiration_datetime = blizzard_token_expires

    def _build_url(self, resource: str, region: str, is_oauth: bool = False) -> str:
        """Build the appropriate URL for the given resource and region.

        Args:
            resource: The API resource path.
            region: The region (us, eu, kr, tw, cn).
            is_oauth: Whether this is an OAuth endpoint.

        Returns:
            The complete URL for the request.
        """
        if region == "cn":
            if is_oauth:
                return f"https://www.gateway.battlenet.com.cn{resource}"
            else:
                return f"https://gateway.battlenet.com.cn{resource}"
        else:
            if is_oauth:
                return f"https://oauth.battle.net{resource}"
            else:
                return f"https://{region}.api.blizzard.com{resource}"

    def get_resource(
        self, resource: str, region: str, query_params: Optional[dict[str, Any]] = None
    ) -> dict[str, Any]:
        """Make a request to a regular API resource.

        Args:
            resource: The API resource path.
            region: The region to query.
            query_params: Optional query parameters.

        Returns:
            The API response as a dictionary.
        """
        url = self._build_url(resource, region, is_oauth=False)
        return self._make_request(url, region, query_params)

    def get_oauth_resource(
        self, resource: str, region: str, query_params: Optional[dict[str, Any]] = None
    ) -> dict[str, Any]:
        """Make a request to an OAuth API resource.

        Args:
            resource: The API resource path.
            region: The region to query.
            query_params: Optional query parameters.

        Returns:
            The API response as a dictionary.
        """
        url = self._build_url(resource, region, is_oauth=True)
        return self._make_request(url, region, query_params)
