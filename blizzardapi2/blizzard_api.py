"""Main entry point for the Blizzard API client.

This module provides a unified interface to all Blizzard game APIs through
a single client instance. Each game's API is accessible through its own
property on the main client.
"""

from typing import Final

from .battlenet.battlenet_api import BattlenetApi
from .diablo3.diablo3_api import Diablo3Api
from .hearthstone.hearthstone_api import HearthstoneApi
from .starcraft2.starcraft2_api import Starcraft2Api
from .wow.wow_api import WowApi


class BlizzardApi:
    """Unified client for accessing all Blizzard game APIs.
    
    This class serves as the main entry point for the Blizzard API client.
    It initializes and provides access to individual game API clients
    (WoW, Diablo 3, Hearthstone, etc.) through properties.
    
    Example:
        ```python
        # Synchronous usage
        client = BlizzardApi(client_id="your_client_id", client_secret="your_client_secret")
        character = client.wow.get_character_profile("realm", "character")
        
        # Asynchronous usage
        async with BlizzardApi(client_id="your_client_id", client_secret="your_client_secret") as client:
            character = await client.wow.get_character_profile("realm", "character")
            profile = await client.diablo3.get_profile("battletag")
        ```
    
    Attributes:
        client_id: The Blizzard API client ID.
        client_secret: The Blizzard API client secret.
        battlenet: Client for Battle.net API endpoints.
        diablo3: Client for Diablo 3 API endpoints.
        hearthstone: Client for Hearthstone API endpoints.
        starcraft2: Client for StarCraft 2 API endpoints.
        wow: Client for World of Warcraft API endpoints.
    """

    def __init__(self, client_id: str, client_secret: str) -> None:
        """Initialize the Blizzard API client.
        
        Args:
            client_id: The Blizzard API client ID.
            client_secret: The Blizzard API client secret.
            
        Raises:
            ValueError: If client_id or client_secret is empty.
        """
        if not client_id or not client_secret:
            raise ValueError("client_id and client_secret must not be empty")
            
        self._client_id: Final[str] = client_id
        self._client_secret: Final[str] = client_secret
        
        # Initialize game API clients
        self.battlenet: Final[BattlenetApi] = BattlenetApi(client_id, client_secret)
        self.diablo3: Final[Diablo3Api] = Diablo3Api(client_id, client_secret)
        self.hearthstone: Final[HearthstoneApi] = HearthstoneApi(client_id, client_secret)
        self.wow: Final[WowApi] = WowApi(client_id, client_secret)
        self.starcraft2: Final[Starcraft2Api] = Starcraft2Api(client_id, client_secret)
    
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
