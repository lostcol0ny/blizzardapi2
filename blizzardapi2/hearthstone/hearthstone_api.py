"""Hearthstone API client.

This module exposes the Hearthstone facade. Hearthstone has only one
sub-domain (game data), but this file mirrors the structure of the other
game packages (`wow.game_data`, `diablo3.game_data`, etc.) so the public
API surface stays consistent.
"""

from ..endpoint import ApiEndpoint
from .hearthstone_game_data_api import HearthstoneGameDataApi


class HearthstoneApi(ApiEndpoint):
    """Hearthstone API client.

    Exposes Hearthstone endpoints under ``.game_data`` for consistency with
    the other game facades (``wow.game_data``, ``diablo3.game_data``, ...).

    Example:
        ```python
        api = BlizzardApi("your_id", "your_secret")
        cards = api.hearthstone.game_data.search_cards(Region.US, Locale.EN_US)
        card = api.hearthstone.game_data.get_card(Region.US, Locale.EN_US, "test-card")
        ```

    Attributes:
        client_id: The Blizzard API client ID.
        client_secret: The Blizzard API client secret.
        region: Default region to use for requests.
        locale: Default locale to use for requests.
        game_data: The Hearthstone game-data API client.
    """

    def extend_endpoint(self) -> None:
        """Add the Hearthstone game-data endpoint."""
        self.game_data = HearthstoneGameDataApi(
            self.client_id, self.client_secret, self.region, self.locale
        )
