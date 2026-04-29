"""Hearthstone API client.

This module exposes the Hearthstone facade. Hearthstone has only one
sub-domain (game data), but this file mirrors the structure of the other
game packages (`wow.game_data`, `diablo3.game_data`, etc.) so the public
API surface stays consistent.
"""

from typing import Any, Dict

from ..api import BaseApi
from ..types import Locale, Region
from .hearthstone_game_data_api import HearthstoneGameDataApi


class ApiResponse:
    """Wrapper for API responses with metadata."""

    data: Dict[str, Any]
    region: Region
    locale: Locale
    namespace: str


class HearthstoneApi(BaseApi):
    """Hearthstone API client facade.

    Exposes Hearthstone endpoints under ``.game_data`` for consistency with
    the other game facades (``wow.game_data``, ``diablo3.game_data``, ...).

    Example:
        ```python
        api = BlizzardApi("your_id", "your_secret")
        cards = api.hearthstone.game_data.search_cards("us", "en_US")
        card = api.hearthstone.game_data.get_card("us", "en_US", "test-card")
        ```

    Attributes:
        _client_id: The Blizzard API client ID.
        _client_secret: The Blizzard API client secret.
        game_data: The Hearthstone game-data API client.
    """

    def __init__(self, client_id: str, client_secret: str) -> None:
        """Initialize the API client.

        Args:
            client_id: The Blizzard API client ID.
            client_secret: The Blizzard API client secret.
        """
        super().__init__(client_id, client_secret)
        self.game_data = HearthstoneGameDataApi(client_id, client_secret)
