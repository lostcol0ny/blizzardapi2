# StarCraft 2 API Documentation

This document provides information about the StarCraft 2 API endpoints available in the blizzardapi2 library.

## Available Endpoints

### Community API

The Community API provides access to StarCraft 2 community data.

```python
from blizzardapi2 import BlizzardApi, Region, Locale

api_client = BlizzardApi("client_id", "client_secret")

# Get profile
profile = api_client.starcraft2.community.get_profile(
    "region_id",
    "realm_id",
    "profile_id",
    region=Region.US,
    region=Locale.EN_US
)

# Get metadata
metadata = api_client.starcraft2.community.get_metadata(
    "region_id",
    "realm_id",
    "profile_id",
    region=Region.US,
    region=Locale.EN_US
)

# Get profile ladder
profile_ladder = api_client.starcraft2.community.get_profile_ladder(
    "region_id",
    "realm_id",
    "profile_id",
    "ladder_id",
    region=Region.US,
    region=Locale.EN_US
)

# Get grandmaster leaderboard
grandmaster = api_client.starcraft2.community.get_grandmaster_leaderboard(
    "region_id",
    region=Region.US,
    region=Locale.EN_US
)

# Get season
season = api_client.starcraft2.community.get_season(
    "region_id",
    region=Region.US,
    region=Locale.EN_US
)

# Get player account
player_account = api_client.starcraft2.community.get_player_account(
    "region_id",
    "realm_id",
    "profile_id",
    region=Region.US,
    region=Locale.EN_US
)
```

### Game Data API

The Game Data API provides access to StarCraft 2 game data.

```python
# Get league data
league_data = api_client.starcraft2.game_data.get_league_data(
    "season_id",
    "queue_id",
    "team_type",
    "league_id",
    region=Region.US,
    region=Locale.EN_US
)

# Get season
season = api_client.starcraft2.game_data.get_season(
    Region.US,
    Locale.EN_US,
    region=Region.US,
    region=Locale.EN_US
)

# Get player account
player_account = api_client.starcraft2.game_data.get_player_account(
    Region.US,
    Locale.EN_US,
    "region_id",
    "realm_id",
    "profile_id",
    region=Region.US,
    region=Locale.EN_US
)

# Get profile
profile = api_client.starcraft2.game_data.get_profile(
    Region.US,
    Locale.EN_US,
    "region_id",
    "realm_id",
    "profile_id",
    region=Region.US,
    region=Locale.EN_US
)

# Get profile ladder
profile_ladder = api_client.starcraft2.game_data.get_profile_ladder(
    "region_id",
    "realm_id",
    "profile_id",
    "ladder_id",
    region=Region.US,
    region=Locale.EN_US
)

# Get grandmaster leaderboard
grandmaster = api_client.starcraft2.game_data.get_grandmaster_leaderboard(
    "region_id",
    region=Region.US,
    region=Locale.EN_US
)
```

### Default Region & Locale Values

You can also specify a default `Region` and `Locale` the API should use.

```python
from blizzardapi2 import BlizzardApi, Region, Locale

api_client = BlizzardApi("client_id", "client_secret", region=Region.US, region=Locale.EN_US)

# Get profile
profile = api_client.starcraft2.community.get_profile(
    "region_id",
    "realm_id",
    "profile_id"
)

# Get grandmaster leaderboard
grandmaster = api_client.starcraft2.game_data.get_grandmaster_leaderboard("region_id")
```

And then selectively override those values when necessary

```python
# Get profile
profile = api_client.starcraft2.community.get_profile(
    "region_id",
    "realm_id",
    "profile_id",
    region=Region.EU
)

# Get grandmaster leaderboard
grandmaster = api_client.starcraft2.game_data.get_grandmaster_leaderboard(
    "region_id",
    locale=Locale.ES_MX
)
```

## Async Usage

All endpoints support async/await for better performance:

```python
import asyncio
from blizzardapi2 import BlizzardApi, Region, Locale

async def main():
    api_client = BlizzardApi("client_id", "client_secret")

    # Get profile
    profile = await api_client.starcraft2.community.get_profile(
        "region_id",
        "realm_id",
        "profile_id",
        region=Region.US,
        region=Locale.EN_US
    )

asyncio.run(main())
```

## Response Types

All API responses are returned as structured dataclasses with proper type hints. This provides better code completion and type checking in your IDE.

## Error Handling

The library includes comprehensive error handling for API responses. All errors are raised as exceptions with descriptive messages to help with debugging.
