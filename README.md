# blizzardapi2
![GitHub](https://img.shields.io/github/license/lostcol0ny/python-blizzardapi2)[![Python package](https://github.com/lostcol0ny/python-blizzardapi2/actions/workflows/python-package.yml/badge.svg?branch=main)](https://github.com/lostcol0ny/python-blizzardapi2/actions/workflows/python-package.yml)[![Dependabot Updates](https://github.com/lostcol0ny/python-blizzardapi2/actions/workflows/dependabot/dependabot-updates/badge.svg?branch=main)](https://github.com/lostcol0ny/python-blizzardapi2/actions/workflows/dependabot/dependabot-updates)[![CodeQL](https://github.com/lostcol0ny/python-blizzardapi2/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/lostcol0ny/python-blizzardapi2/actions/workflows/github-code-scanning/codeql)

blizzardapi2 is a client library for Blizzard's APIs. It's a fork of [the original library](https://github.com/trevorphillipscoding/python-blizzardapi/) and I'm trying to update it and keep its packages managed.

Current supported features include:
- Battle.net User
- Wow Profile
- Wow Game Data
- Wow Classic Game Data
- Diablo 3 Community
- Diablo 3 Game Data
- Hearthstone Game Data

To gain access to Blizzard's API please register [here](https://develop.battle.net/access/) to obtain a client id and client secret.

For more information on Blizzard's API visit:

[Official Documentation](https://develop.battle.net/documentation)  
[Official API Forum](https://us.forums.blizzard.com/en/blizzard/c/api-discussion)

# Requirements

Python (3.9, 3.10, 3.11)

# Installing

`pip install blizzardapi2`
    
# Example

**main.py**
```python
from blizzardapi2 import BlizzardApi

api_client = BlizzardApi("client_id", "client_secret")

# Unprotected API endpoint
categories_index = api_client.wow.game_data.get_achievement_categories_index("us", "en_US")

# Protected API endpoint
summary = api_client.wow.profile.get_account_profile_summary("us", "en_US", "access_token")

# Wow Classic endpoint
connected_realms_index = api_client.wow.game_data.get_connected_realms_index("us", "en_US", is_classic=True)
```

# Access token vs Client ID/Client Secret

You can pass in a `client_id` and `client_secret` and use almost any endpoint except for a few that require an `access_token` obtained via OAuth authorization code flow. You can find more information at https://develop.battle.net/documentation/guides/using-oauth/authorization-code-flow.

Here is the list of endpoints, specified by Blizzard, that require an OAuth token.

```
GET /oauth/userinfo
GET /profile/user/wow
GET /profile/user/wow/protected-character/{realm-id}-{character-id}
GET /profile/user/wow/collections
GET /profile/user/wow/collections/pets
GET /profile/user/wow/collections/mounts
```
