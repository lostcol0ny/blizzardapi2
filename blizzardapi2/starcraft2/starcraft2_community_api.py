"""StarCraft II Community API client.

This module provides access to StarCraft II community endpoints,
including profiles, ladders, and other player-related information.
"""

from typing import Any

from ..api import Api, Locale, Region


class Starcraft2CommunityApi(Api):
    """StarCraft II Community API client.

    This class provides access to StarCraft II community data through the Blizzard API,
    including player profiles, ladder information, and other community-related endpoints.

    Example:
        ```python
        # Synchronous usage
        api = Starcraft2CommunityApi(client_id="your_id", client_secret="your_secret")
        profile = api.get_profile("us", "en_US", 1, 1, 12345)
        ladder = api.get_ladder_summary("us", "en_US", 1, 1, 12345)

        # Asynchronous usage
        async with Starcraft2CommunityApi(client_id="your_id", client_secret="your_secret") as api:
            profile = await api.get_profile("us", "en_US", 1, 1, 12345)
            ladder = await api.get_ladder_summary("us", "en_US", 1, 1, 12345)
        ```

    Attributes:
        client_id: The Blizzard API client ID.
        client_secret: The Blizzard API client secret.
    """

    def __init__(self, client_id: str, client_secret: str) -> None:
        """Initialize the StarCraft II Community API client.

        Args:
            client_id: The Blizzard API client ID.
            client_secret: The Blizzard API client secret.

        Raises:
            ValueError: If client_id or client_secret is empty.
        """
        if not client_id or not client_secret:
            raise ValueError("client_id and client_secret must not be empty")
        super().__init__(client_id, client_secret)

    def get_static(self, region: Region, locale: Locale, region_id: int) -> dict[str, Any]:
        """Get all static SC2 profile data.

        This includes achievements, categories, criteria, and rewards.

        Args:
            region: The region to query (e.g., "us", "eu").
            locale: The locale to use for the response (e.g., "en_US").
            region_id: The ID of the region.

        Returns:
            A dictionary containing the static profile data.

        Raises:
            ApiError: If the API request fails.
        """
        resource = f"/sc2/static/profile/{region_id}"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_metadata(
        self, region: Region, locale: Locale, region_id: int, realm_id: int, profile_id: int
    ) -> dict[str, Any]:
        """Get metadata for an individual's profile.

        Args:
            region: The region to query (e.g., "us", "eu").
            locale: The locale to use for the response (e.g., "en_US").
            region_id: The ID of the region.
            realm_id: The ID of the realm.
            profile_id: The ID of the profile.

        Returns:
            A dictionary containing the profile metadata.

        Raises:
            ApiError: If the API request fails.
        """
        resource = f"/sc2/metadata/profile/{region_id}/{realm_id}/{profile_id}"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_profile(
        self,
        region: str,
        locale: str,
        region_id: int,
        realm_id: int,
        profile_id: int,
        **query_params: Any,
    ) -> dict[str, Any]:
        """Get data about an individual SC2 profile.

        Args:
            region: The region to query (e.g., "us", "eu").
            locale: The locale to use for the response (e.g., "en_US").
            region_id: The ID of the region.
            realm_id: The ID of the realm.
            profile_id: The ID of the profile.
            **query_params: Additional query parameters.

        Returns:
            A dictionary containing the profile data.

        Raises:
            ApiError: If the API request fails.
        """
        resource = f"/sc2/profile/{region_id}/{realm_id}/{profile_id}"
        query_params["locale"] = locale
        return super().get_resource(resource, region, query_params)

    def get_ladder_summary(
        self, region: Region, locale: Locale, region_id: int, realm_id: int, profile_id: int
    ) -> dict[str, Any]:
        """Get a ladder summary for an individual SC2 profile.

        Args:
            region: The region to query (e.g., "us", "eu").
            locale: The locale to use for the response (e.g., "en_US").
            region_id: The ID of the region.
            realm_id: The ID of the realm.
            profile_id: The ID of the profile.

        Returns:
            A dictionary containing the ladder summary.

        Raises:
            ApiError: If the API request fails.
        """
        resource = f"/sc2/profile/{region_id}/{realm_id}/{profile_id}/ladder/summary"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_ladder(
        self,
        region: str,
        locale: str,
        region_id: int,
        realm_id: int,
        profile_id: int,
        ladder_id: int,
        **query_params: Any,
    ) -> dict[str, Any]:
        """Get data about an individual profile's ladder.

        Args:
            region: The region to query (e.g., "us", "eu").
            locale: The locale to use for the response (e.g., "en_US").
            region_id: The ID of the region.
            realm_id: The ID of the realm.
            profile_id: The ID of the profile.
            ladder_id: The ID of the ladder.
            **query_params: Additional query parameters.

        Returns:
            A dictionary containing the ladder data.

        Raises:
            ApiError: If the API request fails.
        """
        resource = f"/sc2/profile/{region_id}/{realm_id}/{profile_id}/ladder/{ladder_id}"
        query_params["locale"] = locale
        return super().get_resource(resource, region, query_params)

    def get_grandmaster_leaderboard(
        self, region: Region, locale: Locale, region_id: int
    ) -> dict[str, Any]:
        """Get ladder data for the current season's grandmaster leaderboard.

        Args:
            region: The region to query (e.g., "us", "eu").
            locale: The locale to use for the response (e.g., "en_US").
            region_id: The ID of the region.

        Returns:
            A dictionary containing the grandmaster leaderboard data.

        Raises:
            ApiError: If the API request fails.
        """
        resource = f"/sc2/ladder/grandmaster{region_id}"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_season(self, region: Region, locale: Locale, region_id: int) -> dict[str, Any]:
        """Get data about the current season.

        Args:
            region: The region to query (e.g., "us", "eu").
            locale: The locale to use for the response (e.g., "en_US").
            region_id: The ID of the region.

        Returns:
            A dictionary containing the season data.

        Raises:
            ApiError: If the API request fails.
        """
        resource = f"/sc2/ladder/season/{region_id}"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_player(self, region: Region, locale: Locale, account_id: int) -> dict[str, Any]:
        """Get metadata for an individual's account.

        Args:
            region: The region to query (e.g., "us", "eu").
            locale: The locale to use for the response (e.g., "en_US").
            account_id: The ID of the account.

        Returns:
            A dictionary containing the account metadata.

        Raises:
            ApiError: If the API request fails.
        """
        resource = f"/sc2/player/{account_id}"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)
