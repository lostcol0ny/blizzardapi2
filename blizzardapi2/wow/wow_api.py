"""World of Warcraft API client.

This module provides access to the World of Warcraft API endpoints,
including game data and profile information.
"""

from ..endpoint import ApiEndpoint
from .wow_game_data_api import WowGameDataApi
from .wow_profile_api import WowProfileApi


class WowApi(ApiEndpoint):
    """World of Warcraft API client.

    This class provides access to all World of Warcraft API endpoints.
    It organizes access to game data and profile functionality through
    the WowGameDataApi and WowProfileApi components.

    Attributes:
        client_id: A string client id supplied by Blizzard.
        client_secret: A string client secret supplied by Blizzard.
        region (Region, optional): A default region to use for requests.
        locale (Locale, optional): A default locale to use for community requests.
        session (requests.Session, optional): A default session to use for requests.
        game_data: The game data API client.
        profile: The profile API client.
    """

    def extend_endpoint(self) -> None:
        self.game_data = WowGameDataApi(
            self.client_id,
            self.client_secret,
            region=self.region,
            locale=self.locale,
            session=self.session,
        )
        self.profile = WowProfileApi(
            self.client_id,
            self.client_secret,
            region=self.region,
            locale=self.locale,
            session=self.session,
        )
