"""Diablo III Community API client.

This module provides access to Diablo III community endpoints,
including profiles, heroes, and game data information.
"""

from typing import Any, Dict

from ..api import BaseApi
from ..types import Locale, Region


class ApiResponse:
    """Wrapper for API responses with metadata."""

    data: Dict[str, Any]
    region: Region
    locale: Locale
    namespace: str


class Diablo3CommunityApi(BaseApi):
    """Diablo 3 Community API client.

    This class provides access to the Diablo 3 Community API endpoints.
    """

    def __init__(self, client_id: str, client_secret: str) -> None:
        """Initialize the Diablo 3 Community API client.

        Args:
            client_id: The Blizzard API client ID.
            client_secret: The Blizzard API client secret.
        """
        super().__init__(client_id, client_secret)

    def get_act_index(self, region: Region, locale: Locale) -> Dict[str, Any]:
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
        return self.get_resource(resource, region, query_params)

    async def get_act_index_async(self, region: Region, locale: Locale) -> Dict[str, Any]:
        """Get an index of acts asynchronously.

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
        return await self.get_resource_async(resource, region, query_params)

    def get_act(self, region: Region, locale: Locale, act_id: int) -> Dict[str, Any]:
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
        return self.get_resource(resource, region, query_params)

    async def get_act_async(self, region: Region, locale: Locale, act_id: int) -> Dict[str, Any]:
        """Get a single act by ID asynchronously.

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
        return await self.get_resource_async(resource, region, query_params)

    def get_artisan(
        self, region: Region, locale: Locale, artisan_slug: str
    ) -> Dict[str, Any]:
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
        return self.get_resource(resource, region, query_params)

    async def get_artisan_async(
        self, region: Region, locale: Locale, artisan_slug: str
    ) -> Dict[str, Any]:
        """Get a single artisan by slug asynchronously.

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
        return await self.get_resource_async(resource, region, query_params)

    def get_recipe(
        self, region: Region, locale: Locale, artisan_slug: str, recipe_slug: str
    ) -> Dict[str, Any]:
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
        return self.get_resource(resource, region, query_params)

    async def get_recipe_async(
        self, region: Region, locale: Locale, artisan_slug: str, recipe_slug: str
    ) -> Dict[str, Any]:
        """Get a single recipe by slug for the specified artisan asynchronously.

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
        return await self.get_resource_async(resource, region, query_params)

    def get_follower(
        self, region: Region, locale: Locale, follower_slug: str
    ) -> Dict[str, Any]:
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
        return self.get_resource(resource, region, query_params)

    async def get_follower_async(
        self, region: Region, locale: Locale, follower_slug: str
    ) -> Dict[str, Any]:
        """Get a single follower by slug asynchronously.

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
        return await self.get_resource_async(resource, region, query_params)

    def get_character_class(
        self, region: Region, locale: Locale, class_slug: str
    ) -> Dict[str, Any]:
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
        return self.get_resource(resource, region, query_params)

    async def get_character_class_async(
        self, region: Region, locale: Locale, class_slug: str
    ) -> Dict[str, Any]:
        """Get a single character class by slug asynchronously.

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
        return await self.get_resource_async(resource, region, query_params)

    def get_api_skill(
        self, region: Region, locale: Locale, class_slug: str, skill_slug: str
    ) -> Dict[str, Any]:
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
        return self.get_resource(resource, region, query_params)

    async def get_api_skill_async(
        self, region: Region, locale: Locale, class_slug: str, skill_slug: str
    ) -> Dict[str, Any]:
        """Get a single skill by slug for a specific character class asynchronously.

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
        return await self.get_resource_async(resource, region, query_params)

    def get_item_type_index(self, region: Region, locale: Locale) -> Dict[str, Any]:
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
        return self.get_resource(resource, region, query_params)

    async def get_item_type_index_async(self, region: Region, locale: Locale) -> Dict[str, Any]:
        """Get an index of item types asynchronously.

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
        return await self.get_resource_async(resource, region, query_params)

    def get_item_type(
        self, region: Region, locale: Locale, item_type_slug: str
    ) -> Dict[str, Any]:
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
        return self.get_resource(resource, region, query_params)

    async def get_item_type_async(
        self, region: Region, locale: Locale, item_type_slug: str
    ) -> Dict[str, Any]:
        """Get a single item type by slug asynchronously.

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
        return await self.get_resource_async(resource, region, query_params)

    def get_item(
        self, region: Region, locale: Locale, item_slug_id: str
    ) -> Dict[str, Any]:
        """Get a single item by slug and ID.

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
        return self.get_resource(resource, region, query_params)

    async def get_item_async(
        self, region: Region, locale: Locale, item_slug_id: str
    ) -> Dict[str, Any]:
        """Get a single item by slug and ID asynchronously.

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
        return await self.get_resource_async(resource, region, query_params)

    def get_api_account(
        self, region: Region, locale: Locale, account_id: str
    ) -> Dict[str, Any]:
        """Get a career profile for a Diablo III account.

        Args:
            region: The region to query (e.g., "us", "eu").
            locale: The locale to use for the response (e.g., "en_US").
            account_id: The BattleTag of the account.

        Returns:
            A dictionary containing the career profile.

        Raises:
            ApiError: If the API request fails.
        """
        resource = f"/d3/profile/{account_id}"
        query_params = {"locale": locale}
        return self.get_resource(resource, region, query_params)

    async def get_api_account_async(
        self, region: Region, locale: Locale, account_id: str
    ) -> Dict[str, Any]:
        """Get a career profile for a Diablo III account asynchronously.

        Args:
            region: The region to query (e.g., "us", "eu").
            locale: The locale to use for the response (e.g., "en_US").
            account_id: The BattleTag of the account.

        Returns:
            A dictionary containing the career profile.

        Raises:
            ApiError: If the API request fails.
        """
        resource = f"/d3/profile/{account_id}"
        query_params = {"locale": locale}
        return await self.get_resource_async(resource, region, query_params)

    def get_api_hero(
        self, region: Region, locale: Locale, account_id: str, hero_id: int
    ) -> Dict[str, Any]:
        """Get a hero profile for a Diablo III character.

        Args:
            region: The region to query (e.g., "us", "eu").
            locale: The locale to use for the response (e.g., "en_US").
            account_id: The BattleTag of the account.
            hero_id: The ID of the hero.

        Returns:
            A dictionary containing the hero profile.

        Raises:
            ApiError: If the API request fails.
        """
        resource = f"/d3/profile/{account_id}/hero/{hero_id}"
        query_params = {"locale": locale}
        return self.get_resource(resource, region, query_params)

    async def get_api_hero_async(
        self, region: Region, locale: Locale, account_id: str, hero_id: int
    ) -> Dict[str, Any]:
        """Get a hero profile for a Diablo III character asynchronously.

        Args:
            region: The region to query (e.g., "us", "eu").
            locale: The locale to use for the response (e.g., "en_US").
            account_id: The BattleTag of the account.
            hero_id: The ID of the hero.

        Returns:
            A dictionary containing the hero profile.

        Raises:
            ApiError: If the API request fails.
        """
        resource = f"/d3/profile/{account_id}/hero/{hero_id}"
        query_params = {"locale": locale}
        return await self.get_resource_async(resource, region, query_params)

    def get_api_detailed_hero_items(
        self, region: Region, locale: Locale, account_id: str, hero_id: int
    ) -> Dict[str, Any]:
        """Get detailed item information for a hero.

        Args:
            region: The region to query (e.g., "us", "eu").
            locale: The locale to use for the response (e.g., "en_US").
            account_id: The BattleTag of the account.
            hero_id: The ID of the hero.

        Returns:
            A dictionary containing the detailed hero items.

        Raises:
            ApiError: If the API request fails.
        """
        resource = f"/d3/profile/{account_id}/hero/{hero_id}/items"
        query_params = {"locale": locale}
        return self.get_resource(resource, region, query_params)

    async def get_api_detailed_hero_items_async(
        self, region: Region, locale: Locale, account_id: str, hero_id: int
    ) -> Dict[str, Any]:
        """Get detailed item information for a hero asynchronously.

        Args:
            region: The region to query (e.g., "us", "eu").
            locale: The locale to use for the response (e.g., "en_US").
            account_id: The BattleTag of the account.
            hero_id: The ID of the hero.

        Returns:
            A dictionary containing the detailed hero items.

        Raises:
            ApiError: If the API request fails.
        """
        resource = f"/d3/profile/{account_id}/hero/{hero_id}/items"
        query_params = {"locale": locale}
        return await self.get_resource_async(resource, region, query_params)

    def get_api_detailed_follower_items(
        self, region: Region, locale: Locale, account_id: str, hero_id: int
    ) -> Dict[str, Any]:
        """Get detailed item information for a hero's followers.

        Args:
            region: The region to query (e.g., "us", "eu").
            locale: The locale to use for the response (e.g., "en_US").
            account_id: The BattleTag of the account.
            hero_id: The ID of the hero.

        Returns:
            A dictionary containing the detailed follower items.

        Raises:
            ApiError: If the API request fails.
        """
        resource = f"/d3/profile/{account_id}/hero/{hero_id}/follower-items"
        query_params = {"locale": locale}
        return self.get_resource(resource, region, query_params)

    async def get_api_detailed_follower_items_async(
        self, region: Region, locale: Locale, account_id: str, hero_id: int
    ) -> Dict[str, Any]:
        """Get detailed item information for a hero's followers asynchronously.

        Args:
            region: The region to query (e.g., "us", "eu").
            locale: The locale to use for the response (e.g., "en_US").
            account_id: The BattleTag of the account.
            hero_id: The ID of the hero.

        Returns:
            A dictionary containing the detailed follower items.

        Raises:
            ApiError: If the API request fails.
        """
        resource = f"/d3/profile/{account_id}/hero/{hero_id}/follower-items"
        query_params = {"locale": locale}
        return await self.get_resource_async(resource, region, query_params)

    def get_career_profile(
        self, region: Region, locale: Locale, account_id: str
    ) -> Dict[str, Any]:
        """Get a career profile for a Diablo III account.

        Args:
            region: The region to query (e.g., "us", "eu").
            locale: The locale to use for the response (e.g., "en_US").
            account_id: The BattleTag of the account.

        Returns:
            A dictionary containing the career profile.

        Raises:
            ApiError: If the API request fails.
        """
        return self.get_api_account(region, locale, account_id)

    async def get_career_profile_async(
        self, region: Region, locale: Locale, account_id: str
    ) -> Dict[str, Any]:
        """Get a career profile for a Diablo III account asynchronously.

        Args:
            region: The region to query (e.g., "us", "eu").
            locale: The locale to use for the response (e.g., "en_US").
            account_id: The BattleTag of the account.

        Returns:
            A dictionary containing the career profile.

        Raises:
            ApiError: If the API request fails.
        """
        return await self.get_api_account_async(region, locale, account_id)

    def get_hero_profile(
        self, region: Region, locale: Locale, account_id: str, hero_id: int
    ) -> Dict[str, Any]:
        """Get a hero profile for a Diablo III character.

        Args:
            region: The region to query (e.g., "us", "eu").
            locale: The locale to use for the response (e.g., "en_US").
            account_id: The BattleTag of the account.
            hero_id: The ID of the hero.

        Returns:
            A dictionary containing the hero profile.

        Raises:
            ApiError: If the API request fails.
        """
        return self.get_api_hero(region, locale, account_id, hero_id)

    async def get_hero_profile_async(
        self, region: Region, locale: Locale, account_id: str, hero_id: int
    ) -> Dict[str, Any]:
        """Get a hero profile for a Diablo III character asynchronously.

        Args:
            region: The region to query (e.g., "us", "eu").
            locale: The locale to use for the response (e.g., "en_US").
            account_id: The BattleTag of the account.
            hero_id: The ID of the hero.

        Returns:
            A dictionary containing the hero profile.

        Raises:
            ApiError: If the API request fails.
        """
        return await self.get_api_hero_async(region, locale, account_id, hero_id)

    def get_season_index(self, region: Region, locale: Locale) -> Dict[str, Any]:
        """Get the current season index.

        Args:
            region: The region to query (e.g., "us", "eu").
            locale: The locale to use for the response (e.g., "en_US").

        Returns:
            A dictionary containing the season index.

        Raises:
            ApiError: If the API request fails.
        """
        resource = "/d3/data/season"
        query_params = {"locale": locale}
        return self.get_resource(resource, region, query_params)

    async def get_season_index_async(self, region: Region, locale: Locale) -> Dict[str, Any]:
        """Get the current season index asynchronously.

        Args:
            region: The region to query (e.g., "us", "eu").
            locale: The locale to use for the response (e.g., "en_US").

        Returns:
            A dictionary containing the season index.

        Raises:
            ApiError: If the API request fails.
        """
        resource = "/d3/data/season"
        query_params = {"locale": locale}
        return await self.get_resource_async(resource, region, query_params)
