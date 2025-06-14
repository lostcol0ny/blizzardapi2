"""Diablo III API client.

This module provides access to the Diablo III API endpoints,
including game data and community information.
"""

from dataclasses import dataclass

from .diablo3_community_api import Diablo3CommunityApi
from .diablo3_game_data_api import Diablo3GameDataApi


@dataclass(slots=True, frozen=True)
class Diablo3Api:
    """Diablo III API client.

    This class provides access to Diablo III game data and community
    information through the Blizzard API. It's organized into two main
    components: game data and community data.

    Example:
        ```python
        # Synchronous usage
        d3 = Diablo3Api(client_id="your_id", client_secret="your_secret")
        profile = d3.community.get_profile("us", "en_US", "battletag")
        item = d3.game_data.get_item("us", "en_US", "item-slug")

        # Asynchronous usage
        async with Diablo3Api(client_id="your_id", client_secret="your_secret") as d3:
            profile = await d3.community.get_profile("us", "en_US", "battletag")
            item = await d3.game_data.get_item("us", "en_US", "item-slug")
        ```

    Attributes:
        client_id: The Blizzard API client ID.
        client_secret: The Blizzard API client secret.
        community: Client for Diablo III community endpoints (profiles, heroes, etc.).
        game_data: Client for Diablo III game data endpoints (items, skills, etc.).
    """

    client_id: str
    client_secret: str
    community: Diablo3CommunityApi
    game_data: Diablo3GameDataApi

    def __post_init__(self) -> None:
        """Validate and initialize the API client.

        Raises:
            ValueError: If client_id or client_secret is empty.
        """
        if not self.client_id or not self.client_secret:
            raise ValueError("client_id and client_secret must not be empty")

        # Initialize API clients
        object.__setattr__(
            self, "community", Diablo3CommunityApi(self.client_id, self.client_secret)
        )
        object.__setattr__(
            self, "game_data", Diablo3GameDataApi(self.client_id, self.client_secret)
        )
