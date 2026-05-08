# Battle.net API Documentation

This document provides information about the Battle.net API endpoints available in the blizzardapi2 library.

## Available Endpoints

The Battle.net API provides access to user profile data and OAuth functionality.

```python
from blizzardapi2 import BlizzardApi, Region, Locale

api_client = BlizzardApi("client_id", "client_secret")

# Get user info
user_info = api_client.battlenet.get_user_info(
    "access_token",
    region=Region.US,
    region=Locale.EN_US
)

# Get user profile
user_profile = api_client.battlenet.get_user_profile(
    "access_token",
    region=Region.US,
    region=Locale.EN_US
)

# Get user profile status
user_profile_status = api_client.battlenet.get_user_profile_status(
    "access_token",
    region=Region.US,
    region=Locale.EN_US
)
```

## OAuth Flow

The library supports the OAuth authorization code flow for accessing protected endpoints. Here's how to use it:

```python
from blizzardapi2 import BlizzardApi, Region, Locale

api_client = BlizzardApi("client_id", "client_secret")

# Get authorization URL
auth_url = api_client.battlenet.get_authorization_url(
    "redirect_uri",
    "scope",
    region=Region.US
)

# Exchange authorization code for access token
access_token = api_client.battlenet.get_access_token(
    "authorization_code",
    "redirect_uri",
    region=Region.US
)

# Refresh access token
new_access_token = api_client.battlenet.refresh_access_token(
    "refresh_token",
    region=Region.US
)
```

### Default Region & Locale Values

You can also specify a default `Region` and `Locale` the API should use.

```python
from blizzardapi2 import BlizzardApi, Region, Locale

api_client = BlizzardApi("client_id", "client_secret", region=Region.US, region=Locale.EN_US)

# Get user info
user_info = api_client.battlenet.get_user_info("access_token")

# Refresh access token
new_access_token = api_client.battlenet.refresh_access_token("refresh_token")
```

## Async Usage

All endpoints support async/await for better performance:

```python
import asyncio
from blizzardapi2 import BlizzardApi, Region, Locale

async def main():
    api_client = BlizzardApi("client_id", "client_secret")

    # Get user info
    user_info = await api_client.battlenet.get_user_info(
        "access_token",
        region=Region.US,
        region=Locale.EN_US
    )

asyncio.run(main())
```

## Response Types

All API responses are returned as structured dataclasses with proper type hints. This provides better code completion and type checking in your IDE.

## Error Handling

The library includes comprehensive error handling for API responses. All errors are raised as exceptions with descriptive messages to help with debugging.
