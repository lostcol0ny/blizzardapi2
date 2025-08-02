"""api.py file."""

from datetime import UTC, datetime, timedelta
from typing import Any

import requests


class BaseApi:
    """Base API class.

    Attributes:
        _client_id: A string client id supplied by Blizzard.
        _client_secret: A string client secret supplied by Blizzard.
        _access_token: A string access token that is used to access Blizzard's API.
        _api_url: A string url used to call the API endpoints.
        _api_url_cn: A string url used to call the china API endpoints.
        _oauth_url: A string url used to call the OAuth API endpoints.
        _oauth_url_cn: A string url used to call the china OAuth API endpoints.
        _session: An open requests.Session instance.
    """

    def __init__(self, client_id: str, client_secret: str) -> None:
        """Init Api."""
        self._client_id: str = client_id
        self._client_secret: str = client_secret
        self._access_token: str = None
        self._access_token_expiration_datetime: str = "2024-08-06T12:38:15.125Z"

        self._api_url = "https://{0}.api.blizzard.com{1}"
        self._api_url_cn = "https://gateway.battlenet.com.cn{0}"

        self._oauth_url = "https://oauth.battle.net{1}"
        self._oauth_url_cn = "https://www.gateway.battlenet.com.cn{0}"

        self._session = requests.Session()

    def _is_token_expired(self) -> bool:
        """Check if the token is expiring within next 5 minutes."""
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

    def _request_handler(
        self, url: str, region: str, query_params: dict[str, Any] = None
    ) -> dict[str, Any]:
        """Handle the request."""
        self._ensure_valid_token(region)

        headers = {"Authorization": f"Bearer {self._access_token}"}

        # Initialize query_params if it's None
        if query_params is None:
            query_params = {}
        else:
            # Create a copy of query_params to avoid modifying the original
            query_params = query_params.copy()

        # Remove access_token from query_params if it exists
        query_params.pop("access_token", None)

        response = self._session.get(url, params=query_params, headers=headers)

        self._access_token_expiration_datetime = response.headers.get(
            "blizzard-token-expires"
        )

        if response.status_code == 401 or self._is_token_expired():
            self._get_client_token(region)
            headers["Authorization"] = f"Bearer {self._access_token}"
            response = self._session.get(url, params=query_params, headers=headers)

        return self._response_handler(response)

    def _format_api_url(self, resource: str, region: str) -> str:
        """Format the API url into a usable url."""
        if region == "cn":
            url = self._api_url_cn.format(resource)
        else:
            url = self._api_url.format(region, resource)

        return url

    def get_resource(
        self, resource: str, region: str, query_params={}
    ) -> dict[str, Any]:
        """Direction handler for when fetching resources."""
        url = self._format_api_url(resource, region)
        return self._request_handler(url, region, query_params)

    def _format_oauth_url(self, resource: str, region: str) -> str:
        """Format the oauth url into a usable url."""
        if region == "cn":
            url = self._oauth_url_cn.format(resource)
        else:
            url = self._oauth_url.format(region, resource)

        return url

    def get_oauth_resource(
        self, resource: str, region: str, query_params={}
    ) -> dict[str, Any]:
        """Direction handler for when fetching oauth resources."""
        url = self._format_oauth_url(resource, region)
        return self._request_handler(url, region, query_params)
