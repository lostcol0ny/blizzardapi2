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
- Automatic token management with intelligent refresh
- Enum-based region and locale validation
- Clean, maintainable codebase
- Comprehensive error handling

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

api_client = BlizzardApi("client_id", "client_secret")

# Public API endpoint (uses automatic client credentials token)
categories_index = api_client.wow.game_data.get_achievement_categories_index(
    "us",  # region
    "en_US"  # locale
)

# Protected API endpoint (requires user OAuth token)
summary = api_client.wow.profile.get_account_profile_summary(
    "us",
    "en_US",
    "user_access_token"  # OAuth token from authorization code flow
)

# WoW Classic endpoint
connected_realms_index = api_client.wow.game_data.get_connected_realms_index(
    "us",
    "en_US",
    is_classic=True
)
```

**Token Management**

The library automatically manages client credentials tokens for public endpoints:

```python
from blizzardapi2 import BlizzardApi

api_client = BlizzardApi("client_id", "client_secret")

# First call: library automatically fetches and caches a client credentials token
realms = api_client.wow.game_data.get_realms_index("us", "en_US")

# Subsequent calls: library reuses the cached token
achievements = api_client.wow.game_data.get_achievements_index("us", "en_US")

# When token expires: library automatically refreshes it
# You don't need to manage tokens manually!
```

# Access token vs Client ID/Client Secret

You can pass in a `client_id` and `client_secret` and use almost any endpoint except for a few that require an `access_token` obtained via OAuth authorization code flow. You can find more information at https://develop.battle.net/documentation/guides/using-oauth/authorization-code-flow.

**Important:** The library handles all tokens securely by passing them in Authorization headers, never in URLs. When you provide a user OAuth token to methods like `get_account_profile_summary()`, the library automatically:
1. Extracts the token from parameters
2. Sends it via `Authorization: Bearer <token>` header
3. Keeps tokens out of URL query strings

Here is the list of endpoints, specified by Blizzard, that require an OAuth token:

```
GET /oauth/userinfo
GET /profile/user/wow
GET /profile/user/wow/protected-character/{realm-id}-{character-id}
GET /profile/user/wow/collections
GET /profile/user/wow/collections/pets
GET /profile/user/wow/collections/mounts
```

**Note:** For these protected endpoints, you must implement the OAuth authorization code flow in your application to obtain a user access token. The library does not handle the OAuth flow itself - it only accepts and uses the token you provide.

# Documentation

For detailed documentation on each game's API, see the following README files:

- [WoW API Documentation](docs/wow/README.md)
- [Diablo 3 API Documentation](docs/diablo3/README.md)
- [Hearthstone API Documentation](docs/hearthstone/README.md)
- [Starcraft 2 API Documentation](docs/starcraft2/README.md)
