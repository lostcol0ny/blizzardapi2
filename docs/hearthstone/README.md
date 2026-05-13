# Hearthstone API Documentation

This document provides information about the Hearthstone API endpoints available in the blizzardapi2 library.

## Available Endpoints

The Hearthstone API provides access to game data including cards, card backs, and metadata.

```python
from blizzardapi2 import BlizzardApi, Region, Locale

api_client = BlizzardApi("client_id", "client_secret")

# Get card search
cards = api_client.hearthstone.game_data.get_cards(
    mana_cost=5,
    attack=5,
    health=5,
    region=Region.US,
    locale=Locale.EN_US
)

# Get card by ID
card = api_client.hearthstone.game_data.get_card(
    "card_id",
    region=Region.US,
    locale=Locale.EN_US
)

# Get card backs
card_backs = api_client.hearthstone.game_data.get_card_backs(
    region=Region.US,
    locale=Locale.EN_US
)

# Get card back by ID
card_back = api_client.hearthstone.game_data.get_card_back(
    "card_back_id",
    region=Region.US,
    locale=Locale.EN_US
)

# Get deck
deck = api_client.hearthstone.game_data.get_deck(
    "deck_code",
    region=Region.US,
    locale=Locale.EN_US
)

# Get metadata
metadata = api_client.hearthstone.game_data.get_metadata(
    region=Region.US,
    locale=Locale.EN_US
)
```

### Default Region & Locale Values

You can also specify a default `Region` and `Locale` the API should use.

```python
from blizzardapi2 import BlizzardApi, Region, Locale

api_client = BlizzardApi("client_id", "client_secret", region=Region.US, locale=Locale.EN_US)

# Get card search
cards = api_client.hearthstone.game_data.get_cards(
    mana_cost=5,
    attack=5,
    health=5
)
```

And then selectively override those values when necessary

```python
# Get card search
cards = api_client.hearthstone.game_data.get_cards(
    mana_cost=5,
    attack=5,
    health=5,
    region=Region.EU
)

# Get card search
cards = api_client.hearthstone.game_data.get_cards(
    mana_cost=5,
    attack=5,
    health=5,
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

    # Get card search
    cards = await api_client.hearthstone.game_data.get_cards(
        mana_cost=5,
        attack=5,
        health=5,
        region=Region.US,
        locale=Locale.EN_US
    )

asyncio.run(main())
```

## Response Types

All API responses are returned as structured dataclasses with proper type hints. This provides better code completion and type checking in your IDE.

## Error Handling

The library includes comprehensive error handling for API responses. All errors are raised as exceptions with descriptive messages to help with debugging.
