"""starcraft2_community_api.py file."""

from typing import Dict, Any
from ..api import Api


class Starcraft2CommunityApi(Api):
    """All Starcraft 2 Community API methods.
    Attributes:
        client_id: A string client id supplied by Blizzard.
        client_secret: A string client secret supplied by Blizzard.
    """

    def __init__(self, client_id: str, client_secret: str) -> None:
        """Init Starcraft2CommunityApi."""
        super().__init__(client_id, client_secret)

    # Profile API
    def get_static(self, region: str, locale: str, region_id: int) -> Dict[str, Any]:
        """Returns all static SC2 profile data (achievements, categories, criteria, and rewards)."""
        resource = f"/sc2/static/profile/{region_id}"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_metadata(
        self, region: str, locale: str, region_id: int, realm_id: int, profile_id: int
    ) -> Dict[str, Any]:
        """Returns metadata for an individual's profile."""
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
    ) -> Dict[str, Any]:
        """Returns data about an individual SC2 profile."""
        resource = f"/sc2/profile/{region_id}/{realm_id}/{profile_id}"
        query_params["locale"] = locale
        return super().get_resource(resource, region, query_params)

    def get_ladder_summary(
        self, region: str, locale: str, region_id: int, realm_id: int, profile_id: int
    ) -> Dict[str, Any]:
        """Returns a ladder summary for an individual SC2 profile."""
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
    ) -> Dict[str, Any]:
        """Returns data about an individual profile's ladder."""
        resource = (
            f"/sc2/profile/{region_id}/{realm_id}/{profile_id}/ladder/{ladder_id}"
        )
        query_params["locale"] = locale
        return super().get_resource(resource, region, query_params)

    # Ladder API

    def get_grandmaster_leaderboard(
        self, region: str, locale: str, region_id: int
    ) -> Dict[str, Any]:
        """Returns ladder data for the current season's grandmaster leaderboard."""
        resource = f"/sc2/ladder/grandmaster{region_id}"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_season(self, region: str, locale: str, region_id: int) -> Dict[str, Any]:
        """Returns data about the current season."""
        resource = f"/sc2/ladder/season/{region_id}"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    # Account API
    def get_player(self, region: str, locale: str, account_id: int) -> Dict[str, Any]:
        """Returns metadata for an individual's account."""
        resource = f"/sc2/player/{account_id}"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)
