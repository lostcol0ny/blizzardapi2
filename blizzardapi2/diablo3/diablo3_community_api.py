from typing import Any

from ..api import BaseApi

"""diablo3_community_api.py file."""


class Diablo3CommunityApi(BaseApi):
    """All Diablo 3 Community API methods.

    Attributes:
        client_id (str): A string client ID supplied by Blizzard.
        client_secret (str): A string client secret supplied by Blizzard.
    """

    def __init__(self, client_id: str, client_secret: str) -> None:
        """
        Initialize the Diablo3CommunityApi class.

        Args:
            client_id (str): The client ID supplied by Blizzard.
            client_secret (str): The client secret supplied by Blizzard.
        """
        super().__init__(client_id, client_secret)

    def get_act_index(self, region: str, locale: str) -> dict[str, Any]:
        """
        Return an index of acts.

        Args:
            region (str): The region to query (e.g., "us", "eu").
            locale (str): The locale to use for the response.

        Returns:
            Dict[str, Any]: A dictionary containing the index of acts.
        """
        resource = "/d3/data/act"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_act(self, region: str, locale: str, act_id: int) -> dict[str, Any]:
        """
        Return a single act by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            act_id (int): The ID of the act to retrieve.

        Returns:
            Dict[str, Any]: A dictionary containing the act details.
        """
        resource = f"/d3/data/act/{act_id}"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_artisan(
        self, region: str, locale: str, artisan_slug: str
    ) -> dict[str, Any]:
        """
        Return a single artisan by slug.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            artisan_slug (str): The slug of the artisan to retrieve.

        Returns:
            Dict[str, Any]: A dictionary containing the artisan details.
        """
        resource = f"/d3/data/artisan/{artisan_slug}"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_recipe(
        self, region: str, locale: str, artisan_slug: str, recipe_slug: str
    ) -> dict[str, Any]:
        """
        Return a single recipe by slug for the specified artisan.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            artisan_slug (str): The slug of the artisan.
            recipe_slug (str): The slug of the recipe to retrieve.

        Returns:
            Dict[str, Any]: A dictionary containing the recipe details.
        """
        resource = f"/d3/data/artisan/{artisan_slug}/recipe/{recipe_slug}"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_follower(
        self, region: str, locale: str, follower_slug: str
    ) -> dict[str, Any]:
        """
        Return a single follower by slug.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            follower_slug (str): The slug of the follower to retrieve.

        Returns:
            Dict[str, Any]: A dictionary containing the follower details.
        """
        resource = f"/d3/data/follower/{follower_slug}"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_character_class(
        self, region: str, locale: str, class_slug: str
    ) -> dict[str, Any]:
        """
        Return a single character class by slug.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            class_slug (str): The slug of the character class to retrieve.

        Returns:
            Dict[str, Any]: A dictionary containing the character class details.
        """
        resource = f"/d3/data/hero/{class_slug}"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_api_skill(
        self, region: str, locale: str, class_slug: str, skill_slug: str
    ) -> dict[str, Any]:
        """
        Return a single skill by slug for a specific character class.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            class_slug (str): The slug of the character class.
            skill_slug (str): The slug of the skill to retrieve.

        Returns:
            Dict[str, Any]: A dictionary containing the skill details.
        """
        resource = f"/d3/data/hero/{class_slug}/skill/{skill_slug}"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_item_type_index(self, region: str, locale: str) -> dict[str, Any]:
        """
        Return an index of item types.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.

        Returns:
            Dict[str, Any]: A dictionary containing the index of item types.
        """
        resource = "/d3/data/item-type"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_item_type(
        self, region: str, locale: str, item_type_slug: str
    ) -> dict[str, Any]:
        """
        Return a single item type by slug.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            item_type_slug (str): The slug of the item type to retrieve.

        Returns:
            Dict[str, Any]: A dictionary containing the item type details.
        """
        resource = f"/d3/data/item-type/{item_type_slug}"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_item(self, region: str, locale: str, item_slug_id: str) -> dict[str, Any]:
        """
        Return a single item by item slug and ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            item_slug_id (str): The slug and ID of the item to retrieve.

        Returns:
            Dict[str, Any]: A dictionary containing the item details.
        """
        resource = f"/d3/data/item/{item_slug_id}"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_api_account(
        self, region: str, locale: str, account_id: str
    ) -> dict[str, Any]:
        """
        Return the specified account profile.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            account_id (str): The ID of the account to retrieve.

        Returns:
            Dict[str, Any]: A dictionary containing the account profile details.
        """
        resource = f"/d3/profile/{account_id}/"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_api_hero(
        self, region: str, locale: str, account_id: str, hero_id: int
    ) -> dict[str, Any]:
        """
        Return a single hero.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            account_id (str): The ID of the account.
            hero_id (int): The ID of the hero to retrieve.

        Returns:
            Dict[str, Any]: A dictionary containing the hero details.
        """
        resource = f"/d3/profile/{account_id}/hero/{hero_id}"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_api_detailed_hero_items(
        self, region: str, locale: str, account_id: str, hero_id: int
    ) -> dict[str, Any]:
        """
        Return a list of items for the specified hero.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            account_id (str): The ID of the account.
            hero_id (int): The ID of the hero.

        Returns:
            Dict[str, Any]: A dictionary containing the list of items for the hero.
        """
        resource = f"/d3/profile/{account_id}/hero/{hero_id}/items"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_api_detailed_follower_items(
        self, region: str, locale: str, account_id: str, hero_id: int
    ) -> dict[str, Any]:
        """
        Return a single item by item slug and ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            account_id (str): The ID of the account.
            hero_id (int): The ID of the hero.

        Returns:
            Dict[str, Any]: A dictionary containing the item details.
        """
        resource = f"/d3/profile/{account_id}/hero/{hero_id}/follower-items"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)
