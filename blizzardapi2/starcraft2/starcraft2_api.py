"""StarCraft II API client.

This module provides access to the StarCraft II API endpoints,
including game data and community information.
"""

from typing import Any, Dict


from ..api import BaseApi
from ..types import Locale, Region
from .starcraft2_community_api import Starcraft2CommunityApi
from .starcraft2_game_data_api import Starcraft2GameDataApi


class Starcraft2Api(BaseApi):
    """StarCraft II API client.

    This class provides access to the StarCraft II API endpoints.
    """

    def __init__(self, client_id: str, client_secret: str) -> None:
        """Initialize the StarCraft II API client.

        Args:
            client_id: The Blizzard API client ID.
            client_secret: The Blizzard API client secret.
        """
        super().__init__(client_id, client_secret)
        self.community = Starcraft2CommunityApi(client_id, client_secret)
        self.game_data = Starcraft2GameDataApi(client_id, client_secret)

    def get_league_data(
        self, region: Region, locale: Locale, season_id: int, queue_id: int, team_type: int
    ) -> Dict[str, Any]:
        """Get league data for a specific season, queue, and team type.

        Args:
            region: The region to query (e.g., "us", "eu").
            locale: The locale to use for the response (e.g., "en_US").
            season_id: The ID of the season.
            queue_id: The ID of the queue.
            team_type: The type of team.

        Returns:
            A dictionary containing the league data.

        Raises:
            ApiError: If the API request fails.
        """
        resource = f"/data/sc2/league/{season_id}/{queue_id}/{team_type}"
        query_params = {"locale": locale}
        return self.get_resource(resource, region, query_params)

    def get_season(self, region: Region, locale: Locale) -> Dict[str, Any]:
        """Get the current season.

        Args:
            region: The region to query (e.g., "us", "eu").
            locale: The locale to use for the response (e.g., "en_US").

        Returns:
            A dictionary containing the current season information.

        Raises:
            ApiError: If the API request fails.
        """
        resource = "/data/sc2/season/current"
        query_params = {"locale": locale}
        return self.get_resource(resource, region, query_params)

    def get_player_ladder_summary(
        self, region: Region, locale: Locale, profile_id: int, realm_id: int
    ) -> Dict[str, Any]:
        """Get a player's ladder summary.

        Args:
            region: The region to query (e.g., "us", "eu").
            locale: The locale to use for the response (e.g., "en_US").
            profile_id: The ID of the player's profile.
            realm_id: The ID of the player's realm.

        Returns:
            A dictionary containing the player's ladder summary.

        Raises:
            ApiError: If the API request fails.
        """
        resource = f"/data/sc2/player/{profile_id}/{realm_id}/ladder/summary"
        query_params = {"locale": locale}
        return self.get_resource(resource, region, query_params)

    def get_player_ladder(
        self, region: Region, locale: Locale, profile_id: int, realm_id: int, ladder_id: int
    ) -> Dict[str, Any]:
        """Get a player's ladder information.

        Args:
            region: The region to query (e.g., "us", "eu").
            locale: The locale to use for the response (e.g., "en_US").
            profile_id: The ID of the player's profile.
            realm_id: The ID of the player's realm.
            ladder_id: The ID of the ladder.

        Returns:
            A dictionary containing the player's ladder information.

        Raises:
            ApiError: If the API request fails.
        """
        resource = f"/data/sc2/player/{profile_id}/{realm_id}/ladder/{ladder_id}"
        query_params = {"locale": locale}
        return self.get_resource(resource, region, query_params)

    def get_player_profile(
        self, region: Region, locale: Locale, profile_id: int, realm_id: int
    ) -> Dict[str, Any]:
        """Get a player's profile information.

        Args:
            region: The region to query (e.g., "us", "eu").
            locale: The locale to use for the response (e.g., "en_US").
            profile_id: The ID of the player's profile.
            realm_id: The ID of the player's realm.

        Returns:
            A dictionary containing the player's profile information.

        Raises:
            ApiError: If the API request fails.
        """
        resource = f"/data/sc2/player/{profile_id}/{realm_id}"
        query_params = {"locale": locale}
        return self.get_resource(resource, region, query_params)

    def get_player_ladder_history(
        self, region: Region, locale: Locale, profile_id: int, realm_id: int
    ) -> Dict[str, Any]:
        """Get a player's ladder history.

        Args:
            region: The region to query (e.g., "us", "eu").
            locale: The locale to use for the response (e.g., "en_US").
            profile_id: The ID of the player's profile.
            realm_id: The ID of the player's realm.

        Returns:
            A dictionary containing the player's ladder history.

        Raises:
            ApiError: If the API request fails.
        """
        resource = f"/data/sc2/player/{profile_id}/{realm_id}/ladder/history"
        query_params = {"locale": locale}
        return self.get_resource(resource, region, query_params)

    def get_player_achievements(
        self, region: Region, locale: Locale, profile_id: int, realm_id: int
    ) -> Dict[str, Any]:
        """Get a player's achievements.

        Args:
            region: The region to query (e.g., "us", "eu").
            locale: The locale to use for the response (e.g., "en_US").
            profile_id: The ID of the player's profile.
            realm_id: The ID of the player's realm.

        Returns:
            A dictionary containing the player's achievements.

        Raises:
            ApiError: If the API request fails.
        """
        resource = f"/data/sc2/player/{profile_id}/{realm_id}/achievements"
        query_params = {"locale": locale}
        return self.get_resource(resource, region, query_params)

    def get_player_rewards(
        self, region: Region, locale: Locale, profile_id: int, realm_id: int
    ) -> Dict[str, Any]:
        """Get a player's rewards.

        Args:
            region: The region to query (e.g., "us", "eu").
            locale: The locale to use for the response (e.g., "en_US").
            profile_id: The ID of the player's profile.
            realm_id: The ID of the player's realm.

        Returns:
            A dictionary containing the player's rewards.

        Raises:
            ApiError: If the API request fails.
        """
        resource = f"/data/sc2/player/{profile_id}/{realm_id}/rewards"
        query_params = {"locale": locale}
        return self.get_resource(resource, region, query_params)
