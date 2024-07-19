from typing import Dict, Any
from ..api import Api

"""diablo3_community_api.py file."""


class Diablo3CommunityApi(Api):
    """All Diablo 3 Community API methods.

    Attributes:
        client_id: A string client id supplied by Blizzard.
        client_secret: A string client secret supplied by Blizzard.
    """

    def __init__(self, client_id: str, client_secret: str) -> None:
        """Init Diablo3CommunityApi."""
        super().__init__(client_id, client_secret)

    # D3 Act API

    def get_act_index(self, region: str, locale: str) -> Dict[str, Any]:
        """Return an index of acts."""
        resource = "/d3/data/act"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_act(self, region: str, locale: str, act_id: int) -> Dict[str, Any]:
        """Return a single act by ID."""
        resource = f"/d3/data/act/{act_id}"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    # D3 Artisan and Recipe API

    def get_artisan(
        self, region: str, locale: str, artisan_slug: str
    ) -> Dict[str, Any]:
        """Return a single artisan by slug."""
        resource = f"/d3/data/artisan/{artisan_slug}"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_recipe(
        self, region: str, locale: str, artisan_slug: str, recipe_slug: str
    ) -> Dict[str, Any]:
        """Return a single recipe by slug for the specified artisan."""
        resource = f"/d3/data/artisan/{artisan_slug}/recipe/{recipe_slug}"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    # D3 Follower API

    def get_follower(
        self, region: str, locale: str, follower_slug: str
    ) -> Dict[str, Any]:
        """Return a single follower by slug."""
        resource = f"/d3/data/follower/{follower_slug}"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    # D3 Character Class and Skill API

    def get_character_class(
        self, region: str, locale: str, class_slug: str
    ) -> Dict[str, Any]:
        """Return a single character class by slug."""
        resource = f"/d3/data/hero/{class_slug}"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_api_skill(
        self, region: str, locale: str, class_slug: str, skill_slug: str
    ) -> Dict[str, Any]:
        """Return a single skill by slug for a specific character class."""
        resource = f"/d3/data/hero/{class_slug}/skill/{skill_slug}"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    # D3 Item Type API

    def get_item_type_index(self, region: str, locale: str) -> Dict[str, Any]:
        """Return an index of item types."""
        resource = "/d3/data/item-type"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_item_type(
        self, region: str, locale: str, item_type_slug: str
    ) -> Dict[str, Any]:
        """Return a single item type by slug."""
        resource = f"/d3/data/item-type/{item_type_slug}"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    # D3 Item API

    def get_item(self, region: str, locale: str, item_slug_id: str) -> Dict[str, Any]:
        """Return a single item by item slug and ID."""
        resource = f"/d3/data/item/{item_slug_id}"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    # D3 Profile API

    def get_api_account(
        self, region: str, locale: str, account_id: str
    ) -> Dict[str, Any]:
        """Return the specified account profile."""
        resource = f"/d3/profile/{account_id}/"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_api_hero(
        self, region: str, locale: str, account_id: str, hero_id: int
    ) -> Dict[str, Any]:
        """Return a single hero."""
        resource = f"/d3/profile/{account_id}/hero/{hero_id}"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_api_detailed_hero_items(
        self, region: str, locale: str, account_id: str, hero_id: int
    ) -> Dict[str, Any]:
        """Return a list of items for the specified hero."""
        resource = f"/d3/profile/{account_id}/hero/{hero_id}/items"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_api_detailed_follower_items(
        self, region: str, locale: str, account_id: str, hero_id: int
    ) -> Dict[str, Any]:
        """Return a single item by item slug and ID."""
        resource = f"/d3/profile/{account_id}/hero/{hero_id}/follower-items"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)
