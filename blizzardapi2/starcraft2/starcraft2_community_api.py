"""starcraft2_community_api.py file."""

from typing import Any

from ..api import BaseApi


class Starcraft2CommunityApi(BaseApi):
    """All Starcraft 2 Community API methods.

    Attributes:
        client_id (str): A string client ID supplied by Blizzard.
        client_secret (str): A string client secret supplied by Blizzard.
    """

    def __init__(self, client_id: str, client_secret: str) -> None:
        """
        Initialize the Starcraft2CommunityApi class.

        Args:
            client_id (str): The client ID supplied by Blizzard.
            client_secret (str): The client secret supplied by Blizzard.
        """
        super().__init__(client_id, client_secret)

    def get_static(self, region: str, locale: str, region_id: int) -> dict[str, Any]:
        """
        Return all static SC2 profile data (achievements, categories, criteria, and rewards).

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            region_id (int): The ID of the region.

        Returns:
            Dict[str, Any]: A dictionary containing the static profile data.
        """
        resource = f"/sc2/static/profile/{region_id}"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_metadata(
        self, region: str, locale: str, region_id: int, realm_id: int, profile_id: int
    ) -> dict[str, Any]:
        """
        Return metadata for an individual's profile.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            region_id (int): The ID of the region.
            realm_id (int): The ID of the realm.
            profile_id (int): The ID of the profile.

        Returns:
            Dict[str, Any]: A dictionary containing the profile metadata.
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
        """
        Return data about an individual SC2 profile.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            region_id (int): The ID of the region.
            realm_id (int): The ID of the realm.
            profile_id (int): The ID of the profile.
            **query_params (Any): Additional query parameters.

        Returns:
            Dict[str, Any]: A dictionary containing the profile data.
        """
        resource = f"/sc2/profile/{region_id}/{realm_id}/{profile_id}"
        query_params["locale"] = locale
        return super().get_resource(resource, region, query_params)

    def get_ladder_summary(
        self, region: str, locale: str, region_id: int, realm_id: int, profile_id: int
    ) -> dict[str, Any]:
        """
        Return a ladder summary for an individual SC2 profile.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            region_id (int): The ID of the region.
            realm_id (int): The ID of the realm.
            profile_id (int): The ID of the profile.

        Returns:
            Dict[str, Any]: A dictionary containing the ladder summary.
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
        """
        Return data about an individual profile's ladder.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            region_id (int): The ID of the region.
            realm_id (int): The ID of the realm.
            profile_id (int): The ID of the profile.
            ladder_id (int): The ID of the ladder.
            **query_params (Any): Additional query parameters.

        Returns:
            Dict[str, Any]: A dictionary containing the ladder data.
        """
        resource = (
            f"/sc2/profile/{region_id}/{realm_id}/{profile_id}/ladder/{ladder_id}"
        )
        query_params["locale"] = locale
        return super().get_resource(resource, region, query_params)

    def get_grandmaster_leaderboard(
        self, region: str, locale: str, region_id: int
    ) -> dict[str, Any]:
        """
        Return ladder data for the current season's grandmaster leaderboard.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            region_id (int): The ID of the region.

        Returns:
            Dict[str, Any]: A dictionary containing the grandmaster leaderboard data.
        """
        resource = f"/sc2/ladder/grandmaster{region_id}"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_season(self, region: str, locale: str, region_id: int) -> dict[str, Any]:
        """
        Return data about the current season.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            region_id (int): The ID of the region.

        Returns:
            Dict[str, Any]: A dictionary containing the season data.
        """
        resource = f"/sc2/ladder/season/{region_id}"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_player(self, region: str, locale: str, account_id: int) -> dict[str, Any]:
        """
        Return metadata for an individual's account.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            account_id (int): The ID of the account.

        Returns:
            Dict[str, Any]: A dictionary containing the account metadata.
        """
        resource = f"/sc2/player/{account_id}"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)
