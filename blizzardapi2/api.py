"""api.py file."""

from datetime import UTC, datetime, timedelta
from typing import Any, Optional

import requests

from .endpoint import ApiEndpoint
from .types import Locale, OptionalLocale, OptionalRegion, Region


class BaseApi(ApiEndpoint):
    """Shared API services for Blizzard API clients.

    Provides common functionality for authentication, token management,
    and HTTP requests to Blizzard APIs.
    """

    # Region-specific URL mappings
    OAUTH_URLS = {
        "cn": "https://www.gateway.battlenet.com.cn",
        "default": "https://oauth.battle.net",
    }

    API_URLS = {
        "cn": "https://gateway.battlenet.com.cn",
        "default": "https://{region}.api.blizzard.com",
    }

    TOKEN_REFRESH_BUFFER = timedelta(minutes=5)

    # Per-request timeouts (seconds). Subclass and override either constant
    # to customize. `requests` defaults to no timeout, which lets a hung
    # Blizzard endpoint wedge the caller indefinitely.
    DEFAULT_GET_TIMEOUT = 30.0
    DEFAULT_POST_TIMEOUT = 10.0

    def extend_endpoint(self) -> None:
        self._access_token: Optional[str] = None
        self._token_expires_at: Optional[datetime] = None
        self._session = requests.Session()

    def _is_token_expired(self) -> bool:
        """Check if the token is expiring within the refresh buffer window."""
        if self._token_expires_at is None:
            return True
        return datetime.now(UTC) >= self._token_expires_at - self.TOKEN_REFRESH_BUFFER

    def _get_client_token(self, region: str) -> dict[str, Any]:
        """Fetch an access token using client credentials flow.

        Args:
            region: The region to query (e.g., us, eu, kr, tw, cn).  Defaults to None, in which case the default region provided at instantiation is used.

        Returns:
            The token response from the API.
        """
        url = self._build_oauth_url("/oauth/token", region)
        response = self._session.post(
            url,
            params={"grant_type": "client_credentials"},
            auth=(self.client_id, self._client_secret),
            timeout=self.DEFAULT_POST_TIMEOUT,
        )
        response.raise_for_status()
        token_data = response.json()

        # Store token and calculate expiration
        self._access_token = token_data["access_token"]
        expires_in = token_data.get("expires_in", 86400)  # Default 24 hours
        self._token_expires_at = datetime.now(UTC) + timedelta(seconds=expires_in)

        return token_data

    def _ensure_valid_token(self, region: str) -> None:
        """Ensure we have a valid client credentials token."""
        if self._access_token is None or self._is_token_expired():
            self._get_client_token(region)

    def _build_oauth_url(self, resource: str, region: Region | str) -> str:
        """Build URL for OAuth endpoints.

        Args:
            resource: The API resource path.
            region: The region to query (e.g., us, eu, kr, tw, cn).  Defaults to None, in which case the default region provided at instantiation is used.

        Returns:
            The complete OAuth URL.
        """
        base_url = self.OAUTH_URLS.get(region, self.OAUTH_URLS["default"])
        return f"{base_url}{resource}"

    def _build_api_url(self, resource: str, region: str) -> str:
        """Build URL for regular API endpoints.

        Args:
            resource: The API resource path.
            region: The region to query (e.g., us, eu, kr, tw, cn).  Defaults to None, in which case the default region provided at instantiation is used.

        Returns:
            The complete API URL.
        """
        base_url = self.API_URLS.get(
            region, self.API_URLS["default"].format(region=region)
        )
        return f"{base_url}{resource}"

    def _make_request(
        self,
        url: str,
        region: str,
        query_params: Optional[dict[str, Any]] = None,
    ) -> dict[str, Any]:
        """Make an authenticated request to the API.

        Args:
            url: The complete URL to request.
            region: The region to query (e.g., us, eu, kr, tw, cn).  Defaults to None, in which case the default region provided at instantiation is used.
            query_params: Optional query parameters.

        Returns:
            The API response as a dictionary.
        """
        # Prepare query parameters
        params = (query_params or {}).copy()

        # Check if user provided their own access token
        user_token = params.pop("access_token", None)

        # Determine which token to use
        if user_token:
            # Use user-provided token (for OAuth user endpoints)
            token = user_token
        else:
            # Ensure client credentials token is valid
            self._ensure_valid_token(region)
            token = self._access_token

        # Make the request
        response = self._session.get(
            url,
            params=params,
            headers={"Authorization": f"Bearer {token}"},
            timeout=self.DEFAULT_GET_TIMEOUT,
        )

        # Handle 401 errors for client credentials (not user tokens)
        if response.status_code == 401 and not user_token:
            # Token might have expired, refresh and retry
            self._get_client_token(region)
            response = self._session.get(
                url,
                params=params,
                headers={"Authorization": f"Bearer {self._access_token}"},
                timeout=self.DEFAULT_GET_TIMEOUT,
            )

        response.raise_for_status()
        return response.json()

    def get_resource(
        self,
        resource: str,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
        query_params: Optional[dict[str, Any]] = None,
    ) -> dict[str, Any]:
        """Make a request to a regular API resource.

        Args:
            resource: The API resource path.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.
            query_params: Optional query parameters.

        Returns:
            The API response as a dictionary.
        """
        _region = Region(region or self.region)
        url = self._build_api_url(resource, _region)
        return self._make_request(url, _region, query_params)

    def get_oauth_resource(
        self,
        resource: str,
        region: OptionalRegion = None,
        query_params: Optional[dict[str, Any]] = None,
    ) -> dict[str, Any]:
        """Make a request to an OAuth API resource.

        Args:
            resource: The API resource path.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            query_params: Optional query parameters.

        Returns:
            The API response as a dictionary.
        """
        _region = Region(region or self.region)
        url = self._build_oauth_url(resource, _region)
        return self._make_request(url, _region, query_params)


class LocaleApi(BaseApi):
    """Locale-aware  API class for Blizzard API clients.

    Extends the base API to handle locale-aware services
    """

    def get_resource(
        self,
        resource: str,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
        query_params: Optional[dict[str, Any]] = None,
    ) -> dict[str, Any]:
        """Make a request to a locale-aware API resource.

        Args:
            resource: The API resource path.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.
            query_params: Optional query parameters.

        Returns:
            The API response as a dictionary.
        """
        # Allow the locale in the query_params (if any) to override any othe locale provided (explicitly or by default)
        _query_params = (query_params or {})
        if _query_params.get("locale") is None:
            _query_params["locale"] = Locale(locale or self.locale)
        return super().get_resource(resource, region=region, query_params=_query_params)
