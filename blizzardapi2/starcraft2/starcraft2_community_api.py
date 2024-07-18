"""starcraft2_community_api.py file."""
from ..api import Api


class Starcraft2CommunityApi(Api):
    """All Starcraft 2 Community API methods.

    Attributes:
        client_id: A string client id supplied by Blizzard.
        client_secret: A string client secret supplied by Blizzard.
    """

    def __init__(self, client_id, client_secret):
        """Init Starcraft2CommunityApi."""
        super().__init__(client_id, client_secret)

    # Profile API

    def get_static(self, region: str, locale:str, region_id: int):
        """Returns all static SC2 profile data (achievements, categories, criteria, and rewards)."""
        resource = f"/sc2/static/profile/{region_id}"
        query_params = ({"locale": locale})
        return super().get_resource(resource, region, query_params)

    def get_metadata(self, region, locale, region_id, realm_id, profile_id):
        """Returns metadata for an individual's profile."""
        resource = f"/sc2/metadata/profile/{region_id}/{realm_id}/{profile_id}"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_profile(self, region, locale, region_id, realm_id, profile_id, **query_params):
        """Returns data about an individual SC2 profile."""
        resource = f"/sc2/profile/{region_id}/{realm_id}/{profile_id}"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_ladder_summary(self, region, locale, region_id, realm_id, profile_id):
        """Returns a ladder summary for an individual SC2 profile."""
        resource = f"/sc2/profile/{region_id}/{realm_id}/{profile_id}/ladder/summary"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_ladder(self, region, locale, region_id, realm_id, profile_id, ladder_id, **query_params):
        """Returns data about an individual profile's ladder."""
        resource = f"/sc2/profile/{region_id}/{realm_id}/{profile_id}/ladder/{ladder_id}"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)
    
    # Ladder API
    
    def get_grandmaster_leaderboard(self, region, locale, region_id):
        """Returns ladder data for the current season's grandmaster leaderboard."""
        resource = f"/sc2/ladder/grandmaster{region_id}"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_season(self, region, locale, region_id):
        """Returns data about the current season."""
        resource = f"/sc2/ladder/season/{region_id}"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)
    
    # Account API

    def get_player(self, region, locale, account_id):
        """Returns metadata for an individual's account."""
        resource = f"/sc2/player/{account_id}"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)
