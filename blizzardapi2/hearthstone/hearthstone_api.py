"""Hearthstone API client.

This module provides access to the Hearthstone API endpoints,
including game data and card information.
"""

from dataclasses import dataclass

from .hearthstone_game_data_api import HearthstoneGameDataApi


@dataclass(slots=True, frozen=True)
class HearthstoneApi:
    """Hearthstone API client.

    This class provides access to Hearthstone game data through the Blizzard API,
    including card information, deck data, and other game-related endpoints.

    Example:
        ```python
        # Synchronous usage
        hs = HearthstoneApi(client_id="your_id", client_secret="your_secret")
        cards = hs.game_data.search_cards("us", "en_US", card_class="mage")
        deck = hs.game_data.get_deck("us", "en_US", code="AAECAf0EAA==")

        # Asynchronous usage
        async with HearthstoneApi(client_id="your_id", client_secret="your_secret") as hs:
            cards = await hs.game_data.search_cards("us", "en_US", card_class="mage")
            deck = await hs.game_data.get_deck("us", "en_US", code="AAECAf0EAA==")
        ```

    Attributes:
        client_id: The Blizzard API client ID.
        client_secret: The Blizzard API client secret.
        game_data: Client for Hearthstone game data endpoints (cards, decks, etc.).
    """

    client_id: str
    client_secret: str
    game_data: HearthstoneGameDataApi

    def __post_init__(self) -> None:
        """Validate and initialize the API client.

        Raises:
            ValueError: If client_id or client_secret is empty.
        """
        if not self.client_id or not self.client_secret:
            raise ValueError("client_id and client_secret must not be empty")

        # Initialize API clients
        object.__setattr__(
            self, "game_data", HearthstoneGameDataApi(self.client_id, self.client_secret)
        )
