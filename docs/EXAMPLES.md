
# Examples Of How To Enhance the `blizzardapi2` API

## Caching Requests for Static Data

You can add caching of requests through the `blizzardapi2` API by using the optional `session` parameter during API object creation.

Simply sub-class `requests.Session` and override the `get()` and `request()` methods to handle static resource requests.  For example:

```python
import requests
from cachecontrol import CacheControl

from blizzardapi2 import BlizzardApi

# Create a custom Session class that uses CacheControl for caching GET requests to static namespaces
class MySession(requests.Session):
    def __init__(self):
        super().__init__()
        self._cache = CacheControl(
            requests.Session(),
        )

    def get(self, url, **kwargs):
        # Use the cached session when requesting static namespace resources, otherwise use the normal session
        _namespace: str = kwargs.get("params", {}).get("namespace", "") or kwargs.get(
            "headers", {}
        ).get("Battlenet-Namespace", "")
        return (
            self._cache.get(url, **kwargs)
            if _namespace.startswith("static")
            else super().get(url, **kwargs)
        )

    def request(self, method, url, **kwargs):
        # Override the request method to route GET requests through the cache and others through the normal flow
        return (
            self.get(url, **kwargs)
            if method.upper() == "GET"
            else super().request(method, url, **kwargs)
        )


api_client = BlizzardApi("client_id", "client_secret", session=MySession())
```

See [examples/custom_session.py](../examples/custom_session.py) for a fully functional example.

You caching strategy can be as simple or complex as you wish.  Just remember that both index and dynamic objects change over time, so may not be good candidates for cacheing.

## Creating an OAUTH token for requests that require the OAuth Authorization Code flow

Blizzard requires a custom token for any access to the following API end-points:

| Resource path | API call |
| ------------- | -------- |
| /userinfo | `.battlenet.oauth.get_user_info(access_token)` |
| /profile/user/wow | `.wow.profile.get_account_profile_summary(access_token)` |
| /profile/user/wow/protected-character/{realm-id}-{character-id} | `.wow.profile.get_protected_character_profile_summary(access_token, realm_id, character_id)` |
| /profile/user/wow/collections | `.wow.profile.get_account_collections_index(access_token)` |
| /profile/user/wow/collections/heirlooms | `.wow.profile.get_account_heirlooms_collection_summary(access_token)` |
| /profile/user/wow/collections/mounts | `.wow.profile.get_account_mounts_collection_summary(access_token)` |
| /profile/user/wow/collections/pets | `.wow.profile.get_account_pets_collection_summary(access_token)` |
| /profile/user/wow/collections/toys | `.wow.profile.get_account_toys_collection_summary(access_token)` |
| /profile/user/wow/collections/transmogs | `.wow.profile.get_account_transmog_collection_summary(access_token)` |


Other than accepting `access_string` in the above methods, `blizzardapi2` doesn't support the OAuth Authorization Code flow as it requires both a client (web browser) and server to complete the protocol.

However, creating a simple server to personal use isn't complicated.  You can find an example server in [examples/oauth_server.py](../examples/oauth_server.py)

**Note:** while the code in `examples/oauth_server.py` uses `Flask`, any webserver framework that supports routes will work just as well.

Some things to remember:
* Make sure you register your full redirection URI as part of your battle.net client configuration.  Otherwise the post-authentication redirection will fail.
* Make sure your oauth server saves the token produced by OAuth Authorization Code flow somewhere permanent.  `blizzardapi2` still requires you to pass that value explicitly.
