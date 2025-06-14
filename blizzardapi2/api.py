"""api.py file."""

from dataclasses import dataclass
from datetime import UTC, datetime, timedelta
from enum import Enum
from typing import (Any, Dict, Final, Literal, Optional, Protocol, Self,
                    TypedDict)

import aiohttp
import requests

# Type aliases for better type safety
HTTPMethod = Literal["GET", "POST", "PUT", "DELETE", "PATCH"]
RegionType = Literal["us", "eu", "kr", "tw", "cn"]


class Region(str, Enum):
    """Valid regions for the WoW API."""

    US = "us"
    EU = "eu"
    KR = "kr"
    TW = "tw"
    CN = "cn"


class Locale(str, Enum):
    """Valid locales for the WoW API."""

    EN_US = "en_US"
    EN_GB = "en_GB"
    ES_MX = "es_MX"
    PT_BR = "pt_BR"
    DE_DE = "de_DE"
    ES_ES = "es_ES"
    FR_FR = "fr_FR"
    IT_IT = "it_IT"
    PT_PT = "pt_PT"
    RU_RU = "ru_RU"
    KO_KR = "ko_KR"
    ZH_TW = "zh_TW"
    ZH_CN = "zh_CN"


class TokenResponse(TypedDict):
    """Type definition for OAuth token response."""

    access_token: str
    token_type: str
    expires_in: int


class ErrorResponse(Protocol):
    """Protocol defining the structure of error response objects.
    
    This protocol defines the minimum interface that any error response object
    must implement to be compatible with our error handling system. It's used
    to ensure type safety when working with different HTTP client libraries
    (requests, aiohttp, etc.).
    
    The `...` in the method bodies indicates that the actual implementation
    will be provided by the concrete classes that implement this protocol.
    """
    
    @property
    def status_code(self) -> Optional[int]:
        """Get the HTTP status code from the response.
        
        Returns:
            Optional[int]: The HTTP status code, or None if not available.
        """
        ...
    
    @property
    def headers(self) -> Dict[str, str]:
        """Get the response headers.
        
        Returns:
            Dict[str, str]: A dictionary of response headers.
        """
        ...
    
    def json(self) -> Dict[str, Any]:
        """Parse the response body as JSON.
        
        Returns:
            Dict[str, Any]: The parsed JSON response.
            
        Raises:
            ValueError: If the response body is not valid JSON.
        """
        ...


@dataclass(slots=True, frozen=True)
class BlizzardAPIError(Exception):
    """Base exception for Blizzard API errors.

    This is the base exception class for all Blizzard API related errors.
    It includes additional context about the error and the request that caused it.
    """

    message: str
    status_code: Optional[int] = None
    response: Optional[ErrorResponse] = None
    request_url: Optional[str] = None
    request_method: Optional[HTTPMethod] = None
    request_params: Optional[Dict[str, Any]] = None

    def __post_init__(self) -> None:
        """Initialize the error with the message."""
        super().__init__(self.message)

    def __str__(self) -> str:
        """Return a string representation of the error."""
        error_parts = [self.message]

        if self.status_code:
            error_parts.append(f"Status code: {self.status_code}")

        if self.request_url:
            error_parts.append(f"URL: {self.request_url}")

        if self.request_method:
            error_parts.append(f"Method: {self.request_method}")

        if self.request_params:
            error_parts.append(f"Parameters: {self.request_params}")

        return " | ".join(error_parts)


@dataclass(slots=True, frozen=True)
class TokenError(BlizzardAPIError):
    """Exception raised for token-related errors.

    This exception is raised when there are issues with OAuth token management,
    such as token retrieval, validation, or expiration.
    """

    token_type: Optional[str] = None
    region: Optional[RegionType] = None

    def __str__(self) -> str:
        """Return a string representation of the token error."""
        error_parts = [f"Token Error: {self.message}"]

        if self.token_type:
            error_parts.append(f"Token Type: {self.token_type}")

        if self.region:
            error_parts.append(f"Region: {self.region}")

        if self.status_code:
            error_parts.append(f"Status Code: {self.status_code}")

        return " | ".join(error_parts)


