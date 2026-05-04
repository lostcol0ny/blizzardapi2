"""Diablo III API client.

This module provides access to the Diablo III API endpoints,
including game data and community information.
"""

from blizzardapi2.endpoint import ApiEndpoint

from .diablo3_community_api import Diablo3CommunityApi
from .diablo3_game_data_api import Diablo3GameDataApi


class Diablo3Api(ApiEndpoint):
    """Diablo III API client.

    This class provides access to all Diablo III API endpoints.
    It organizes access to community and game data functionality through
    the Diablo3CommunityApi and Diablo3GameDataApi components.

    Attributes:
        community: The community API client.
        game_data: The game data API client.
    """

    def extend_endpoint(self) -> None:
        self.community = Diablo3CommunityApi(
            self.client_id, self.client_secret, self.region, self.locale
        )
        self.game_data = Diablo3GameDataApi(
            self.client_id, self.client_secret, self.region
        )
