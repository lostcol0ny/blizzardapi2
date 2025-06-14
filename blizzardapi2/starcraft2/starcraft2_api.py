"""StarCraft II API client.

This module provides access to the StarCraft II API endpoints,
including game data and community information.
"""

from dataclasses import dataclass

from .starcraft2_community_api import Starcraft2CommunityApi
from .starcraft2_game_data_api import Starcraft2GameDataApi


@dataclass(slots=True, frozen=True)
class Starcraft2Api:
    """StarCraft II API client.

    This class provides access to StarCraft II game data and community
    information through the Blizzard API. It's organized into two main
    components: game data and community data.

    Example:
        ```python
        # Synchronous usage
        sc2 = Starcraft2Api(client_id="your_id", client_secret="your_secret")
        profile = sc2.community.get_profile(1, 2, 3)
        league = sc2.game_data.get_league(1)

        # Asynchronous usage
        async with Starcraft2Api(client_id="your_id", client_secret="your_secret") as sc2:
            profile = await sc2.community.get_profile(1, 2, 3)
            league = await sc2.game_data.get_league(1)
        ```

    Attributes:
        client_id: The Blizzard API client ID.
        client_secret: The Blizzard API client secret.
        community: Client for StarCraft II community endpoints (profiles, ladders, etc.).
        game_data: Client for StarCraft II game data endpoints (leagues, seasons, etc.).
    """

    client_id: str
    client_secret: str
    community: Starcraft2CommunityApi
    game_data: Starcraft2GameDataApi

    def __post_init__(self) -> None:
        """Validate and initialize the API client.

        Raises:
            ValueError: If client_id or client_secret is empty.
        """
        if not self.client_id or not self.client_secret:
            raise ValueError("client_id and client_secret must not be empty")

        # Initialize API clients
        object.__setattr__(
            self, "community", Starcraft2CommunityApi(self.client_id, self.client_secret)
        )
        object.__setattr__(
            self, "game_data", Starcraft2GameDataApi(self.client_id, self.client_secret)
        )
