"""Main entry point for the Blizzard API client.

This module provides a unified interface to all Blizzard game APIs through
a single client instance. Each game's API is accessible through its own
property on the main client.
"""

from .api import BaseApi
from .battlenet.battlenet_api import BattlenetApi
from .diablo3.diablo3_api import Diablo3Api
from .hearthstone.hearthstone_api import HearthstoneApi
from .starcraft2.starcraft2_api import Starcraft2Api
from .wow.wow_api import WowApi


class BlizzardApi(BaseApi):
    """Blizzard API client.

    This class provides access to all Blizzard game APIs through a unified
    interface. It organizes access to individual game APIs through their
    respective components.

    Attributes:
        _client_id: The Blizzard API client ID.
        _client_secret: The Blizzard API client secret.
        wow: The World of Warcraft API client.
        diablo3: The Diablo III API client.
        hearthstone: The Hearthstone API client.
        starcraft2: The StarCraft II API client.
        battlenet: The Battle.net API client.
    """

    def __init__(self, client_id: str, client_secret: str) -> None:
        """Initialize the API client.

        Args:
            client_id: The Blizzard API client ID.
            client_secret: The Blizzard API client secret.
        """
        self._client_id = client_id
        self._client_secret = client_secret
        self.wow = WowApi(client_id, client_secret)
        self.diablo3 = Diablo3Api(client_id, client_secret)
        self.hearthstone = HearthstoneApi(client_id, client_secret)
        self.starcraft2 = Starcraft2Api(client_id, client_secret)
        self.battlenet = BattlenetApi(client_id, client_secret)

    async def __aenter__(self) -> "BlizzardApi":
        """Async context manager entry.

        Initializes async sessions for all game API clients.

        Returns:
            BlizzardApi: The initialized API client.
        """
        # Initialize async sessions for all game clients
        await self.battlenet.__aenter__()
        await self.diablo3.__aenter__()
        await self.hearthstone.__aenter__()
        await self.wow.__aenter__()
        await self.starcraft2.__aenter__()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        """Async context manager exit.

        Closes async sessions for all game API clients.

        Args:
            exc_type: The type of exception that was raised, if any.
            exc_val: The exception instance that was raised, if any.
            exc_tb: The traceback for the exception, if any.
        """
        # Close async sessions for all game clients
        await self.battlenet.__aexit__(exc_type, exc_val, exc_tb)
        await self.diablo3.__aexit__(exc_type, exc_val, exc_tb)
        await self.hearthstone.__aexit__(exc_type, exc_val, exc_tb)
        await self.wow.__aexit__(exc_type, exc_val, exc_tb)
        await self.starcraft2.__aexit__(exc_type, exc_val, exc_tb)

    @property
    def client_id(self) -> str:
        """Get the client ID.

        Returns:
            str: The Blizzard API client ID.
        """
        return self._client_id

    @property
    def client_secret(self) -> str:
        """Get the client secret.

        Returns:
            str: The Blizzard API client secret.
        """
        return self._client_secret
