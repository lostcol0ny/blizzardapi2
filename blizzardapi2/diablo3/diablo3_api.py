"""Diablo III API client.

This module provides access to the Diablo III API endpoints,
including game data and community information.
"""

from ..endpoint import ApiEndpoint
from .diablo3_community_api import Diablo3CommunityApi
from .diablo3_game_data_api import Diablo3GameDataApi


class Diablo3Api(ApiEndpoint):
    """Diablo III API client.

    This class provides access to all Diablo III API endpoints.
    It organizes access to community and game data functionality through
    the Diablo3CommunityApi and Diablo3GameDataApi components.

    Attributes:
        client_id: A string client id supplied by Blizzard.
        client_secret: A string client secret supplied by Blizzard.
        region (Region, optional): A default region to use for requests.
        locale (Locale, optional): A default locale to use for community requests.
        session (requests.Session, optional): A default session to use for requests.
        community: The community API client.
        game_data: The game data API client.
    """

    def extend_endpoint(self) -> None:
        self.community = Diablo3CommunityApi(
            self.client_id,
            self.client_secret,
            region=self.region,
            locale=self.locale,
            session=self.session,
        )
        self.game_data = Diablo3GameDataApi(
            self.client_id, self.client_secret, region=self.region, session=self.session
        )
