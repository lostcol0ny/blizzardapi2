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
from blizzardapi2 import BlizzardApi
from blizzardapi2.wow.wow_profile_api import Region, Locale

api_client = BlizzardApi("client_id", "client_secret")

# Get character profile
profile = api_client.wow.profile.get_character_profile_summary(
    Region.US,
    Locale.EN_US,
    "realm-slug",
    "character-name"
)

# Get achievement categories
achievements = api_client.wow.game_data.get_achievement_categories_index(
    Region.US,
    Locale.EN_US
)
```

### Async Usage

```python
import asyncio
from blizzardapi2 import BlizzardApi
from blizzardapi2.wow.wow_profile_api import Region, Locale

async def main():
    api_client = BlizzardApi("client_id", "client_secret")

    # Get character data
    profile = await api_client.wow.profile.get_character_profile_summary(
        Region.US,
        Locale.EN_US,
        "realm-slug",
        "character-name"
    )

    # Get multiple character collections concurrently
    tasks = [
        api_client.wow.profile.get_character_mounts_collection_summary(
            Region.US,
            Locale.EN_US,
            "realm-slug",
            "character-name"
        ),
        api_client.wow.profile.get_character_pets_collection_summary(
            Region.US,
            Locale.EN_US,
            "realm-slug",
            "character-name"
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

The API uses dataclasses for structured responses:

```python
@dataclass
class CharacterProfileResponse:
    data: dict[str, Any]
    status_code: int
    headers: dict[str, str]
    character_name: str
    realm_slug: str
    region: str
    locale: str
```

## Error Handling

The API includes comprehensive error handling for:

- Invalid regions/locales
- API rate limits
- Authentication errors
- Network issues
- Invalid responses

## Best Practices

1. Use async methods for better performance
2. Use enums for regions and locales to prevent errors
3. Handle API rate limits appropriately
4. Cache responses when possible
5. Use concurrent requests for multiple API calls
