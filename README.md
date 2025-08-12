# Blizzard API 2

[![PyPI version](https://badge.fury.io/py/blizzardapi2.svg)](https://badge.fury.io/py/blizzardapi2)
[![Python Versions](https://img.shields.io/pypi/pyversions/blizzardapi2.svg)](https://pypi.org/project/blizzardapi2/)
[![Downloads](https://img.shields.io/pypi/dm/blizzardapi2.svg)](https://pypi.org/project/blizzardapi2/)
[![Build Status](https://github.com/lostcol0ny/python-blizzardapi2/actions/workflows/python-package.yml/badge.svg)](https://github.com/lostcol0ny/python-blizzardapi2/actions/workflows/python-package.yml)

![GitHub](https://img.shields.io/github/license/lostcol0ny/python-blizzardapi2)[![Dependabot](https://github.com/lostcol0ny/blizzardapi2/actions/workflows/dependabot/dependabot-updates/badge.svg)](https://github.com/lostcol0ny/blizzardapi2/actions/workflows/dependabot/dependabot-updates)[![CodeQL](https://github.com/lostcol0ny/python-blizzardapi2/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/lostcol0ny/python-blizzardapi2/actions/workflows/github-code-scanning/codeql)[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

blizzardapi2 is a client library for Blizzard's APIs. It's a fork of [the original library](https://github.com/trevorphillipscoding/python-blizzardapi/).

Current supported features include:

- Battle.net User
- WoW Profile
- WoW Game Data
- WoW Classic Game Data
- Diablo 3 Community
- Diablo 3 Game Data
- Hearthstone Game Data
- Starcraft 2 Community
- Starcraft 2 Game Data

Modern features:

- Full type hints support
- Async/await support for better performance
- Enum-based region and locale validation
- Structured response types using dataclasses
- Improved error handling and logging

To gain access to Blizzard's API please register [here](https://develop.battle.net/access/) to obtain a client id and client secret.

For more information on Blizzard's API visit:

[Official Documentation](https://develop.battle.net/documentation)  
[Official API Forum](https://us.forums.blizzard.com/en/blizzard/c/api-discussion)

# Requirements

Python (3.11+)

# Installing

`pip install blizzardapi2`

# Examples

**Basic Usage**

```python
from blizzardapi2 import BlizzardApi
from blizzardapi2.types import Locale, Region

api_client = BlizzardApi("client_id", "client_secret")

# Unprotected API endpoint
categories_index = api_client.wow.game_data.get_achievement_categories_index(
    Region.US,
    Locale.EN_US
)

# Protected API endpoint
summary = api_client.wow.profile.get_account_profile_summary(
    Region.US,
    Locale.EN_US,
    "access_token"
)

# Wow Classic endpoint
connected_realms_index = api_client.wow.game_data.get_connected_realms_index(
    Region.US,
    Locale.EN_US,
    is_classic=True
)
```

**Async Usage**

```python
import asyncio
from blizzardapi2 import BlizzardApi
from blizzardapi2.types import Locale, Region

async def main():
    api_client = BlizzardApi("client_id", "client_secret")

    # Async API calls
    profile = await api_client.wow.profile.get_account_profile_summary(
        Region.US,
        Locale.EN_US,
        "access_token"
    )

    # Multiple concurrent requests
    tasks = [
        api_client.wow.profile.get_character_profile_summary(
            Region.US,
            Locale.EN_US,
            "realm-slug",
            "character-name"
        ),
        api_client.wow.profile.get_character_achievements_summary(
            Region.US,
            Locale.EN_US,
            "realm-slug",
            "character-name"
        )
    ]
    results = await asyncio.gather(*tasks)

asyncio.run(main())
```

# Access token vs Client ID/Client Secret

You can pass in a `client_id` and `client_secret` and use almost any endpoint except for a few that require an `access_token` obtained via OAuth authorization code flow. You can find more information at https://develop.battle.net/documentation/guides/using-oauth/authorization-code-flow.

Here is the list of endpoints, specified by Blizzard, that require an OAuth token:

```
GET /oauth/userinfo
GET /profile/user/wow
GET /profile/user/wow/protected-character/{realm-id}-{character-id}
GET /profile/user/wow/collections
GET /profile/user/wow/collections/pets
GET /profile/user/wow/collections/mounts
```

# Documentation

For detailed documentation on each game's API, see the following README files:

- [WoW API Documentation](docs/wow/README.md)
- [Diablo 3 API Documentation](docs/diablo3/README.md)
- [Hearthstone API Documentation](docs/hearthstone/README.md)
- [Starcraft 2 API Documentation](docs/starcraft2/README.md)
