# World of Warcraft API

This module provides access to the World of Warcraft API endpoints, including both Profile and Game Data APIs.

## Features

- Full async support for all endpoints
- Type-safe region and locale handling using enums
- Structured response types using dataclasses
- Support for both retail and classic WoW
- Comprehensive error handling

## API Categories

### Profile API

The Profile API provides access to character and account data. It includes:

- Account profile information
- Character profiles and statistics
- Collections (mounts, pets, toys, etc.)
- Achievements and statistics
- Equipment and appearance
- Professions and specializations

### Game Data API

The Game Data API provides access to game data such as:

- Achievements
- Azerite Essences
- Connected Realms
- Items
- Mounts
- Pets
- Professions
- Realms
- Specializations
- And more...

## Usage Examples

### Basic Usage

```python
from blizzardapi2 import BlizzardApi, Region, Locale

api_client = BlizzardApi("client_id", "client_secret")

# Get character profile
profile = api_client.wow.profile.get_character_profile_summary(
    "realm-slug",
    "character-name",
    region=Region.US,
    locale=Locale.EN_US
)

# Get achievement categories
achievements = api_client.wow.game_data.get_achievement_categories_index(
    region=Region.US,
    locale=Locale.EN_US
)
```

### Default Region & Locale Values

You can also specify a default `Region` and `Locale` the API should use.

```python
from blizzardapi2 import BlizzardApi, Region, Locale

api_client = BlizzardApi("client_id", "client_secret", region=Region.US, locale=Locale.EN_US)

# Get character profile
profile = api_client.wow.profile.get_character_profile_summary(
    "realm-slug",
    "character-name"
)

# Get achievement categories
achievements = api_client.wow.game_data.get_achievement_categories_index()
```

And then selectively override those values when necessary

```python
# Get character profile
profile = api_client.wow.profile.get_character_profile_summary(
    "realm-slug",
    "character-name",
    region=Region.EU
)

# Get achievement categories
achievements = api_client.wow.game_data.get_achievement_categories_index(
    locale=Locale.ES_MX
)
```

### Async Usage

```python
import asyncio
from blizzardapi2 import BlizzardApi, Region, Locale

async def main():
    api_client = BlizzardApi("client_id", "client_secret")

    # Get character data
    profile = await api_client.wow.profile.get_character_profile_summary(
        "realm-slug",
        "character-name",
        region=Region.US,
        locale=Locale.EN_US,
    )

    # Get multiple character collections concurrently
    tasks = [
        api_client.wow.profile.get_character_mounts_collection_summary(
            "realm-slug",
            "character-name",
            region=Region.US,
            locale=Locale.EN_US
        ),
        api_client.wow.profile.get_character_pets_collection_summary(
            "realm-slug",
            "character-name",
            region=Region.US,
            locale=Locale.EN_US
        )
    ]
    collections = await asyncio.gather(*tasks)

asyncio.run(main())
```

## Protected Endpoints

Some endpoints require OAuth authentication. These include:

- Account profile information
- Protected character data
- Collections data

For these endpoints, you'll need to provide an access token obtained through OAuth authorization.

## Response Types

All API responses are returned as structured dataclasses with proper type hints. This provides better code completion and type checking in your IDE.

## Error Handling

The library includes comprehensive error handling for API responses. All errors are raised as exceptions with descriptive messages to help with debugging.
