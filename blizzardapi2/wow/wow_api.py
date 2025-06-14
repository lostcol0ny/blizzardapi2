"""World of Warcraft API client.

This module provides access to the World of Warcraft API endpoints,
including game data and profile information.
"""

from dataclasses import dataclass

from .wow_game_data_api import WowGameDataApi
from .wow_profile_api import WowProfileApi


@dataclass(slots=True, frozen=True)
class WowApi:
    """World of Warcraft API client.

    This class provides access to World of Warcraft game data and profile
    information through the Blizzard API. It's organized into two main
    components: game data and profile data.

    Example:
        ```python
        # Synchronous usage
        wow = WowApi(client_id="your_id", client_secret="your_secret")
        character = wow.profile.get_character_profile("realm", "character")
        items = wow.game_data.get_item(12345)

        # Asynchronous usage
        async with WowApi(client_id="your_id", client_secret="your_secret") as wow:
            character = await wow.profile.get_character_profile("realm", "character")
            items = await wow.game_data.get_item(12345)
        ```

    Attributes:
        client_id: The Blizzard API client ID.
        client_secret: The Blizzard API client secret.
        game_data: Client for WoW game data endpoints (items, mounts, etc.).
        profile: Client for WoW profile endpoints (characters, guilds, etc.).
    """

    client_id: str
    client_secret: str
    game_data: WowGameDataApi
    profile: WowProfileApi

    def __post_init__(self) -> None:
        """Validate and initialize the API client.

        Raises:
            ValueError: If client_id or client_secret is empty.
        """
        if not self.client_id or not self.client_secret:
            raise ValueError("client_id and client_secret must not be empty")

        # Initialize API clients
        object.__setattr__(
            self, "game_data", WowGameDataApi(self.client_id, self.client_secret)
        )
        object.__setattr__(
            self, "profile", WowProfileApi(self.client_id, self.client_secret)
        )
