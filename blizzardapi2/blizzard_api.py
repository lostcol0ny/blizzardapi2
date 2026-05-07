"""Main entry point for the Blizzard API client.

This module provides a unified interface to all Blizzard game APIs through
a single client instance. Each game's API is accessible through its own
property on the main client.
"""

from .battlenet.battlenet_api import BattlenetApi
from .diablo3.diablo3_api import Diablo3Api
from .endpoint import ApiEndpoint
from .hearthstone.hearthstone_api import HearthstoneApi
from .starcraft2.starcraft2_api import Starcraft2Api
from .wow.wow_api import WowApi


class BlizzardApi(ApiEndpoint):
    """Blizzard API client.

    This class provides access to all Blizzard game APIs through a unified
    interface. It organizes access to individual game APIs through their
    respective components.

    Attributes:
        wow: The World of Warcraft API client.
        diablo3: The Diablo III API client.
        hearthstone: The Hearthstone API client.
        starcraft2: The StarCraft II API client.
        battlenet: The Battle.net API client.
    """

    def extend_endpoint(self) -> None:
        self.wow = WowApi(self.client_id, self.client_secret, self.region, self.locale)
        self.diablo3 = Diablo3Api(
            self.client_id, self.client_secret, self.region, self.locale
        )
        self.hearthstone = HearthstoneApi(
            self.client_id, self.client_secret, self.region, self.locale
        )
        self.starcraft2 = Starcraft2Api(
            self.client_id, self.client_secret, self.region, self.locale
        )
        self.battlenet = BattlenetApi(self.client_id, self.client_secret, self.region)
