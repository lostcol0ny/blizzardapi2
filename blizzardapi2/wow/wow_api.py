"""World of Warcraft API client.

This module provides access to the World of Warcraft API endpoints,
including game data and profile information.
"""

from blizzardapi2.endpoint import ApiEndpoint

from .wow_game_data_api import WowGameDataApi
from .wow_profile_api import WowProfileApi


class WowApi(ApiEndpoint):
    """World of Warcraft API client.

    This class provides access to all World of Warcraft API endpoints.
    It organizes access to game data and profile functionality through
    the WowGameDataApi and WowProfileApi components.

    Attributes:
        game_data: The game data API client.
        profile: The profile API client.
    """

    def extend_endpoint(self) -> None:
        self.game_data = WowGameDataApi(
            self.client_id, self.client_secret, self.region, self.locale
        )
        self.profile = WowProfileApi(
            self.client_id, self.client_secret, self.region, self.locale
        )
