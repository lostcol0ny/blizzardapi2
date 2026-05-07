from typing import Any

from ..api import LocaleApi
from ..types import OptionalLocale, OptionalRegion

"""diablo3_community_api.py file."""


class Diablo3CommunityApi(LocaleApi):
    """All Diablo 3 Community API methods.

    Attributes:
        client_id (str): A string client ID supplied by Blizzard.
        client_secret (str): A string client secret supplied by Blizzard.
        region (Region, optional): A default region to use for requests.
        locale (Locale, optional): A default locale to use for requests.
    """

    def get_act_index(
        self, *, region: OptionalRegion = None, locale: OptionalLocale = None
    ) -> dict[str, Any]:
        """
        Return an index of acts.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the index of acts.
        """
        resource = "/d3/data/act"
        return super().get_resource(resource, region, locale=locale)

    def get_act(
        self,
        act_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return a single act by ID.

        Args:
            act_id (int): The ID of the act to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the act details.
        """
        resource = f"/d3/data/act/{act_id}"
        return super().get_resource(resource, region, locale=locale)

    def get_artisan(
        self,
        artisan_slug: str,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return a single artisan by slug.

        Args:
            artisan_slug (str): The slug of the artisan to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the artisan details.
        """
        resource = f"/d3/data/artisan/{artisan_slug}"
        return super().get_resource(resource, region, locale=locale)

    def get_recipe(
        self,
        artisan_slug: str,
        recipe_slug: str,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return a single recipe by slug for the specified artisan.

        Args:
            artisan_slug (str): The slug of the artisan.
            recipe_slug (str): The slug of the recipe to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the recipe details.
        """
        resource = f"/d3/data/artisan/{artisan_slug}/recipe/{recipe_slug}"
        return super().get_resource(resource, region, locale=locale)

    def get_follower(
        self,
        follower_slug: str,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return a single follower by slug.

        Args:
            follower_slug (str): The slug of the follower to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the follower details.
        """
        resource = f"/d3/data/follower/{follower_slug}"
        return super().get_resource(resource, region, locale=locale)

    def get_character_class(
        self,
        class_slug: str,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return a single character class by slug.

        Args:
            class_slug (str): The slug of the character class to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the character class details.
        """
        resource = f"/d3/data/hero/{class_slug}"
        return super().get_resource(resource, region, locale=locale)

    def get_api_skill(
        self,
        class_slug: str,
        skill_slug: str,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return a single skill by slug for a specific character class.

        Args:
            class_slug (str): The slug of the character class.
            skill_slug (str): The slug of the skill to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the skill details.
        """
        resource = f"/d3/data/hero/{class_slug}/skill/{skill_slug}"
        return super().get_resource(resource, region, locale=locale)

    def get_item_type_index(
        self,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return an index of item types.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the index of item types.
        """
        resource = "/d3/data/item-type"
        return super().get_resource(resource, region, locale=locale)

    def get_item_type(
        self,
        item_type_slug: str,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return a single item type by slug.

        Args:
            item_type_slug (str): The slug of the item type to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the item type details.
        """
        resource = f"/d3/data/item-type/{item_type_slug}"
        return super().get_resource(resource, region, locale=locale)

    def get_item(
        self,
        item_slug_id: str,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return a single item by item slug and ID.

        Args:
            item_slug_id (str): The slug and ID of the item to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the item details.
        """
        resource = f"/d3/data/item/{item_slug_id}"
        return super().get_resource(resource, region, locale=locale)

    def get_api_account(
        self,
        account_id: str,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return the specified account profile.

        Args:
            account_id (str): The ID of the account to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the account profile details.
        """
        resource = f"/d3/profile/{account_id}/"
        return super().get_resource(resource, region, locale=locale)

    def get_api_hero(
        self,
        account_id: str,
        hero_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return a single hero.

        Args:
            account_id (str): The ID of the account.
            hero_id (int): The ID of the hero to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the hero details.
        """
        resource = f"/d3/profile/{account_id}/hero/{hero_id}"
        return super().get_resource(resource, region, locale=locale)

    def get_api_detailed_hero_items(
        self,
        account_id: str,
        hero_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return a list of items for the specified hero.

        Args:
            account_id (str): The ID of the account.
            hero_id (int): The ID of the hero.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the list of items for the hero.
        """
        resource = f"/d3/profile/{account_id}/hero/{hero_id}/items"
        return super().get_resource(resource, region, locale=locale)

    def get_api_detailed_follower_items(
        self,
        account_id: str,
        hero_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return the equipped follower items for a given hero.

        Args:
            account_id (str): The ID of the account.
            hero_id (int): The ID of the hero.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the follower items
                equipped on the specified hero.
        """
        resource = f"/d3/profile/{account_id}/hero/{hero_id}/follower-items"
        return super().get_resource(resource, region, locale=locale)
