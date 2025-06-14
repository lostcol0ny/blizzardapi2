# Diablo 3 API Documentation

This document provides information about the Diablo 3 API endpoints available in the blizzardapi2 library.

## Available Endpoints

### Community API

The Community API provides access to Diablo 3 community data.

```python
from blizzardapi2 import BlizzardApi
from blizzardapi2.diablo3.diablo3_community_api import Region, Locale

api_client = BlizzardApi("client_id", "client_secret")

# Get career profile
career_profile = api_client.diablo3.community.get_career_profile(
    Region.US,
    Locale.EN_US,
    "battletag"
)

# Get hero profile
hero_profile = api_client.diablo3.community.get_hero_profile(
    Region.US,
    Locale.EN_US,
    "battletag",
    "hero_id"
)
```

### Game Data API

The Game Data API provides access to Diablo 3 game data.

```python
# Get season index
season_index = api_client.diablo3.game_data.get_season_index(
    Region.US,
    Locale.EN_US
)

# Get season
season = api_client.diablo3.game_data.get_season(
    Region.US,
    Locale.EN_US,
    "season_id"
)

# Get leaderboard
leaderboard = api_client.diablo3.game_data.get_leaderboard(
    Region.US,
    Locale.EN_US,
    "season_id",
    "leaderboard"
)
```

## Async Usage

All endpoints support async/await for better performance:

```python
import asyncio
from blizzardapi2 import BlizzardApi
from blizzardapi2.diablo3.diablo3_community_api import Region, Locale

async def main():
    api_client = BlizzardApi("client_id", "client_secret")

    # Get career profile
    career_profile = await api_client.diablo3.community.get_career_profile(
        Region.US,
        Locale.EN_US,
        "battletag"
    )

asyncio.run(main())
```

## Response Types

All API responses are returned as structured dataclasses with proper type hints. This provides better code completion and type checking in your IDE.

## Error Handling

The library includes comprehensive error handling for API responses. All errors are raised as exceptions with descriptive messages to help with debugging.
