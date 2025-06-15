# Battle.net API Documentation

This document provides information about the Battle.net API endpoints available in the blizzardapi2 library.

## Available Endpoints

The Battle.net API provides access to user profile data and OAuth functionality.

```python
from blizzardapi2 import BlizzardApi
from blizzardapi2.battlenet.battlenet_api import Region, Locale

api_client = BlizzardApi("client_id", "client_secret")

# Get user info
user_info = api_client.battlenet.get_user_info(
    Region.US,
    Locale.EN_US,
    "access_token"
)

# Get user profile
user_profile = api_client.battlenet.get_user_profile(
    Region.US,
    Locale.EN_US,
    "access_token"
)

# Get user profile status
user_profile_status = api_client.battlenet.get_user_profile_status(
    Region.US,
    Locale.EN_US,
    "access_token"
)
```

## OAuth Flow

The library supports the OAuth authorization code flow for accessing protected endpoints. Here's how to use it:

```python
from blizzardapi2 import BlizzardApi
from blizzardapi2.battlenet.battlenet_api import Region, Locale

api_client = BlizzardApi("client_id", "client_secret")

# Get authorization URL
auth_url = api_client.battlenet.get_authorization_url(
    Region.US,
    "redirect_uri",
    "scope"
)

# Exchange authorization code for access token
access_token = api_client.battlenet.get_access_token(
    Region.US,
    "authorization_code",
    "redirect_uri"
)

# Refresh access token
new_access_token = api_client.battlenet.refresh_access_token(
    Region.US,
    "refresh_token"
)
```

## Async Usage

All endpoints support async/await for better performance:

```python
import asyncio
from blizzardapi2 import BlizzardApi
from blizzardapi2.battlenet.battlenet_api import Region, Locale

async def main():
    api_client = BlizzardApi("client_id", "client_secret")

    # Get user info
    user_info = await api_client.battlenet.get_user_info(
        Region.US,
        Locale.EN_US,
        "access_token"
    )

asyncio.run(main())
```

## Response Types

All API responses are returned as structured dataclasses with proper type hints. This provides better code completion and type checking in your IDE.

## Error Handling

The library includes comprehensive error handling for API responses. All errors are raised as exceptions with descriptive messages to help with debugging.
