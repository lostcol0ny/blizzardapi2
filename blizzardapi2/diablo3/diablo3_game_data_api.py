"""Diablo III Game Data API client.

This module provides access to Diablo III game data endpoints,
including seasons, eras, and leaderboards.
"""

from typing import Any, Dict

from ..api import BaseApi, Locale, Region


class ApiResponse:
    """Wrapper for API responses with metadata."""

    data: Dict[str, Any]
    region: Region
    locale: Locale
    namespace: str


class Diablo3GameDataApi(BaseApi):
    """Diablo III Game Data API client.

    This class provides access to the Diablo III Game Data API endpoints.
    It handles authentication and request formatting for all game data related
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

    def get_season_index(self, region: Region) -> dict[str, Any]:
        """Get an index of available seasons.

        Args:
            region: The region to query (e.g., "us", "eu").

        Returns:
            A dictionary containing the index of seasons.

        Raises:
            ApiError: If the API request fails.
        """
        resource = "/data/d3/season/"
        return self.get_resource(resource, region)

    def get_season(self, region: Region, season_id: int) -> dict[str, Any]:
        """Get a leaderboard list for the specified season.

        Args:
            region: The region to query (e.g., "us", "eu").
            season_id: The ID of the season to retrieve.

        Returns:
            A dictionary containing the leaderboard list for the season.

        Raises:
            ApiError: If the API request fails.
        """
        resource = f"/data/d3/season/{season_id}"
        return self.get_resource(resource, region)

    def get_season_leaderboard(
        self, region: Region, season_id: int, leaderboard_id: int
    ) -> dict[str, Any]:
        """Get the specified leaderboard for the specified season.

        Args:
            region: The region to query (e.g., "us", "eu").
            season_id: The ID of the season.
            leaderboard_id: The ID of the leaderboard to retrieve.

        Returns:
            A dictionary containing the leaderboard details.

        Raises:
            ApiError: If the API request fails.
        """
        resource = f"/data/d3/season/{season_id}/leaderboard/{leaderboard_id}"
        return self.get_resource(resource, region)

    def get_era_index(self, region: Region) -> dict[str, Any]:
        """Get an index of available eras.

        Args:
            region: The region to query (e.g., "us", "eu").

        Returns:
            A dictionary containing the index of eras.

        Raises:
            ApiError: If the API request fails.
        """
        resource = "/data/d3/era/"
        return self.get_resource(resource, region)

    def get_era(self, region: Region, era_id: int) -> dict[str, Any]:
        """Get a leaderboard list for a particular era.

        Args:
            region: The region to query (e.g., "us", "eu").
            era_id: The ID of the era to retrieve.

        Returns:
            A dictionary containing the leaderboard list for the era.

        Raises:
            ApiError: If the API request fails.
        """
        resource = f"/data/d3/era/{era_id}"
        return self.get_resource(resource, region)

    def get_era_leaderboard(
        self, region: Region, era_id: int, leaderboard_id: int
    ) -> dict[str, Any]:
        """Get the specified leaderboard for the specified era.

        Args:
            region: The region to query (e.g., "us", "eu").
            era_id: The ID of the era.
            leaderboard_id: The ID of the leaderboard to retrieve.

        Returns:
            A dictionary containing the leaderboard details.

        Raises:
            ApiError: If the API request fails.
        """
        resource = f"/data/d3/era/{era_id}/leaderboard/{leaderboard_id}"
        return self.get_resource(resource, region)
