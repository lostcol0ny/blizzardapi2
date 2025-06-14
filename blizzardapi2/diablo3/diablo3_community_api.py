"""Diablo III Community API client.

This module provides access to Diablo III community endpoints,
including profiles, heroes, and game data information.
"""

from typing import Any

from ..api import Api, Locale, Region


class Diablo3CommunityApi(Api):
    """Diablo III Community API client.

    This class provides access to Diablo III community data through the Blizzard API,
    including player profiles, hero information, and game data.

    Example:
        ```python
        # Synchronous usage
        api = Diablo3CommunityApi(client_id="your_id", client_secret="your_secret")
        profile = api.get_api_account("us", "en_US", "battletag")
        hero = api.get_api_hero("us", "en_US", "battletag", 12345)

        # Asynchronous usage
        async with Diablo3CommunityApi(client_id="your_id", client_secret="your_secret") as api:
            profile = await api.get_api_account("us", "en_US", "battletag")
            hero = await api.get_api_hero("us", "en_US", "battletag", 12345)
        ```

    Attributes:
        client_id: The Blizzard API client ID.
        client_secret: The Blizzard API client secret.
    """

    def __init__(self, client_id: str, client_secret: str) -> None:
        """Initialize the Diablo III Community API client.

        Args:
            client_id: The Blizzard API client ID.
            client_secret: The Blizzard API client secret.

        Raises:
            ValueError: If client_id or client_secret is empty.
        """
        if not client_id or not client_secret:
            raise ValueError("client_id and client_secret must not be empty")
        super().__init__(client_id, client_secret)

    def get_act_index(self, region: Region, locale: Locale) -> dict[str, Any]:
        """Get an index of acts.

        Args:
            region: The region to query (e.g., "us", "eu").
            locale: The locale to use for the response (e.g., "en_US").

        Returns:
            A dictionary containing the index of acts.

        Raises:
            ApiError: If the API request fails.
        """
        resource = "/d3/data/act"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_act(self, region: Region, locale: Locale, act_id: int) -> dict[str, Any]:
        """Get a single act by ID.

        Args:
            region: The region to query (e.g., "us", "eu").
            locale: The locale to use for the response (e.g., "en_US").
            act_id: The ID of the act to retrieve.

        Returns:
            A dictionary containing the act details.

        Raises:
            ApiError: If the API request fails.
        """
        resource = f"/d3/data/act/{act_id}"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_artisan(
        self, region: Region, locale: Locale, artisan_slug: str
    ) -> dict[str, Any]:
        """Get a single artisan by slug.

        Args:
            region: The region to query (e.g., "us", "eu").
            locale: The locale to use for the response (e.g., "en_US").
            artisan_slug: The slug of the artisan to retrieve.

        Returns:
            A dictionary containing the artisan details.

        Raises:
            ApiError: If the API request fails.
        """
        resource = f"/d3/data/artisan/{artisan_slug}"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_recipe(
        self, region: Region, locale: Locale, artisan_slug: str, recipe_slug: str
    ) -> dict[str, Any]:
        """Get a single recipe by slug for the specified artisan.

        Args:
            region: The region to query (e.g., "us", "eu").
            locale: The locale to use for the response (e.g., "en_US").
            artisan_slug: The slug of the artisan.
            recipe_slug: The slug of the recipe to retrieve.

        Returns:
            A dictionary containing the recipe details.

        Raises:
            ApiError: If the API request fails.
        """
        resource = f"/d3/data/artisan/{artisan_slug}/recipe/{recipe_slug}"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_follower(
        self, region: Region, locale: Locale, follower_slug: str
    ) -> dict[str, Any]:
        """Get a single follower by slug.

        Args:
            region: The region to query (e.g., "us", "eu").
            locale: The locale to use for the response (e.g., "en_US").
            follower_slug: The slug of the follower to retrieve.

        Returns:
            A dictionary containing the follower details.

        Raises:
            ApiError: If the API request fails.
        """
        resource = f"/d3/data/follower/{follower_slug}"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_character_class(
        self, region: Region, locale: Locale, class_slug: str
    ) -> dict[str, Any]:
        """Get a single character class by slug.

        Args:
            region: The region to query (e.g., "us", "eu").
            locale: The locale to use for the response (e.g., "en_US").
            class_slug: The slug of the character class to retrieve.

        Returns:
            A dictionary containing the character class details.

        Raises:
            ApiError: If the API request fails.
        """
        resource = f"/d3/data/hero/{class_slug}"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_api_skill(
        self, region: Region, locale: Locale, class_slug: str, skill_slug: str
    ) -> dict[str, Any]:
        """Get a single skill by slug for a specific character class.

        Args:
            region: The region to query (e.g., "us", "eu").
            locale: The locale to use for the response (e.g., "en_US").
            class_slug: The slug of the character class.
            skill_slug: The slug of the skill to retrieve.

        Returns:
            A dictionary containing the skill details.

        Raises:
            ApiError: If the API request fails.
        """
        resource = f"/d3/data/hero/{class_slug}/skill/{skill_slug}"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_item_type_index(self, region: Region, locale: Locale) -> dict[str, Any]:
        """Get an index of item types.

        Args:
            region: The region to query (e.g., "us", "eu").
            locale: The locale to use for the response (e.g., "en_US").

        Returns:
            A dictionary containing the index of item types.

        Raises:
            ApiError: If the API request fails.
        """
        resource = "/d3/data/item-type"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_item_type(
        self, region: Region, locale: Locale, item_type_slug: str
    ) -> dict[str, Any]:
        """Get a single item type by slug.

        Args:
            region: The region to query (e.g., "us", "eu").
            locale: The locale to use for the response (e.g., "en_US").
            item_type_slug: The slug of the item type to retrieve.

        Returns:
            A dictionary containing the item type details.

        Raises:
            ApiError: If the API request fails.
        """
        resource = f"/d3/data/item-type/{item_type_slug}"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_item(self, region: Region, locale: Locale, item_slug_id: str) -> dict[str, Any]:
        """Get a single item by item slug and ID.

        Args:
            region: The region to query (e.g., "us", "eu").
            locale: The locale to use for the response (e.g., "en_US").
            item_slug_id: The slug and ID of the item to retrieve.

        Returns:
            A dictionary containing the item details.

        Raises:
            ApiError: If the API request fails.
        """
        resource = f"/d3/data/item/{item_slug_id}"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_api_account(
        self, region: Region, locale: Locale, account_id: str
    ) -> dict[str, Any]:
        """Get the specified account profile.

        Args:
            region: The region to query (e.g., "us", "eu").
            locale: The locale to use for the response (e.g., "en_US").
            account_id: The ID of the account to retrieve.

        Returns:
            A dictionary containing the account profile details.

        Raises:
            ApiError: If the API request fails.
        """
        resource = f"/d3/profile/{account_id}/"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_api_hero(
        self, region: Region, locale: Locale, account_id: str, hero_id: int
    ) -> dict[str, Any]:
        """Get a single hero.

        Args:
            region: The region to query (e.g., "us", "eu").
            locale: The locale to use for the response (e.g., "en_US").
            account_id: The ID of the account.
            hero_id: The ID of the hero to retrieve.

        Returns:
            A dictionary containing the hero details.

        Raises:
            ApiError: If the API request fails.
        """
        resource = f"/d3/profile/{account_id}/hero/{hero_id}"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_api_detailed_hero_items(
        self, region: Region, locale: Locale, account_id: str, hero_id: int
    ) -> dict[str, Any]:
        """Get a list of items for the specified hero.

        Args:
            region: The region to query (e.g., "us", "eu").
            locale: The locale to use for the response (e.g., "en_US").
            account_id: The ID of the account.
            hero_id: The ID of the hero.

        Returns:
            A dictionary containing the list of items for the hero.

        Raises:
            ApiError: If the API request fails.
        """
        resource = f"/d3/profile/{account_id}/hero/{hero_id}/items"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_api_detailed_follower_items(
        self, region: Region, locale: Locale, account_id: str, hero_id: int
    ) -> dict[str, Any]:
        """Get a list of items for the specified hero's followers.

        Args:
            region: The region to query (e.g., "us", "eu").
            locale: The locale to use for the response (e.g., "en_US").
            account_id: The ID of the account.
            hero_id: The ID of the hero.

        Returns:
            A dictionary containing the list of items for the hero's followers.

        Raises:
            ApiError: If the API request fails.
        """
        resource = f"/d3/profile/{account_id}/hero/{hero_id}/follower-items"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)