@dataclass(slots=True, frozen=True)
class RequestError(BlizzardAPIError):
    """Exception raised for request-related errors.

    This exception is raised when there are issues with API requests,
    such as network errors, invalid responses, or rate limiting.
    """

    retry_after: Optional[int] = None
    error_code: Optional[str] = None
    error_details: Optional[Dict[str, Any]] = None

    def __str__(self) -> str:
        """Return a string representation of the request error."""
        error_parts = [f"Request Error: {self.message}"]

        if self.error_code:
            error_parts.append(f"Error Code: {self.error_code}")

        if self.retry_after:
            error_parts.append(f"Retry After: {self.retry_after} seconds")

        if self.status_code:
            error_parts.append(f"Status Code: {self.status_code}")

        if self.request_url:
            error_parts.append(f"URL: {self.request_url}")

        return " | ".join(error_parts)

    @property
    def is_rate_limited(self) -> bool:
        """Check if the error is due to rate limiting."""
        return self.status_code == 429 or self.retry_after is not None

    @property
    def should_retry(self) -> bool:
        """Check if the request should be retried."""
        return self.is_rate_limited or self.status_code in (500, 502, 503, 504)


class Api:
    """Base API class for interacting with Blizzard's APIs.

    This class handles authentication, request formatting, and response handling
    for all Blizzard API endpoints. It supports both synchronous and asynchronous
    operations.

    Attributes:
        _client_id: The Blizzard API client ID.
        _client_secret: The Blizzard API client secret.
        _access_token: The current OAuth access token.
        _token_expiry: When the current token expires.
        _session: The requests session for making HTTP requests.
        _async_session: The aiohttp session for making async HTTP requests.
    """

    # Base URLs for different regions
    API_URLS: Final[Dict[str, str]] = {
        Region.CN: "https://gateway.battlenet.com.cn{0}",
        "default": "https://{0}.api.blizzard.com{1}",
    }
    OAUTH_URLS: Final[Dict[str, str]] = {
        Region.CN: "https://www.gateway.battlenet.com.cn{0}",
        "default": "https://oauth.battle.net{1}",
    }

    def __init__(self, client_id: str, client_secret: str) -> None:
        """Initialize the API client.

        Args:
            client_id: The Blizzard API client ID.
            client_secret: The Blizzard API client secret.
        """
        self._client_id = client_id
        self._client_secret = client_secret
        self._access_token: Optional[str] = None
        self._token_expiry: Optional[datetime] = None
        self._session = requests.Session()
        self._async_session: Optional[aiohttp.ClientSession] = None

    async def __aenter__(self) -> Self:
        """Async context manager entry.

        Returns:
            Self: The API instance.
        """
        if self._async_session is None:
            self._async_session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        """Async context manager exit.

        Args:
            exc_type: The exception type if any.
            exc_val: The exception value if any.
            exc_tb: The exception traceback if any.
        """
        if self._async_session is not None:
            await self._async_session.close()
            self._async_session = None

    def _get_base_url(self, region: Region, is_oauth: bool = False) -> str:
        """Get the base URL for the given region.

        Args:
            region: The region to get the URL for.
            is_oauth: Whether to get the OAuth URL.

        Returns:
            str: The base URL for the region.
        """
        urls = self.OAUTH_URLS if is_oauth else self.API_URLS
        return urls.get(region, urls["default"])

    def _format_url(self, resource: str, region: Region, is_oauth: bool = False) -> str:
        """Format a URL for the given resource and region.

        Args:
            resource: The API resource path.
            region: The region to format the URL for.
            is_oauth: Whether this is an OAuth URL.

        Returns:
            str: The formatted URL.
        """
        base_url = self._get_base_url(region, is_oauth)
        if region == Region.CN:
            return base_url.format(resource)
        return base_url.format(region, resource)

    def _is_token_expired(self) -> bool:
        """Check if the current token is expired or will expire soon.

        Returns:
            bool: True if the token is expired or will expire within 5 minutes.
        """
        if not self._token_expiry:
            return True
        return datetime.now(UTC) >= self._token_expiry - timedelta(minutes=5)

    def _get_client_token(self, region: Region) -> TokenResponse:
        """Get a new OAuth token.

        Args:
            region: The region to get the token for.

        Returns:
            TokenResponse: The token response.

        Raises:
            TokenError: If token retrieval fails.
        """
        url = self._format_url("/oauth/token", region, is_oauth=True)
        try:
            response = self._session.post(
                url,
                params={"grant_type": "client_credentials"},
                auth=(self._client_id, self._client_secret),
            )
            response.raise_for_status()
            data = response.json()

            self._access_token = data["access_token"]
            self._token_expiry = datetime.now(UTC) + timedelta(
                seconds=data["expires_in"]
            )

            return data
        except requests.RequestException as e:
            raise TokenError(
                message=f"Failed to get token: {str(e)}",
                token_type="access_token",
                region=region,
                status_code=getattr(e.response, "status_code", None),
                response=e.response,
                request_url=url,
                request_method="POST",
                request_params={"grant_type": "client_credentials"},
            ) from e

    async def _get_client_token_async(self, region: Region) -> TokenResponse:
        """Get a new OAuth token asynchronously.

        Args:
            region: The region to get the token for.

        Returns:
            TokenResponse: The token response.

        Raises:
            TokenError: If token retrieval fails.
        """
        if self._async_session is None:
            self._async_session = aiohttp.ClientSession()

        url = self._format_url("/oauth/token", region, is_oauth=True)
        try:
            async with self._async_session.post(
                url,
                params={"grant_type": "client_credentials"},
                auth=aiohttp.BasicAuth(self._client_id, self._client_secret),
            ) as response:
                response.raise_for_status()
                data = await response.json()

                self._access_token = data["access_token"]
                self._token_expiry = datetime.now(UTC) + timedelta(
                    seconds=data["expires_in"]
                )

                return data
        except aiohttp.ClientError as e:
            status_code = getattr(e, "status", None)
            raise TokenError(
                message=f"Failed to get token: {str(e)}",
                token_type="access_token",
                region=region,
                status_code=status_code,
                request_url=url,
                request_method="POST",
                request_params={"grant_type": "client_credentials"},
            ) from e

    def _ensure_valid_token(self, region: Region) -> None:
        """Ensure we have a valid token, getting a new one if needed.

        Args:
            region: The region to get the token for.

        Raises:
            TokenError: If token retrieval fails.
        """
        if self._is_token_expired():
            self._get_client_token(region)

    async def _ensure_valid_token_async(self, region: Region) -> None:
        """Ensure we have a valid token asynchronously.

        Args:
            region: The region to get the token for.

        Raises:
            TokenError: If token retrieval fails.
        """
        if self._is_token_expired():
            await self._get_client_token_async(region)

    def _make_request(
        self,
        method: str,
        resource: str,
        region: Region,
        is_oauth: bool = False,
        **kwargs: Any,
    ) -> Dict[str, Any]:
        """Make an API request.

        Args:
            method: The HTTP method to use.
            resource: The API resource path.
            region: The region to make the request to.
            is_oauth: Whether this is an OAuth request.
            **kwargs: Additional arguments to pass to the request.

        Returns:
            Dict[str, Any]: The JSON response.

        Raises:
            RequestError: If the request fails.
        """
        url = self._format_url(resource, region, is_oauth)

        if not is_oauth:
            self._ensure_valid_token(region)
            headers = kwargs.pop("headers", {})
            headers["Authorization"] = f"Bearer {self._access_token}"
            kwargs["headers"] = headers

        try:
            response = self._session.request(method, url, **kwargs)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            error_details = None
            retry_after = None
            error_code = None

            if hasattr(e, "response") and e.response is not None:
                try:
                    error_data = e.response.json()
                    error_details = error_data
                    error_code = error_data.get("code")
                except ValueError:
                    pass

                retry_after = e.response.headers.get("Retry-After")

            raise RequestError(
                message=f"Request failed: {str(e)}",
                status_code=getattr(e.response, "status_code", None),
                response=e.response,
                request_url=url,
                request_method=method,
                request_params=kwargs.get("params"),
                retry_after=retry_after,
                error_code=error_code,
                error_details=error_details,
            ) from e

    async def _make_request_async(
        self,
        method: str,
        resource: str,
        region: Region,
        is_oauth: bool = False,
        **kwargs: Any,
    ) -> Dict[str, Any]:
        """Make an API request asynchronously.

        Args:
            method: The HTTP method to use.
            resource: The API resource path.
            region: The region to make the request to.
            is_oauth: Whether this is an OAuth request.
            **kwargs: Additional arguments to pass to the request.

        Returns:
            Dict[str, Any]: The JSON response.

        Raises:
            RequestError: If the request fails.
        """
        if self._async_session is None:
            self._async_session = aiohttp.ClientSession()

        url = self._format_url(resource, region, is_oauth)

        if not is_oauth:
            await self._ensure_valid_token_async(region)
            headers = kwargs.pop("headers", {})
            headers["Authorization"] = f"Bearer {self._access_token}"
            kwargs["headers"] = headers

        try:
            async with self._async_session.request(method, url, **kwargs) as response:
                response.raise_for_status()
                return await response.json()
        except aiohttp.ClientError as e:
            error_details = None
            retry_after = None
            error_code = None

            if hasattr(e, "response") and e.response is not None:
                try:
                    error_data = await e.response.json()
                    error_details = error_data
                    error_code = error_data.get("code")
                except (ValueError, aiohttp.ContentTypeError):
                    pass

                retry_after = e.response.headers.get("Retry-After")

            raise RequestError(
                message=f"Request failed: {str(e)}",
                status_code=getattr(e, "status", None),
                request_url=url,
                request_method=method,
                request_params=kwargs.get("params"),
                retry_after=retry_after,
                error_code=error_code,
                error_details=error_details,
            ) from e

    def get_resource(
        self, resource: str, region: Region, query_params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Get a resource from the API.

        Args:
            resource: The API resource path.
            region: The region to get the resource from.
            query_params: Optional query parameters.

        Returns:
            Dict[str, Any]: The JSON response.
        """
        return self._make_request("GET", resource, region, params=query_params)

    async def get_resource_async(
        self, resource: str, region: Region, query_params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Get a resource from the API asynchronously.

        Args:
            resource: The API resource path.
            region: The region to get the resource from.
            query_params: Optional query parameters.

        Returns:
            Dict[str, Any]: The JSON response.
        """
        return await self._make_request_async(
            "GET", resource, region, params=query_params
        )

    def get_oauth_resource(
        self, resource: str, region: Region, query_params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Get a resource from the OAuth API.

        Args:
            resource: The OAuth resource path.
            region: The region to get the resource from.
            query_params: Optional query parameters.

        Returns:
            Dict[str, Any]: The JSON response.
        """
        return self._make_request(
            "GET", resource, region, is_oauth=True, params=query_params
        )

    async def get_oauth_resource_async(
        self, resource: str, region: Region, query_params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Get a resource from the OAuth API asynchronously.

        Args:
            resource: The OAuth resource path.
            region: The region to get the resource from.
            query_params: Optional query parameters.

        Returns:
            Dict[str, Any]: The JSON response.
        """
        return await self._make_request_async(
            "GET", resource, region, is_oauth=True, params=query_params
        )
