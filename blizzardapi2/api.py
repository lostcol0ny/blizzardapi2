"""api.py file."""

from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, Literal, Optional, Protocol, TypedDict

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


@dataclass(slots=True)
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

    def __init__(self, message: str, **kwargs: Any) -> None:
        """Initialize the error with the message and additional context.

        Args:
            message: The error message.
            **kwargs: Additional error context.
        """
        super().__init__(message)
        self.message = message
        for key, value in kwargs.items():
            setattr(self, key, value)

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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


class BaseApi:
    """Base API class."""

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        region: str = "us",
        locale: str = "en_US",
    ):
        """Initialize the API client.

        Args:
            client_id: The client ID.
            client_secret: The client secret.
            region: The region to use.
            locale: The locale to use.
        """
        self._client_id = client_id
        self._client_secret = client_secret
        self._region = region
        self._locale = locale
        self._session = requests.Session()
        self._async_session: Optional[aiohttp.ClientSession] = None
        self._token: Optional[str] = None
        self._token_type: Optional[str] = None
        self._token_expires_in: Optional[int] = None
        self._token_created_at: Optional[float] = None

    def __del__(self):
        """Clean up resources."""
        try:
            if hasattr(self, "_session"):
                self._session.close()
            if hasattr(self, "_async_session") and self._async_session is not None:
                if not self._async_session.closed:
                    self._async_session.close()
        except Exception:
            pass  # Ignore cleanup errors during garbage collection

    async def __aenter__(self) -> "BaseApi":
        """Async context manager entry."""
        if self._async_session is None:
            self._async_session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        """Async context manager exit."""
        if self._async_session is not None and not self._async_session.closed:
            await self._async_session.close()
            self._async_session = None

    def _get_token(self) -> str:
        """Get the OAuth token.

        Returns:
            The OAuth token.

        Raises:
            TokenError: If the token request fails.
        """
        if self._token is None or self._is_token_expired():
            response = self._session.post(
                f"https://{self._region}.battle.net/oauth/token",
                auth=(self._client_id, self._client_secret),
                data={"grant_type": "client_credentials"},
            )
            if response.status_code != 200:
                raise TokenError(
                    f"Failed to get token: {response.status_code} {response.reason}",
                    response=response,
                )
            data = response.json()
            self._token = data["access_token"]
            self._token_type = data["token_type"]
            self._token_expires_in = data["expires_in"]
            self._token_created_at = response.elapsed.total_seconds()
        return self._token

    async def _get_token_async(self) -> str:
        """Get the OAuth token asynchronously.

        Returns:
            The OAuth token.

        Raises:
            TokenError: If the token request fails.
        """
        if self._token is None or self._is_token_expired():
            if self._async_session is None:
                self._async_session = aiohttp.ClientSession()
            response = await self._async_session.post(
                f"https://{self._region}.battle.net/oauth/token",
                auth=aiohttp.BasicAuth(self._client_id, self._client_secret),
                data={"grant_type": "client_credentials"},
            )
            if response.status != 200:
                raise TokenError(
                    f"Failed to get token: {response.status} {response.reason}",
                    response=response,
                )
            data = await response.json()
            self._token = data["access_token"]
            self._token_type = data["token_type"]
            self._token_expires_in = data["expires_in"]
            self._token_created_at = response.elapsed.total_seconds()
            await response.release()
        return self._token

    def _is_token_expired(self) -> bool:
        """Check if the token is expired.

        Returns:
            True if the token is expired, False otherwise.
        """
        if self._token_expires_in is None or self._token_created_at is None:
            return True
        return (
            self._token_created_at + self._token_expires_in
            < requests.get("https://www.google.com").elapsed.total_seconds()
        )

    def _make_request(
        self,
        region: str,
        endpoint: str,
        **query_params: Any,
    ) -> dict[str, Any]:
        """Make a request to the API.

        Args:
            region: The region to get data from.
            endpoint: The API endpoint.
            **query_params: Additional query parameters.

        Returns:
            The API response.

        Raises:
            TokenError: If the token request fails.
        """
        token = self._get_token()
        response = self._session.get(
            f"https://{region}.api.blizzard.com/{endpoint}",
            params={"locale": self._locale, "access_token": token, **query_params},
        )
        if response.status_code != 200:
            raise TokenError(
                f"Failed to get data: {response.status_code} {response.reason}",
                response=response,
            )
        return response.json()

    async def _make_request_async(
        self,
        region: str,
        endpoint: str,
        **query_params: Any,
    ) -> dict[str, Any]:
        """Make a request to the API asynchronously.

        Args:
            region: The region to get data from.
            endpoint: The API endpoint.
            **query_params: Additional query parameters.

        Returns:
            The API response.

        Raises:
            TokenError: If the token request fails.
        """
        token = await self._get_token_async()
        if self._async_session is None:
            self._async_session = aiohttp.ClientSession()
        response = await self._async_session.get(
            f"https://{region}.api.blizzard.com/{endpoint}",
            params={"locale": self._locale, "access_token": token, **query_params},
        )
        if response.status != 200:
            raise TokenError(
                f"Failed to get data: {response.status} {response.reason}",
                response=response,
            )
        data = await response.json()
        await response.release()
        return data

    def get_resource(
        self,
        resource: str,
        region: str,
        query_params: Optional[dict[str, Any]] = None,
    ) -> dict[str, Any]:
        """Get a resource from the API.

        Args:
            resource: The resource to get.
            region: The region to get the resource from.
            query_params: Additional query parameters.

        Returns:
            The API response.
        """
        return self._make_request(region, resource, **(query_params or {}))

    async def get_resource_async(
        self,
        resource: str,
        region: str,
        query_params: Optional[dict[str, Any]] = None,
    ) -> dict[str, Any]:
        """Get a resource from the API asynchronously.

        Args:
            resource: The resource to get.
            region: The region to get the resource from.
            query_params: Additional query parameters.

        Returns:
            The API response.
        """
        return await self._make_request_async(region, resource, **(query_params or {}))

    def get_oauth_resource(
        self,
        resource: str,
        region: str,
        query_params: Optional[dict[str, Any]] = None,
    ) -> dict[str, Any]:
        """Get an OAuth resource from the API.

        Args:
            resource: The resource to get.
            region: The region to get the resource from.
            query_params: Additional query parameters.

        Returns:
            The API response.
        """
        return self._make_request(region, resource, **(query_params or {}))

    async def get_oauth_resource_async(
        self,
        resource: str,
        region: str,
        query_params: Optional[dict[str, Any]] = None,
    ) -> dict[str, Any]:
        """Get an OAuth resource from the API asynchronously.

        Args:
            resource: The resource to get.
            region: The region to get the resource from.
            query_params: Additional query parameters.

        Returns:
            The API response.
        """
        return await self._make_request_async(region, resource, **(query_params or {}))
