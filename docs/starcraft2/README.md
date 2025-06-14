# StarCraft 2 API Documentation

This document provides information about the StarCraft 2 API endpoints available in the blizzardapi2 library.

## Available Endpoints

### Community API

The Community API provides access to StarCraft 2 community data.

```python
from blizzardapi2 import BlizzardApi
from blizzardapi2.starcraft2.starcraft2_community_api import Region, Locale

api_client = BlizzardApi("client_id", "client_secret")

# Get profile
profile = api_client.starcraft2.community.get_profile(
    Region.US,
    Locale.EN_US,
    "region_id",
    "realm_id",
    "profile_id"
)

# Get metadata
metadata = api_client.starcraft2.community.get_metadata(
    Region.US,
    Locale.EN_US,
    "region_id",
    "realm_id",
    "profile_id"
)

# Get profile ladder
profile_ladder = api_client.starcraft2.community.get_profile_ladder(
    Region.US,
    Locale.EN_US,
    "region_id",
    "realm_id",
    "profile_id",
    "ladder_id"
)

# Get grandmaster leaderboard
grandmaster = api_client.starcraft2.community.get_grandmaster_leaderboard(
    Region.US,
    Locale.EN_US,
    "region_id"
)

# Get season
season = api_client.starcraft2.community.get_season(
    Region.US,
    Locale.EN_US,
    "region_id"
)

# Get player account
player_account = api_client.starcraft2.community.get_player_account(
    Region.US,
    Locale.EN_US,
    "region_id",
    "realm_id",
    "profile_id"
)
```

### Game Data API

The Game Data API provides access to StarCraft 2 game data.

```python
# Get league data
league_data = api_client.starcraft2.game_data.get_league_data(
    Region.US,
    Locale.EN_US,
    "season_id",
    "queue_id",
    "team_type",
    "league_id"
)

# Get season
season = api_client.starcraft2.game_data.get_season(
    Region.US,
    Locale.EN_US
)

# Get player account
player_account = api_client.starcraft2.game_data.get_player_account(
    Region.US,
    Locale.EN_US,
    "region_id",
    "realm_id",
    "profile_id"
)

# Get profile
profile = api_client.starcraft2.game_data.get_profile(
    Region.US,
    Locale.EN_US,
    "region_id",
    "realm_id",
    "profile_id"
)

# Get profile ladder
profile_ladder = api_client.starcraft2.game_data.get_profile_ladder(
    Region.US,
    Locale.EN_US,
    "region_id",
    "realm_id",
    "profile_id",
    "ladder_id"
)

# Get grandmaster leaderboard
grandmaster = api_client.starcraft2.game_data.get_grandmaster_leaderboard(
    Region.US,
    Locale.EN_US,
    "region_id"
)
```

## Async Usage

All endpoints support async/await for better performance:

```python
import asyncio
from blizzardapi2 import BlizzardApi
from blizzardapi2.starcraft2.starcraft2_community_api import Region, Locale

async def main():
    api_client = BlizzardApi("client_id", "client_secret")

    # Get profile
    profile = await api_client.starcraft2.community.get_profile(
        Region.US,
        Locale.EN_US,
        "region_id",
        "realm_id",
        "profile_id"
    )

asyncio.run(main())
```

## Response Types

All API responses are returned as structured dataclasses with proper type hints. This provides better code completion and type checking in your IDE.

## Error Handling

The library includes comprehensive error handling for API responses. All errors are raised as exceptions with descriptive messages to help with debugging.
