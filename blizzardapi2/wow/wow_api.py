"""World of Warcraft API client.

This module provides access to the World of Warcraft API endpoints,
including game data and profile information.
"""

from ..api import BaseApi
from .wow_game_data_api import WowGameDataApi
from .wow_profile_api import WowProfileApi


class WowApi(BaseApi):
    """World of Warcraft API client.

    This class provides access to all World of Warcraft API endpoints.
    It organizes access to game data and profile functionality through
    the WowGameDataApi and WowProfileApi components.

    Attributes:
        _client_id: The Blizzard API client ID.
        _client_secret: The Blizzard API client secret.
        game_data: The game data API client.
        profile: The profile API client.
    """

    def __init__(self, client_id: str, client_secret: str) -> None:
        """Initialize the API client.

        Args:
            client_id: The Blizzard API client ID.
            client_secret: The Blizzard API client secret.
        """
        super().__init__(client_id, client_secret)
        self.game_data = WowGameDataApi(client_id, client_secret)
        self.profile = WowProfileApi(client_id, client_secret)
