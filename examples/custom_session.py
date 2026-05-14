"""
custom_session.py

This file demonstrates how to enable the caching of requests from the various
`blizzardapi2` APIs using the `session=` parameter and a custom request.Session object
"""

from __future__ import annotations

import configparser
import os
from timeit import timeit

import requests
from cachecontrol import CacheControl

from blizzardapi2 import BlizzardApi, Locale, Region


class MySession(requests.Session):
    """
    Create a custom Session class that uses CacheControl for caching GET requests to
    static namespaces.
    """

    def __init__(self):
        super().__init__()
        self._cache = CacheControl(
            requests.Session(),
        )

    def get(  # pyright: ignore[reportIncompatibleMethodOverride]
        self, url: str | bytes, **kwargs
    ) -> requests.Response:
        """
        Sends a GET request.  Returns a :class:`Response` object.

        Uses a separate cached session when requesting static namespace resources,
        otherwise use the normal session
        """
        _namespace: str = kwargs.get("params", {}).get("namespace", "") or kwargs.get(
            "headers", {}
        ).get("Battlenet-Namespace", "")
        return (
            self._cache.get(url, **kwargs)
            if _namespace.startswith("static")
            else super().get(url, **kwargs)
        )

    def request(  # pyright: ignore[reportIncompatibleMethodOverride]
        self, method: str, url: str | bytes, **kwargs
    ) -> requests.Response:
        """
        Sends a request.  Returns a :class:`Response` object.

        Override the request method to route GET requests through the cache and others
        through the normal flow
        """
        #
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
