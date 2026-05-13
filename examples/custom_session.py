import configparser
import os
from timeit import timeit

import requests
from cachecontrol import CacheControl

from blizzardapi2 import BlizzardApi, Region, Locale


# Create a custom Session class that uses CacheControl for caching GET requests to static namespaces
class MySession(requests.Session):
    def __init__(self):
        super().__init__()
        self._cache = CacheControl(
            requests.Session(),
        )

    def get(self, url, **kwargs):
        # Use the cached session when requesting static namespace resources, otherwise use the normal session
        _namespace: str = kwargs.get("params", {}).get("namespace", "") or kwargs.get(
            "headers", {}
        ).get("Battlenet-Namespace", "")
        return (
            self._cache.get(url, **kwargs)
            if _namespace.startswith("static")
            else super().get(url, **kwargs)
        )

    def request(self, method, url, **kwargs):
        # Override the request method to route GET requests through the cache and others through the normal flow
        return (
            self.get(url, **kwargs)
            if method.upper() == "GET"
            else super().request(method, url, **kwargs)
        )


# Read API data from a local config file
#   [battle.net]
#   client_id = ...
#   client_secret = ...
config = configparser.ConfigParser()
config.read(os.environ["CONFIG_PATH"])
battle_net_config = config["battle.net"]

# Instantiate two API clients, one with the custom session and one without
client1 = BlizzardApi(
    battle_net_config["client_id"],
    battle_net_config["client_secret"],
    region=Region.US,
    locale=Locale.EN_US,
)
client2 = BlizzardApi(
    battle_net_config["client_id"],
    battle_net_config["client_secret"],
    region=Region.US,
    locale=Locale.EN_US,
    session=MySession(),
)

# Test the performance of the uncached service
_ = client1.wow.game_data.get_achievement_categories_index()
print(
    timeit(
        stmt=client1.wow.game_data.get_achievement_categories_index,
        globals=globals(),
        number=5,
    )
)

# Test the performance of the cached service
_ = client2.wow.game_data.get_achievement_categories_index()
print(
    timeit(
        stmt=client2.wow.game_data.get_achievement_categories_index,
        globals=globals(),
        number=5,
    )
)
