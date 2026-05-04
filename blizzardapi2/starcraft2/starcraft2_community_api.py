"""starcraft2_community_api.py file."""

from typing import Any, Optional

from ..api import LocaleApi


class Starcraft2CommunityApi(LocaleApi):
    """All Starcraft 2 Community API methods.

    Attributes:
        client_id (str): A string client ID supplied by Blizzard.
        client_secret (str): A string client secret supplied by Blizzard.nch
        region (str, optional): A default region to use for requests.
        locale (str, optional): A default locale to use for requests.
    """

    def get_static(
        self,
        region_id: int,
        *,
        region: Optional[str] = None,
        locale: Optional[str] = None,
    ) -> dict[str, Any]:
        """
        Return all static SC2 profile data (achievements, categories, criteria, and rewards).

        Args:
            region_id (int): The ID of the region.
            region (str, optional): the region to query (e.g., "us", "eu"). Defaults to None, in which case the default region provided at instantiation is used.
            locale (str, optional): the locale to use for the response (e.g., "en_US", "es_MX"). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the static profile data.
        """
        resource = f"/sc2/static/profile/{region_id}"
        return super().get_resource(resource, region, locale)

    def get_metadata(
        self,
        region_id: int,
        realm_id: int,
        profile_id: int,
        *,
        region: Optional[str] = None,
        locale: Optional[str] = None,
    ) -> dict[str, Any]:
        """
        Return metadata for an individual's profile.

        Args:
            region_id (int): The ID of the region.
            realm_id (int): The ID of the realm.
            profile_id (int): The ID of the profile.
            region (str, optional): the region to query (e.g., "us", "eu"). Defaults to None, in which case the default region provided at instantiation is used.
            locale (str, optional): the locale to use for the response (e.g., "en_US", "es_MX"). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the profile metadata.
        """
        resource = f"/sc2/metadata/profile/{region_id}/{realm_id}/{profile_id}"
        return super().get_resource(resource, region, locale)

    def get_profile(
        self,
        region_id: int,
        realm_id: int,
        profile_id: int,
        *,
        region: Optional[str] = None,
        locale: Optional[str] = None,
        **query_params: Any,
    ) -> dict[str, Any]:
        """
        Return data about an individual SC2 profile.

        Args:
            region_id (int): The ID of the region.
            realm_id (int): The ID of the realm.
            profile_id (int): The ID of the profile.
            region (str, optional): the region to query (e.g., "us", "eu"). Defaults to None, in which case the default region provided at instantiation is used.
            locale (str, optional): the locale to use for the response (e.g., "en_US", "es_MX"). Defaults to None, in which case the default locale provided at instantiation is used.
            **query_params (Any): Additional query parameters.

        Returns:
            Dict[str, Any]: A dictionary containing the profile data.
        """
        resource = f"/sc2/profile/{region_id}/{realm_id}/{profile_id}"
        return super().get_resource(resource, region, locale, query_params)

    def get_ladder_summary(
        self,
        region_id: int,
        realm_id: int,
        profile_id: int,
        *,
        region: Optional[str] = None,
        locale: Optional[str] = None,
    ) -> dict[str, Any]:
        """
        Return a ladder summary for an individual SC2 profile.

        Args:
            region_id (int): The ID of the region.
            realm_id (int): The ID of the realm.
            profile_id (int): The ID of the profile.
            region (str, optional): the region to query (e.g., "us", "eu"). Defaults to None, in which case the default region provided at instantiation is used.
            locale (str, optional): the locale to use for the response (e.g., "en_US", "es_MX"). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the ladder summary.
        """
        resource = f"/sc2/profile/{region_id}/{realm_id}/{profile_id}/ladder/summary"
        return super().get_resource(resource, region, locale)

    def get_ladder(
        self,
        region_id: int,
        realm_id: int,
        profile_id: int,
        ladder_id: int,
        *,
        region: Optional[str] = None,
        locale: Optional[str] = None,
        **query_params: Any,
    ) -> dict[str, Any]:
        """
        Return data about an individual profile's ladder.

        Args:
            region_id (int): The ID of the region.
            realm_id (int): The ID of the realm.
            profile_id (int): The ID of the profile.
            ladder_id (int): The ID of the ladder.
            region (str, optional): the region to query (e.g., "us", "eu"). Defaults to None, in which case the default region provided at instantiation is used.
            locale (str, optional): the locale to use for the response (e.g., "en_US", "es_MX"). Defaults to None, in which case the default locale provided at instantiation is used.
            **query_params (Any): Additional query parameters.

        Returns:
            Dict[str, Any]: A dictionary containing the ladder data.
        """
        resource = (
            f"/sc2/profile/{region_id}/{realm_id}/{profile_id}/ladder/{ladder_id}"
        )
        return super().get_resource(resource, region, locale, query_params)

    def get_grandmaster_leaderboard(
        self,
        region_id: int,
        *,
        region: Optional[str] = None,
        locale: Optional[str] = None,
    ) -> dict[str, Any]:
        """
        Return ladder data for the current season's grandmaster leaderboard.

        Args:
            region_id (int): The ID of the region.
            region (str, optional): the region to query (e.g., "us", "eu"). Defaults to None, in which case the default region provided at instantiation is used.
            locale (str, optional): the locale to use for the response (e.g., "en_US", "es_MX"). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the grandmaster leaderboard data.
        """
        resource = f"/sc2/ladder/grandmaster/{region_id}"
        return super().get_resource(resource, region, locale)

    def get_season(
        self,
        region_id: int,
        *,
        region: Optional[str] = None,
        locale: Optional[str] = None,
    ) -> dict[str, Any]:
        """
        Return data about the current season.

        Args:
            region_id (int): The ID of the region.
            region (str, optional): the region to query (e.g., "us", "eu"). Defaults to None, in which case the default region provided at instantiation is used.
            locale (str, optional): the locale to use for the response (e.g., "en_US", "es_MX"). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the season data.
        """
        resource = f"/sc2/ladder/season/{region_id}"
        return super().get_resource(resource, region, locale)

    def get_player(
        self,
        account_id: int,
        *,
        region: Optional[str] = None,
        locale: Optional[str] = None,
    ) -> dict[str, Any]:
        """
        Return metadata for an individual's account.

        Args:
            account_id (int): The ID of the account.
            region (str, optional): the region to query (e.g., "us", "eu"). Defaults to None, in which case the default region provided at instantiation is used.
            locale (str, optional): the locale to use for the response (e.g., "en_US", "es_MX"). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the account metadata.
        """
        resource = f"/sc2/player/{account_id}"
        return super().get_resource(resource, region, locale)
