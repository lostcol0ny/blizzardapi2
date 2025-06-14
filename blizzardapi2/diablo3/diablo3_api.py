"""Diablo III API client.

This module provides access to the Diablo III API endpoints,
including game data and community information.
"""

from ..api import BaseApi
from .diablo3_community_api import Diablo3CommunityApi
from .diablo3_game_data_api import Diablo3GameDataApi


class Diablo3Api(BaseApi):
    """Diablo III API client.

    This class provides access to all Diablo III API endpoints.
    It organizes access to community and game data functionality through
    the Diablo3CommunityApi and Diablo3GameDataApi components.

    Attributes:
        _client_id: The Blizzard API client ID.
        _client_secret: The Blizzard API client secret.
        community: The community API client.
        game_data: The game data API client.
    """

    def __init__(self, client_id: str, client_secret: str) -> None:
        """Initialize the API client.

        Args:
            client_id: The Blizzard API client ID.
            client_secret: The Blizzard API client secret.
        """
        self._client_id = client_id
        self._client_secret = client_secret
        self.community = Diablo3CommunityApi(client_id, client_secret)
        self.game_data = Diablo3GameDataApi(client_id, client_secret)
