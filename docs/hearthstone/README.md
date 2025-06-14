# Hearthstone API Documentation

This document provides information about the Hearthstone API endpoints available in the blizzardapi2 library.

## Available Endpoints

The Hearthstone API provides access to game data including cards, card backs, and metadata.

```python
from blizzardapi2 import BlizzardApi
from blizzardapi2.hearthstone.hearthstone_api import Region, Locale

api_client = BlizzardApi("client_id", "client_secret")

# Get card search
cards = api_client.hearthstone.game_data.get_cards(
    Region.US,
    Locale.EN_US,
    mana_cost=5,
    attack=5,
    health=5
)

# Get card by ID
card = api_client.hearthstone.game_data.get_card(
    Region.US,
    Locale.EN_US,
    "card_id"
)

# Get card backs
card_backs = api_client.hearthstone.game_data.get_card_backs(
    Region.US,
    Locale.EN_US
)

# Get card back by ID
card_back = api_client.hearthstone.game_data.get_card_back(
    Region.US,
    Locale.EN_US,
    "card_back_id"
)

# Get deck
deck = api_client.hearthstone.game_data.get_deck(
    Region.US,
    Locale.EN_US,
    "deck_code"
)

# Get metadata
metadata = api_client.hearthstone.game_data.get_metadata(
    Region.US,
    Locale.EN_US
)
```

## Async Usage

All endpoints support async/await for better performance:

```python
import asyncio
from blizzardapi2 import BlizzardApi
from blizzardapi2.hearthstone.hearthstone_api import Region, Locale

async def main():
    api_client = BlizzardApi("client_id", "client_secret")

    # Get card search
    cards = await api_client.hearthstone.game_data.get_cards(
        Region.US,
        Locale.EN_US,
        mana_cost=5,
        attack=5,
        health=5
    )

asyncio.run(main())
```

## Response Types

All API responses are returned as structured dataclasses with proper type hints. This provides better code completion and type checking in your IDE.

## Error Handling

The library includes comprehensive error handling for API responses. All errors are raised as exceptions with descriptive messages to help with debugging.
