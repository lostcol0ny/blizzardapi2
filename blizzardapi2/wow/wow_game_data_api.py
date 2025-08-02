"""wow_game_data_api.py file."""

from typing import Any

from ..api import BaseApi


class WowGameDataApi(BaseApi):
    """All Wow Game Data API methods.

    Attributes:
        client_id (str): A string client ID supplied by Blizzard.
        client_secret (str): A string client secret supplied by Blizzard.
    """

    def __init__(self, client_id: str, client_secret: str) -> None:
        """
        Initialize the WowGameDataApi class.

        Args:
            client_id (str): The client ID supplied by Blizzard.
            client_secret (str): The client secret supplied by Blizzard.
        """
        super().__init__(client_id, client_secret)

    # Achievement API

    def get_achievements_index(self, region: str, locale: str) -> dict[str, Any]:
        """
        Return an index of achievements.

        Args:
            region (str): The region to query (e.g., "us", "eu").
            locale (str): The locale to use for the response.

        Returns:
            Dict[str, Any]: A dictionary containing the index of achievements.
        """
        resource = "/data/wow/achievement/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_achievement(
        self, region: str, locale: str, achievement_id: int
    ) -> dict[str, Any]:
        """
        Return an achievement by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            achievement_id (int): The ID of the achievement to retrieve.

        Returns:
            Dict[str, Any]: A dictionary containing the achievement details.
        """
        resource = f"/data/wow/achievement/{achievement_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_achievement_categories_index(
        self, region: str, locale: str
    ) -> dict[str, Any]:
        """
        Return an index of achievement categories.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.

        Returns:
            Dict[str, Any]: A dictionary containing the index of achievement categories.
        """
        resource = "/data/wow/achievement-category/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_achievement_category(
        self, region: str, locale: str, achievement_category_id: int
    ) -> dict[str, Any]:
        """
        Return an achievement category by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            achievement_category_id (int): The ID of the achievement category to retrieve.

        Returns:
            Dict[str, Any]: A dictionary containing the achievement category details.
        """
        resource = f"/data/wow/achievement-category/{achievement_category_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_achievement_media(
        self, region: str, locale: str, achievement_id: int
    ) -> dict[str, Any]:
        """
        Return media for an achievement by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            achievement_id (int): The ID of the achievement to retrieve media for.

        Returns:
            Dict[str, Any]: A dictionary containing the achievement media.
        """
        resource = f"/data/wow/media/achievement/{achievement_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

        # Auction House API

    def get_auction_house_index(
        self, region: str, locale: str, connected_realm_id: int
    ) -> dict[str, Any]:
        """
        Return an index of auction houses for a connected realm.

        *CLASSIC ONLY*

        Args:
            region (str): The region to query (e.g., "us", "eu").
            locale (str): The locale to use for the response.
            connected_realm_id (int): The ID of the connected realm.

        Returns:
            Dict[str, Any]: A dictionary containing the auction house index for the connected realm.
        """
        resource = f"/data/wow/connected-realm/{connected_realm_id}/auctions/index"
        query_params = {"namespace": f"dynamic-classic-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_auctions_for_auction_house(
        self, region: str, locale: str, connected_realm_id: int, auction_house_id: int
    ) -> dict[str, Any]:
        """
        Return all active auctions for a specific auction house on a connected realm.

        *CLASSIC ONLY*

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            connected_realm_id (int): The ID of the connected realm.
            auction_house_id (int): The ID of the auction house.

        Returns:
            Dict[str, Any]: A dictionary containing the active auctions for the specified auction house.
        """
        resource = f"/data/wow/connected-realm/{connected_realm_id}/auctions/{auction_house_id}"
        query_params = {"namespace": f"dynamic-classic-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_auctions(
        self, region: str, locale: str, connected_realm_id: int
    ) -> dict[str, Any]:
        """
        Return all active auctions for a connected realm.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            connected_realm_id (int): The ID of the connected realm.

        Returns:
            Dict[str, Any]: A dictionary containing the active auctions for the connected realm.
        """
        resource = f"/data/wow/connected-realm/{connected_realm_id}/auctions"
        query_params = {"namespace": f"dynamic-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_commodities(self, region: str, locale: str) -> dict[str, Any]:
        """
        Return all active auctions for commodity items for the entire game region.

        Auction house data updates at a set interval. The value was initially set at 1 hour;
        however, it might change over time without notice. Depending on the number of active auctions
        on the specified connected realm, the response from this endpoint may be rather large,
        sometimes exceeding 10 MB.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.

        Returns:
            Dict[str, Any]: A dictionary containing all active auctions for commodity items.
        """
        resource = "/data/wow/auctions/commodities"
        query_params = {"namespace": f"dynamic-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

        # Azerite Essence API

    def get_azerite_essences_index(self, region: str, locale: str) -> dict[str, Any]:
        """
        Return an index of Azerite essences.

        Args:
            region (str): The region to query (e.g., "us", "eu").
            locale (str): The locale to use for the response.

        Returns:
            Dict[str, Any]: A dictionary containing the index of Azerite essences.
        """
        resource = "/data/wow/azerite-essence/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_azerite_essence(
        self, region: str, locale: str, azerite_essence_id: int
    ) -> dict[str, Any]:
        """
        Return an Azerite essence by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            azerite_essence_id (int): The ID of the Azerite essence to retrieve.

        Returns:
            Dict[str, Any]: A dictionary containing the Azerite essence details.
        """
        resource = f"/data/wow/azerite-essence/{azerite_essence_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_azerite_essence_media(
        self, region: str, locale: str, azerite_essence_id: int
    ) -> dict[str, Any]:
        """
        Return media for an Azerite essence by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            azerite_essence_id (int): The ID of the Azerite essence to retrieve media for.

        Returns:
            Dict[str, Any]: A dictionary containing the Azerite essence media.
        """
        resource = f"/data/wow/media/azerite-essence/{azerite_essence_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

        # Connected Realm API

    def get_connected_realms_index(
        self, region: str, locale: str, is_classic: bool = False
    ) -> dict[str, Any]:
        """
        Return an index of connected realms.

        Args:
            region (str): The region to query (e.g., "us", "eu").
            locale (str): The locale to use for the response.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the index of connected realms.
        """
        resource = "/data/wow/connected-realm/index"
        namespace = f"dynamic-classic-{region}" if is_classic else f"dynamic-{region}"
        query_params = {"namespace": namespace, "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_connected_realm(
        self,
        region: str,
        locale: str,
        connected_realm_id: int,
        is_classic: bool = False,
    ) -> dict[str, Any]:
        """
        Return a connected realm by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            connected_realm_id (int): The ID of the connected realm to retrieve.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the connected realm details.
        """
        resource = f"/data/wow/connected-realm/{connected_realm_id}"
        namespace = f"dynamic-classic-{region}" if is_classic else f"dynamic-{region}"
        query_params = {"namespace": namespace, "locale": locale}
        return super().get_resource(resource, region, query_params)

        # Covenant API

    def get_covenant_index(self, region: str, locale: str) -> dict[str, Any]:
        """
        Return an index of covenants.

        Args:
            region (str): The region to query (e.g., "us", "eu").
            locale (str): The locale to use for the response.

        Returns:
            Dict[str, Any]: A dictionary containing the index of covenants.
        """
        resource = "/data/wow/covenant/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_covenant(
        self, region: str, locale: str, covenant_id: int
    ) -> dict[str, Any]:
        """
        Return a covenant by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            covenant_id (int): The ID of the covenant to retrieve.

        Returns:
            Dict[str, Any]: A dictionary containing the covenant details.
        """
        resource = f"/data/wow/covenant/{covenant_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_covenant_media(
        self, region: str, locale: str, covenant_id: int
    ) -> dict[str, Any]:
        """
        Return media for a covenant by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            covenant_id (int): The ID of the covenant to retrieve media for.

        Returns:
            Dict[str, Any]: A dictionary containing the covenant media.
        """
        resource = f"/data/wow/media/covenant/{covenant_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_soulbind_index(self, region: str, locale: str) -> dict[str, Any]:
        """
        Return an index of soulbinds.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.

        Returns:
            Dict[str, Any]: A dictionary containing the index of soulbinds.
        """
        resource = "/data/wow/covenant/soulbind/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_soulbind(
        self, region: str, locale: str, soulbind_id: int
    ) -> dict[str, Any]:
        """
        Return a soulbind by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            soulbind_id (int): The ID of the soulbind to retrieve.

        Returns:
            Dict[str, Any]: A dictionary containing the soulbind details.
        """
        resource = f"/data/wow/covenant/soulbind/{soulbind_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_conduit_index(self, region: str, locale: str) -> dict[str, Any]:
        """
        Return an index of conduits.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.

        Returns:
            Dict[str, Any]: A dictionary containing the index of conduits.
        """
        resource = "/data/wow/covenant/conduit/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_conduit(self, region: str, locale: str, conduit_id: int) -> dict[str, Any]:
        """
        Return a conduit by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            conduit_id (int): The ID of the conduit to retrieve.

        Returns:
            Dict[str, Any]: A dictionary containing the conduit details.
        """
        resource = f"/data/wow/covenant/conduit/{conduit_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

        # Creature API

    def get_creature_families_index(
        self, region: str, locale: str, is_classic: bool = False
    ) -> dict[str, Any]:
        """
        Return an index of creature families.

        Args:
            region (str): The region to query (e.g., "us", "eu").
            locale (str): The locale to use for the response.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the index of creature families.
        """
        resource = "/data/wow/creature-family/index"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {"namespace": namespace, "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_creature_family(
        self,
        region: str,
        locale: str,
        creature_family_id: int,
        is_classic: bool = False,
    ) -> dict[str, Any]:
        """
        Return a creature family by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            creature_family_id (int): The ID of the creature family to retrieve.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the creature family details.
        """
        resource = f"/data/wow/creature-family/{creature_family_id}"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {"namespace": namespace, "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_creature_types_index(
        self, region: str, locale: str, is_classic: bool = False
    ) -> dict[str, Any]:
        """
        Return an index of creature types.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the index of creature types.
        """
        resource = "/data/wow/creature-type/index"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {"namespace": namespace, "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_creature_type(
        self, region: str, locale: str, creature_type_id: int, is_classic: bool = False
    ) -> dict[str, Any]:
        """
        Return a creature type by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            creature_type_id (int): The ID of the creature type to retrieve.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the creature type details.
        """
        resource = f"/data/wow/creature-type/{creature_type_id}"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {"namespace": namespace, "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_creature(
        self, region: str, locale: str, creature_id: int, is_classic: bool = False
    ) -> dict[str, Any]:
        """
        Return a creature by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            creature_id (int): The ID of the creature to retrieve.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the creature details.
        """
        resource = f"/data/wow/creature/{creature_id}"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {"namespace": namespace, "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_creature_display_media(
        self,
        region: str,
        locale: str,
        creature_display_id: int,
        is_classic: bool = False,
    ) -> dict[str, Any]:
        """
        Return media for a creature display by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            creature_display_id (int): The ID of the creature display to retrieve media for.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the creature display media.
        """
        resource = f"/data/wow/media/creature-display/{creature_display_id}"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {"namespace": namespace, "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_creature_family_media(
        self,
        region: str,
        locale: str,
        creature_family_id: int,
        is_classic: bool = False,
    ) -> dict[str, Any]:
        """
        Return media for a creature family by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            creature_family_id (int): The ID of the creature family to retrieve media for.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the creature family media.
        """
        resource = f"/data/wow/media/creature-family/{creature_family_id}"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {"namespace": namespace, "locale": locale}
        return super().get_resource(resource, region, query_params)

        # Guild Crest API

    def get_guild_crest_components_index(
        self, region: str, locale: str, is_classic: bool = False
    ) -> dict[str, Any]:
        """
        Return an index of guild crest media.

        Args:
            region (str): The region to query (e.g., "us", "eu").
            locale (str): The locale to use for the response.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the index of guild crest media.
        """
        resource = "/data/wow/guild-crest/index"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {"namespace": namespace, "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_guild_crest_border_media(
        self, region: str, locale: str, border_id: int, is_classic: bool = False
    ) -> dict[str, Any]:
        """
        Return media for a guild crest border by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            border_id (int): The ID of the guild crest border to retrieve.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the guild crest border media.
        """
        resource = f"/data/wow/media/guild-crest/border/{border_id}"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {"namespace": namespace, "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_guild_crest_emblem_media(
        self, region: str, locale: str, emblem_id: int, is_classic: bool = False
    ) -> dict[str, Any]:
        """
        Return media for a guild crest emblem by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            emblem_id (int): The ID of the guild crest emblem to retrieve.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the guild crest emblem media.
        """
        resource = f"/data/wow/media/guild-crest/emblem/{emblem_id}"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {"namespace": namespace, "locale": locale}
        return super().get_resource(resource, region, query_params)

        # Heirloom API

    def get_heirloom_index(self, region: str, locale: str) -> dict[str, Any]:
        """
        Return an index of heirlooms.

        Args:
            region (str): The region to query (e.g., "us", "eu").
            locale (str): The locale to use for the response.

        Returns:
            Dict[str, Any]: A dictionary containing the index of heirlooms.
        """
        resource = "/data/wow/heirloom/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_heirloom(
        self, region: str, locale: str, heirloom_id: int
    ) -> dict[str, Any]:
        """
        Return an heirloom by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            heirloom_id (int): The ID of the heirloom to retrieve.

        Returns:
            Dict[str, Any]: A dictionary containing the heirloom details.
        """
        resource = f"/data/wow/heirloom/{heirloom_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

        # Item API

    def get_item_classes_index(
        self, region: str, locale: str, is_classic: bool = False
    ) -> dict[str, Any]:
        """
        Return an index of item classes.

        Args:
            region (str): The region to query (e.g., "us", "eu").
            locale (str): The locale to use for the response.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the index of item classes.
        """
        resource = "/data/wow/item-class/index"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {"namespace": namespace, "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_item_class(
        self, region: str, locale: str, item_class_id: int, is_classic: bool = False
    ) -> dict[str, Any]:
        """
        Return an item class by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            item_class_id (int): The ID of the item class to retrieve.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the item class details.
        """
        resource = f"/data/wow/item-class/{item_class_id}"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {"namespace": namespace, "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_item_sets_index(
        self, region: str, locale: str, is_classic: bool = False
    ) -> dict[str, Any]:
        """
        Return an index of item sets.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the index of item sets.
        """
        resource = "/data/wow/item-set/index"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {"namespace": namespace, "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_item_set(
        self, region: str, locale: str, item_set_id: int, is_classic: bool = False
    ) -> dict[str, Any]:
        """
        Return an item set by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            item_set_id (int): The ID of the item set to retrieve.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the item set details.
        """
        resource = f"/data/wow/item-set/{item_set_id}"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {"namespace": namespace, "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_item_subclass(
        self,
        region: str,
        locale: str,
        item_class_id: int,
        item_subclass_id: int,
        is_classic: bool = False,
    ) -> dict[str, Any]:
        """
        Return an item subclass by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            item_class_id (int): The ID of the item class.
            item_subclass_id (int): The ID of the item subclass to retrieve.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the item subclass details.
        """
        resource = (
            f"/data/wow/item-class/{item_class_id}/item-subclass/{item_subclass_id}"
        )
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {"namespace": namespace, "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_item(
        self, region: str, locale: str, item_id: int, is_classic: bool = False
    ) -> dict[str, Any]:
        """
        Return an item by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            item_id (int): The ID of the item to retrieve.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the item details.
        """
        resource = f"/data/wow/item/{item_id}"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {"namespace": namespace, "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_item_media(
        self, region: str, locale: str, item_id: int, is_classic: bool = False
    ) -> dict[str, Any]:
        """
        Return media for an item by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            item_id (int): The ID of the item to retrieve media for.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the item media.
        """
        resource = f"/data/wow/media/item/{item_id}"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {"namespace": namespace, "locale": locale}
        return super().get_resource(resource, region, query_params)

        # Item Appearance API

    def get_item_appearance(
        self, region: str, locale: str, appearance_id: int, is_classic: bool = False
    ) -> dict[str, Any]:
        """
        Return an item appearance by ID.

        Args:
            region (str): The region to query (e.g., "us", "eu").
            locale (str): The locale to use for the response.
            appearance_id (int): The ID of the item appearance to retrieve.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the item appearance details.
        """
        resource = f"/data/wow/item-appearance/{appearance_id}"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {"namespace": namespace, "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_item_appearance_sets_index(
        self, region: str, locale: str, is_classic: bool = False
    ) -> dict[str, Any]:
        """
        Return an index of item appearance sets.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the index of item appearance sets.
        """
        resource = "/data/wow/item-appearance/set/index"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {"namespace": namespace, "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_item_appearance_set(
        self, region: str, locale: str, appearance_set_id: int, is_classic: bool = False
    ) -> dict[str, Any]:
        """
        Return an item appearance set by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            appearance_set_id (int): The ID of the item appearance set to retrieve.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the item appearance set details.
        """
        resource = f"/data/wow/item-appearance/set/{appearance_set_id}"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {"namespace": namespace, "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_item_appearance_slot_index(
        self, region: str, locale: str, is_classic: bool = False
    ) -> dict[str, Any]:
        """
        Return an index of item appearance slots.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the index of item appearance slots.
        """
        resource = "/data/wow/item-appearance/slot/index"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {"namespace": namespace, "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_item_appearance_slot(
        self, region: str, locale: str, slot_type: str, is_classic: bool = False
    ) -> dict[str, Any]:
        """
        Return an item appearance slot by slot type.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            slot_type (str): The type of slot to retrieve (e.g., "head", "chest").
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the item appearance slot details.
        """
        resource = f"/data/wow/item-appearance/slot/{slot_type}"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {"namespace": namespace, "locale": locale}
        return super().get_resource(resource, region, query_params)

    # Journal API

    def get_journal_expansions_index(self, region: str, locale: str) -> dict[str, Any]:
        """
        Return an index of journal expansions.

        Args:
            region (str): The region to query (e.g., "us", "eu").
            locale (str): The locale to use for the response.

        Returns:
            Dict[str, Any]: A dictionary containing the index of journal expansions.
        """
        resource = "/data/wow/journal-expansion/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_journal_expansion(
        self, region: str, locale: str, journal_expansion_id: int
    ) -> dict[str, Any]:
        """
        Return a journal expansion by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            journal_expansion_id (int): The ID of the journal expansion to retrieve.

        Returns:
            Dict[str, Any]: A dictionary containing the journal expansion details.
        """
        resource = f"/data/wow/journal-expansion/{journal_expansion_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_journal_encounters_index(self, region: str, locale: str) -> dict[str, Any]:
        """
        Return an index of journal encounters.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.

        Returns:
            Dict[str, Any]: A dictionary containing the index of journal encounters.
        """
        resource = "/data/wow/journal-encounter/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_journal_encounter(
        self, region: str, locale: str, journal_encounter_id: int
    ) -> dict[str, Any]:
        """
        Return a journal encounter by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            journal_encounter_id (int): The ID of the journal encounter to retrieve.

        Returns:
            Dict[str, Any]: A dictionary containing the journal encounter details.
        """
        resource = f"/data/wow/journal-encounter/{journal_encounter_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_journal_instances_index(self, region: str, locale: str) -> dict[str, Any]:
        """
        Return an index of journal instances.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.

        Returns:
            Dict[str, Any]: A dictionary containing the index of journal instances.
        """
        resource = "/data/wow/journal-instance/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_journal_instance(
        self, region: str, locale: str, journal_instance_id: int
    ) -> dict[str, Any]:
        """
        Return a journal instance by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            journal_instance_id (int): The ID of the journal instance to retrieve.

        Returns:
            Dict[str, Any]: A dictionary containing the journal instance details.
        """
        resource = f"/data/wow/journal-instance/{journal_instance_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_journal_instance_media(
        self, region: str, locale: str, journal_instance_id: int
    ) -> dict[str, Any]:
        """
        Return media for a journal instance by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            journal_instance_id (int): The ID of the journal instance to retrieve media for.

        Returns:
            Dict[str, Any]: A dictionary containing the journal instance media.
        """
        resource = f"/data/wow/media/journal-instance/{journal_instance_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

        # Modified Crafting API

    def get_modified_crafting_index(self, region: str, locale: str) -> dict[str, Any]:
        """
        Return the parent index for Modified Crafting.

        Args:
            region (str): The region to query (e.g., "us", "eu").
            locale (str): The locale to use for the response.

        Returns:
            Dict[str, Any]: A dictionary containing the index for Modified Crafting.
        """
        resource = "/data/wow/modified-crafting/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_modified_crafting_category_index(
        self, region: str, locale: str
    ) -> dict[str, Any]:
        """
        Return the index of Modified Crafting categories.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.

        Returns:
            Dict[str, Any]: A dictionary containing the index of Modified Crafting categories.
        """
        resource = "/data/wow/modified-crafting/category/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_modified_crafting_category(
        self, region: str, locale: str, category_id: int
    ) -> dict[str, Any]:
        """
        Return a Modified Crafting category by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            category_id (int): The ID of the Modified Crafting category to retrieve.

        Returns:
            Dict[str, Any]: A dictionary containing the Modified Crafting category details.
        """
        resource = f"/data/wow/modified-crafting/category/{category_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_modified_crafting_reagent_slot_type_index(
        self, region: str, locale: str
    ) -> dict[str, Any]:
        """
        Return the index of Modified Crafting reagent slot types.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.

        Returns:
            Dict[str, Any]: A dictionary containing the index of reagent slot types.
        """
        resource = "/data/wow/modified-crafting/reagent-slot-type/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_modified_crafting_reagent_slot_type(
        self, region: str, locale: str, slot_type_id: int
    ) -> dict[str, Any]:
        """
        Return a Modified Crafting reagent slot type by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            slot_type_id (int): The ID of the reagent slot type to retrieve.

        Returns:
            Dict[str, Any]: A dictionary containing the reagent slot type details.
        """
        resource = f"/data/wow/modified-crafting/reagent-slot-type/{slot_type_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

        # Mount API

    def get_mounts_index(self, region: str, locale: str) -> dict[str, Any]:
        """
        Return an index of mounts.

        Args:
            region (str): The region to query (e.g., "us", "eu").
            locale (str): The locale to use for the response.

        Returns:
            Dict[str, Any]: A dictionary containing the index of mounts.
        """
        resource = "/data/wow/mount/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_mount(self, region: str, locale: str, mount_id: int) -> dict[str, Any]:
        """
        Return a mount by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            mount_id (int): The ID of the mount to retrieve.

        Returns:
            Dict[str, Any]: A dictionary containing the mount details.
        """
        resource = f"/data/wow/mount/{mount_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

        # Mythic Keystone Affix API

    def get_mythic_keystone_affixes_index(
        self, region: str, locale: str
    ) -> dict[str, Any]:
        """
        Return an index of mythic keystone affixes.

        Args:
            region (str): The region to query (e.g., "us", "eu").
            locale (str): The locale to use for the response.

        Returns:
            Dict[str, Any]: A dictionary containing the index of mythic keystone affixes.
        """
        resource = "/data/wow/keystone-affix/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_mythic_keystone_affix(
        self, region: str, locale: str, keystone_affix_id: int
    ) -> dict[str, Any]:
        """
        Return a mythic keystone affix by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            keystone_affix_id (int): The ID of the mythic keystone affix to retrieve.

        Returns:
            Dict[str, Any]: A dictionary containing the mythic keystone affix details.
        """
        resource = f"/data/wow/keystone-affix/{keystone_affix_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_mythic_keystone_affix_media(
        self, region: str, locale: str, keystone_affix_id: int
    ) -> dict[str, Any]:
        """
        Return media for a mythic keystone affix by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            keystone_affix_id (int): The ID of the mythic keystone affix to retrieve media for.

        Returns:
            Dict[str, Any]: A dictionary containing the mythic keystone affix media.
        """
        resource = f"/data/wow/media/keystone-affix/{keystone_affix_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

        # Mythic Keystone Dungeon API

    def get_mythic_keystone_dungeons_index(
        self, region: str, locale: str
    ) -> dict[str, Any]:
        """
        Return an index of Mythic Keystone dungeons.

        Args:
            region (str): The region to query (e.g., "us", "eu").
            locale (str): The locale to use for the response.

        Returns:
            Dict[str, Any]: A dictionary containing the index of Mythic Keystone dungeons.
        """
        resource = "/data/wow/mythic-keystone/dungeon/index"
        query_params = {"namespace": f"dynamic-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_mythic_keystone_dungeon(
        self, region: str, locale: str, dungeon_id: int
    ) -> dict[str, Any]:
        """
        Return a Mythic Keystone dungeon by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            dungeon_id (int): The ID of the dungeon to retrieve.

        Returns:
            Dict[str, Any]: A dictionary containing the Mythic Keystone dungeon details.
        """
        resource = f"/data/wow/mythic-keystone/dungeon/{dungeon_id}"
        query_params = {"namespace": f"dynamic-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_mythic_keystone_index(self, region: str, locale: str) -> dict[str, Any]:
        """
        Return an index of links to other documents related to Mythic Keystone dungeons.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.

        Returns:
            Dict[str, Any]: A dictionary containing the index of links to related documents.
        """
        resource = "/data/wow/mythic-keystone/index"
        query_params = {"namespace": f"dynamic-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_mythic_keystone_periods_index(
        self, region: str, locale: str
    ) -> dict[str, Any]:
        """
        Return an index of Mythic Keystone periods.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.

        Returns:
            Dict[str, Any]: A dictionary containing the index of Mythic Keystone periods.
        """
        resource = "/data/wow/mythic-keystone/period/index"
        query_params = {"namespace": f"dynamic-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_mythic_keystone_period(
        self, region: str, locale: str, period_id: int
    ) -> dict[str, Any]:
        """
        Return a Mythic Keystone period by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            period_id (int): The ID of the Mythic Keystone period to retrieve.

        Returns:
            Dict[str, Any]: A dictionary containing the Mythic Keystone period details.
        """
        resource = f"/data/wow/mythic-keystone/period/{period_id}"
        query_params = {"namespace": f"dynamic-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_mythic_keystone_seasons_index(
        self, region: str, locale: str
    ) -> dict[str, Any]:
        """
        Return an index of Mythic Keystone seasons.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.

        Returns:
            Dict[str, Any]: A dictionary containing the index of Mythic Keystone seasons.
        """
        resource = "/data/wow/mythic-keystone/season/index"
        query_params = {"namespace": f"dynamic-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_mythic_keystone_season(
        self, region: str, locale: str, season_id: int
    ) -> dict[str, Any]:
        """
        Return a Mythic Keystone season by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            season_id (int): The ID of the Mythic Keystone season to retrieve.

        Returns:
            Dict[str, Any]: A dictionary containing the Mythic Keystone season details.
        """
        resource = f"/data/wow/mythic-keystone/season/{season_id}"
        query_params = {"namespace": f"dynamic-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

        # Mythic Keystone Leaderboard API

    def get_mythic_keystone_leaderboards_index(
        self, region: str, locale: str, connected_realm_id: int
    ) -> dict[str, Any]:
        """
        Return an index of Mythic Keystone Leaderboard dungeon instances for a connected realm.

        Args:
            region (str): The region to query (e.g., "us", "eu").
            locale (str): The locale to use for the response.
            connected_realm_id (int): The ID of the connected realm.

        Returns:
            Dict[str, Any]: A dictionary containing the index of Mythic Keystone Leaderboard dungeon instances.
        """
        resource = (
            f"/data/wow/connected-realm/{connected_realm_id}/mythic-leaderboard/index"
        )
        query_params = {"namespace": f"dynamic-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_mythic_keystone_leaderboard(
        self,
        region: str,
        locale: str,
        connected_realm_id: int,
        dungeon_id: int,
        period_id: int,
    ) -> dict[str, Any]:
        """
        Return a weekly Mythic Keystone Leaderboard by period.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            connected_realm_id (int): The ID of the connected realm.
            dungeon_id (int): The ID of the dungeon.
            period_id (int): The ID of the period to retrieve.

        Returns:
            Dict[str, Any]: A dictionary containing the Mythic Keystone Leaderboard details for the specified period.
        """
        resource = f"/data/wow/connected-realm/{connected_realm_id}/mythic-leaderboard/{dungeon_id}/period/{period_id}"
        query_params = {"namespace": f"dynamic-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

        # Mythic Raid Leaderboard API

    def get_mythic_raid_leaderboard(
        self, region: str, locale: str, raid: str, faction: str
    ) -> dict[str, Any]:
        """
        Return the leaderboard for a given raid and faction.

        Args:
            region (str): The region to query (e.g., "us", "eu").
            locale (str): The locale to use for the response.
            raid (str): The raid to retrieve the leaderboard for (e.g., "castle-nathria").
            faction (str): The faction to retrieve the leaderboard for (e.g., "alliance", "horde").

        Returns:
            Dict[str, Any]: A dictionary containing the raid leaderboard details for the specified faction.
        """
        resource = f"/data/wow/leaderboard/hall-of-fame/{raid}/{faction}"
        query_params = {"namespace": f"dynamic-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

        # Pet API

    def get_pets_index(self, region: str, locale: str) -> dict[str, Any]:
        """
        Return an index of battle pets.

        Args:
            region (str): The region to query (e.g., "us", "eu").
            locale (str): The locale to use for the response.

        Returns:
            Dict[str, Any]: A dictionary containing the index of battle pets.
        """
        resource = "/data/wow/pet/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_pet(self, region: str, locale: str, pet_id: int) -> dict[str, Any]:
        """
        Return a battle pet by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            pet_id (int): The ID of the battle pet to retrieve.

        Returns:
            Dict[str, Any]: A dictionary containing the battle pet details.
        """
        resource = f"/data/wow/pet/{pet_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_pet_media(self, region: str, locale: str, pet_id: int) -> dict[str, Any]:
        """
        Return media for a battle pet by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            pet_id (int): The ID of the battle pet to retrieve media for.

        Returns:
            Dict[str, Any]: A dictionary containing the battle pet media.
        """
        resource = f"/data/wow/media/pet/{pet_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_pet_abilities_index(self, region: str, locale: str) -> dict[str, Any]:
        """
        Return an index of pet abilities.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.

        Returns:
            Dict[str, Any]: A dictionary containing the index of pet abilities.
        """
        resource = "/data/wow/pet-ability/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_pet_ability(
        self, region: str, locale: str, pet_ability_id: int
    ) -> dict[str, Any]:
        """
        Return a pet ability by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            pet_ability_id (int): The ID of the pet ability to retrieve.

        Returns:
            Dict[str, Any]: A dictionary containing the pet ability details.
        """
        resource = f"/data/wow/pet-ability/{pet_ability_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_pet_ability_media(
        self, region: str, locale: str, pet_ability_id: int
    ) -> dict[str, Any]:
        """
        Return media for a pet ability by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            pet_ability_id (int): The ID of the pet ability to retrieve media for.

        Returns:
            Dict[str, Any]: A dictionary containing the pet ability media.
        """
        resource = f"/data/wow/media/pet-ability/{pet_ability_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

        # Playable Class API

    def get_playable_classes_index(
        self, region: str, locale: str, is_classic: bool = False
    ) -> dict[str, Any]:
        """
        Return an index of playable classes.

        Args:
            region (str): The region to query (e.g., "us", "eu").
            locale (str): The locale to use for the response.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the index of playable classes.
        """
        resource = "/data/wow/playable-class/index"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {"namespace": namespace, "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_playable_class(
        self, region: str, locale: str, class_id: int, is_classic: bool = False
    ) -> dict[str, Any]:
        """
        Return a playable class by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            class_id (int): The ID of the playable class to retrieve.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the playable class details.
        """
        resource = f"/data/wow/playable-class/{class_id}"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {"namespace": namespace, "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_playable_class_media(
        self,
        region: str,
        locale: str,
        playable_class_id: int,
        is_classic: bool = False,
    ) -> dict[str, Any]:
        """
        Return media for a playable class by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            playable_class_id (int): The ID of the playable class to retrieve media for.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the playable class media.
        """
        resource = f"/data/wow/media/playable-class/{playable_class_id}"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {"namespace": namespace, "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_pvp_talent_slots(
        self, region: str, locale: str, class_id: int
    ) -> dict[str, Any]:
        """
        Return the Pvp talent slots for a playable class by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            class_id (int): The ID of the playable class to retrieve PvP talent slots for.

        Returns:
            Dict[str, Any]: A dictionary containing the PvP talent slots.
        """
        resource = f"/data/wow/playable-class/{class_id}/pvp-talent-slots"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

        # Playable Race API

    def get_playable_races_index(
        self, region: str, locale: str, is_classic: bool = False
    ) -> dict[str, Any]:
        """
        Return an index of playable races.

        Args:
            region (str): The region to query (e.g., "us", "eu").
            locale (str): The locale to use for the response.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the index of playable races.
        """
        resource = "/data/wow/playable-race/index"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {"namespace": namespace, "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_playable_race(
        self, region: str, locale: str, playable_race_id: int, is_classic: bool = False
    ) -> dict[str, Any]:
        """
        Return a playable race by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            playable_race_id (int): The ID of the playable race to retrieve.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the playable race details.
        """
        resource = f"/data/wow/playable-race/{playable_race_id}"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {"namespace": namespace, "locale": locale}
        return super().get_resource(resource, region, query_params)

        # Playable Specialization API

    def get_playable_specializations_index(
        self, region: str, locale: str
    ) -> dict[str, Any]:
        """
        Return an index of playable specializations.

        Args:
            region (str): The region to query (e.g., "us", "eu").
            locale (str): The locale to use for the response.

        Returns:
            Dict[str, Any]: A dictionary containing the index of playable specializations.
        """
        resource = "/data/wow/playable-specialization/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_playable_specialization(
        self, region: str, locale: str, spec_id: int
    ) -> dict[str, Any]:
        """
        Return a playable specialization by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            spec_id (int): The ID of the playable specialization to retrieve.

        Returns:
            Dict[str, Any]: A dictionary containing the playable specialization details.
        """
        resource = f"/data/wow/playable-specialization/{spec_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_playable_specialization_media(
        self, region: str, locale: str, spec_id: int
    ) -> dict[str, Any]:
        """
        Return media for a playable specialization by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            spec_id (int): The ID of the playable specialization to retrieve media for.

        Returns:
            Dict[str, Any]: A dictionary containing the playable specialization media.
        """
        resource = f"/data/wow/media/playable-specialization/{spec_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

        # Power Type API

    def get_power_types_index(
        self, region: str, locale: str, is_classic: bool = False
    ) -> dict[str, Any]:
        """
        Return an index of power types.

        Args:
            region (str): The region to query (e.g., "us", "eu").
            locale (str): The locale to use for the response.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the index of power types.
        """
        resource = "/data/wow/power-type/index"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {"namespace": namespace, "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_power_type(
        self, region: str, locale: str, power_type_id: int, is_classic: bool = False
    ) -> dict[str, Any]:
        """
        Return a power type by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            power_type_id (int): The ID of the power type to retrieve.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the power type details.
        """
        resource = f"/data/wow/power-type/{power_type_id}"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {"namespace": namespace, "locale": locale}
        return super().get_resource(resource, region, query_params)

        # Profession API

    def get_professions_index(self, region: str, locale: str) -> dict[str, Any]:
        """
        Return an index of professions.

        Args:
            region (str): The region to query (e.g., "us", "eu").
            locale (str): The locale to use for the response.

        Returns:
            Dict[str, Any]: A dictionary containing the index of professions.
        """
        resource = "/data/wow/profession/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_profession(
        self, region: str, locale: str, profession_id: int
    ) -> dict[str, Any]:
        """
        Return a profession by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            profession_id (int): The ID of the profession to retrieve.

        Returns:
            Dict[str, Any]: A dictionary containing the profession details.
        """
        resource = f"/data/wow/profession/{profession_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_profession_media(
        self, region: str, locale: str, profession_id: int
    ) -> dict[str, Any]:
        """
        Return media for a profession by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            profession_id (int): The ID of the profession to retrieve media for.

        Returns:
            Dict[str, Any]: A dictionary containing the profession media.
        """
        resource = f"/data/wow/media/profession/{profession_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_profession_skill_tier(
        self, region: str, locale: str, profession_id: int, skill_tier_id: int
    ) -> dict[str, Any]:
        """
        Return a skill tier for a profession by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            profession_id (int): The ID of the profession.
            skill_tier_id (int): The ID of the skill tier to retrieve.

        Returns:
            Dict[str, Any]: A dictionary containing the skill tier details.
        """
        resource = f"/data/wow/profession/{profession_id}/skill-tier/{skill_tier_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_recipe(self, region: str, locale: str, recipe_id: int) -> dict[str, Any]:
        """
        Return a recipe by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            recipe_id (int): The ID of the recipe to retrieve.

        Returns:
            Dict[str, Any]: A dictionary containing the recipe details.
        """
        resource = f"/data/wow/recipe/{recipe_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_recipe_media(
        self, region: str, locale: str, recipe_id: int
    ) -> dict[str, Any]:
        """
        Return media for a recipe by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            recipe_id (int): The ID of the recipe to retrieve media for.

        Returns:
            Dict[str, Any]: A dictionary containing the recipe media.
        """
        resource = f"/data/wow/media/recipe/{recipe_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

        # PvP Season API

    def get_pvp_seasons_index(self, region: str, locale: str) -> dict[str, Any]:
        """
        Return an index of PvP seasons.

        Args:
            region (str): The region to query (e.g., "us", "eu").
            locale (str): The locale to use for the response.

        Returns:
            Dict[str, Any]: A dictionary containing the index of PvP seasons.
        """
        resource = "/data/wow/pvp-season/index"
        query_params = {"namespace": f"dynamic-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_pvp_season(
        self, region: str, locale: str, pvp_season_id: int
    ) -> dict[str, Any]:
        """
        Return a PvP season by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            pvp_season_id (int): The ID of the PvP season to retrieve.

        Returns:
            Dict[str, Any]: A dictionary containing the PvP season details.
        """
        resource = f"/data/wow/pvp-season/{pvp_season_id}"
        query_params = {"namespace": f"dynamic-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_pvp_leaderboards_index(
        self, region: str, locale: str, pvp_season_id: int
    ) -> dict[str, Any]:
        """
        Return an index of PvP leaderboards for a PvP season.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            pvp_season_id (int): The ID of the PvP season.

        Returns:
            Dict[str, Any]: A dictionary containing the index of PvP leaderboards.
        """
        resource = f"/data/wow/pvp-season/{pvp_season_id}/pvp-leaderboard/index"
        query_params = {"namespace": f"dynamic-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_pvp_leaderboard(
        self, region: str, locale: str, pvp_season_id: int, pvp_bracket: str
    ) -> dict[str, Any]:
        """
        Return the PvP leaderboard of a specific PvP bracket for a PvP season.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            pvp_season_id (int): The ID of the PvP season.
            pvp_bracket (str): The PvP bracket to retrieve (e.g., "2v2", "3v3").

        Returns:
            Dict[str, Any]: A dictionary containing the PvP leaderboard details.
        """
        resource = f"/data/wow/pvp-season/{pvp_season_id}/pvp-leaderboard/{pvp_bracket}"
        query_params = {"namespace": f"dynamic-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_pvp_rewards_index(
        self, region: str, locale: str, pvp_season_id: int
    ) -> dict[str, Any]:
        """
        Return an index of PvP rewards for a PvP season.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            pvp_season_id (int): The ID of the PvP season.

        Returns:
            Dict[str, Any]: A dictionary containing the index of PvP rewards.
        """
        resource = f"/data/wow/pvp-season/{pvp_season_id}/pvp-reward/index"
        query_params = {"namespace": f"dynamic-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

        # PvP Tier API

    def get_pvp_tier_media(
        self, region: str, locale: str, pvp_tier_id: int
    ) -> dict[str, Any]:
        """
        Return media for a PvP tier by ID.

        Args:
            region (str): The region to query (e.g., "us", "eu").
            locale (str): The locale to use for the response.
            pvp_tier_id (int): The ID of the PvP tier to retrieve media for.

        Returns:
            Dict[str, Any]: A dictionary containing the PvP tier media.
        """
        resource = f"/data/wow/media/pvp-tier/{pvp_tier_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_pvp_tiers_index(self, region: str, locale: str) -> dict[str, Any]:
        """
        Return an index of PvP tiers.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.

        Returns:
            Dict[str, Any]: A dictionary containing the index of PvP tiers.
        """
        resource = "/data/wow/pvp-tier/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_pvp_tier(
        self, region: str, locale: str, pvp_tier_id: int
    ) -> dict[str, Any]:
        """
        Return a PvP tier by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            pvp_tier_id (int): The ID of the PvP tier to retrieve.

        Returns:
            Dict[str, Any]: A dictionary containing the PvP tier details.
        """
        resource = f"/data/wow/pvp-tier/{pvp_tier_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

        # Quest API

    def get_quests_index(self, region: str, locale: str) -> dict[str, Any]:
        """
        Return the parent index for quests.

        Args:
            region (str): The region to query (e.g., "us", "eu").
            locale (str): The locale to use for the response.

        Returns:
            Dict[str, Any]: A dictionary containing the parent index for quests.
        """
        resource = "/data/wow/quest/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_quest(self, region: str, locale: str, quest_id: int) -> dict[str, Any]:
        """
        Return a quest by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            quest_id (int): The ID of the quest to retrieve.

        Returns:
            Dict[str, Any]: A dictionary containing the quest details.
        """
        resource = f"/data/wow/quest/{quest_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_quest_categories_index(self, region: str, locale: str) -> dict[str, Any]:
        """
        Return an index of quest categories (such as quests for a specific class, profession, or storyline).

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.

        Returns:
            Dict[str, Any]: A dictionary containing the index of quest categories.
        """
        resource = "/data/wow/quest/category/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_quest_category(
        self, region: str, locale: str, quest_category_id: int
    ) -> dict[str, Any]:
        """
        Return a quest category by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            quest_category_id (int): The ID of the quest category to retrieve.

        Returns:
            Dict[str, Any]: A dictionary containing the quest category details.
        """
        resource = f"/data/wow/quest/category/{quest_category_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_quest_areas_index(self, region: str, locale: str) -> dict[str, Any]:
        """
        Return an index of quest areas.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.

        Returns:
            Dict[str, Any]: A dictionary containing the index of quest areas.
        """
        resource = "/data/wow/quest/area/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_quest_area(
        self, region: str, locale: str, quest_area_id: int
    ) -> dict[str, Any]:
        """
        Return a quest area by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            quest_area_id (int): The ID of the quest area to retrieve.

        Returns:
            Dict[str, Any]: A dictionary containing the quest area details.
        """
        resource = f"/data/wow/quest/area/{quest_area_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_quest_types_index(self, region: str, locale: str) -> dict[str, Any]:
        """
        Return an index of quest types (such as PvP quests, raid quests, or account quests).

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.

        Returns:
            Dict[str, Any]: A dictionary containing the index of quest types.
        """
        resource = "/data/wow/quest/type/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_quest_type(
        self, region: str, locale: str, quest_type_id: int
    ) -> dict[str, Any]:
        """
        Return a quest type by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            quest_type_id (int): The ID of the quest type to retrieve.

        Returns:
            Dict[str, Any]: A dictionary containing the quest type details.
        """
        resource = f"/data/wow/quest/type/{quest_type_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

        # Realm API

    def get_realms_index(
        self, region: str, locale: str, is_classic: bool = False
    ) -> dict[str, Any]:
        """
        Return an index of realms.

        Args:
            region (str): The region to query (e.g., "us", "eu").
            locale (str): The locale to use for the response.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the index of realms.
        """
        resource = "/data/wow/realm/index"
        namespace = f"dynamic-classic-{region}" if is_classic else f"dynamic-{region}"
        query_params = {"namespace": namespace, "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_realm(
        self, region: str, locale: str, realm_slug: str, is_classic: bool = False
    ) -> dict[str, Any]:
        """
        Return a single realm by slug or ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            realm_slug (str): The slug of the realm to retrieve.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the realm details.
        """
        resource = f"/data/wow/realm/{realm_slug}"
        namespace = f"dynamic-classic-{region}" if is_classic else f"dynamic-{region}"
        query_params = {"namespace": namespace, "locale": locale}
        return super().get_resource(resource, region, query_params)

        # Region API

    def get_regions_index(
        self, region: str, locale: str, is_classic: bool = False
    ) -> dict[str, Any]:
        """
        Return an index of regions.

        Args:
            region (str): The region to query (e.g., "us", "eu").
            locale (str): The locale to use for the response.
            is_classic (bool, optional): Whether to query for classic regions. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the index of regions.
        """
        resource = "/data/wow/region/index"
        namespace = f"dynamic-classic-{region}" if is_classic else f"dynamic-{region}"
        query_params = {"namespace": namespace, "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_region(
        self, region: str, locale: str, region_id: int, is_classic: bool = False
    ) -> dict[str, Any]:
        """
        Return a region by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            region_id (int): The ID of the region to retrieve.
            is_classic (bool, optional): Whether to query for classic regions. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the region details.
        """
        resource = f"/data/wow/region/{region_id}"
        namespace = f"dynamic-classic-{region}" if is_classic else f"dynamic-{region}"
        query_params = {"namespace": namespace, "locale": locale}
        return super().get_resource(resource, region, query_params)

        # Reputations API

    def get_reputation_factions_index(self, region: str, locale: str) -> dict[str, Any]:
        """
        Return an index of reputation factions.

        Args:
            region (str): The region to query (e.g., "us", "eu").
            locale (str): The locale to use for the response.

        Returns:
            Dict[str, Any]: A dictionary containing the index of reputation factions.
        """
        resource = "/data/wow/reputation-faction/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_reputation_faction(
        self, region: str, locale: str, reputation_faction_id: int
    ) -> dict[str, Any]:
        """
        Return a single reputation faction by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            reputation_faction_id (int): The ID of the reputation faction to retrieve.

        Returns:
            Dict[str, Any]: A dictionary containing the reputation faction details.
        """
        resource = f"/data/wow/reputation-faction/{reputation_faction_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_reputation_tiers_index(self, region: str, locale: str) -> dict[str, Any]:
        """
        Return an index of reputation tiers.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.

        Returns:
            Dict[str, Any]: A dictionary containing the index of reputation tiers.
        """
        resource = "/data/wow/reputation-tiers/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_reputation_tier(
        self, region: str, locale: str, reputation_tiers_id: int
    ) -> dict[str, Any]:
        """
        Return a single set of reputation tiers by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            reputation_tiers_id (int): The ID of the reputation tier to retrieve.

        Returns:
            Dict[str, Any]: A dictionary containing the reputation tier details.
        """
        resource = f"/data/wow/reputation-tiers/{reputation_tiers_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

        # Spell API

    def get_spell(self, region: str, locale: str, spell_id: int) -> dict[str, Any]:
        """
        Return a spell by ID.

        Args:
            region (str): The region to query (e.g., "us", "eu").
            locale (str): The locale to use for the response.
            spell_id (int): The ID of the spell to retrieve.

        Returns:
            Dict[str, Any]: A dictionary containing the spell details.
        """
        resource = f"/data/wow/spell/{spell_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_spell_media(
        self, region: str, locale: str, spell_id: int
    ) -> dict[str, Any]:
        """
        Return media for a spell by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            spell_id (int): The ID of the spell to retrieve media for.

        Returns:
            Dict[str, Any]: A dictionary containing the spell media.
        """
        resource = f"/data/wow/media/spell/{spell_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

        # Talent API

    def get_talents_index(self, region: str, locale: str) -> dict[str, Any]:
        """
        Return an index of talents.

        Args:
            region (str): The region to query (e.g., "us", "eu").
            locale (str): The locale to use for the response.

        Returns:
            Dict[str, Any]: A dictionary containing the index of talents.
        """
        resource = "/data/wow/talent/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_talent(self, region: str, locale: str, talent_id: int) -> dict[str, Any]:
        """
        Return a talent by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            talent_id (int): The ID of the talent to retrieve.

        Returns:
            Dict[str, Any]: A dictionary containing the talent details.
        """
        resource = f"/data/wow/talent/{talent_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_pvp_talents_index(self, region: str, locale: str) -> dict[str, Any]:
        """
        Return an index of PvP talents.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.

        Returns:
            Dict[str, Any]: A dictionary containing the index of PvP talents.
        """
        resource = "/data/wow/pvp-talent/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_pvp_talent(
        self, region: str, locale: str, pvp_talent_id: int
    ) -> dict[str, Any]:
        """
        Return a PvP talent by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            pvp_talent_id (int): The ID of the PvP talent to retrieve.

        Returns:
            Dict[str, Any]: A dictionary containing the PvP talent details.
        """
        resource = f"/data/wow/pvp-talent/{pvp_talent_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

        # Tech Talent API

    def get_tech_talent_tree_index(self, region: str, locale: str) -> dict[str, Any]:
        """
        Return an index of tech talent trees.

        Args:
            region (str): The region to query (e.g., "us", "eu").
            locale (str): The locale to use for the response.

        Returns:
            Dict[str, Any]: A dictionary containing the index of tech talent trees.
        """
        resource = "/data/wow/tech-talent-tree/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_tech_talent_tree(
        self, region: str, locale: str, tech_talent_tree_id: int
    ) -> dict[str, Any]:
        """
        Return a tech talent tree by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            tech_talent_tree_id (int): The ID of the tech talent tree to retrieve.

        Returns:
            Dict[str, Any]: A dictionary containing the tech talent tree details.
        """
        resource = f"/data/wow/tech-talent-tree/{tech_talent_tree_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_tech_talent_index(self, region: str, locale: str) -> dict[str, Any]:
        """
        Return an index of tech talents.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.

        Returns:
            Dict[str, Any]: A dictionary containing the index of tech talents.
        """
        resource = "/data/wow/tech-talent/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_tech_talent(
        self, region: str, locale: str, tech_talent_id: int
    ) -> dict[str, Any]:
        """
        Return a tech talent by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            tech_talent_id (int): The ID of the tech talent to retrieve.

        Returns:
            Dict[str, Any]: A dictionary containing the tech talent details.
        """
        resource = f"/data/wow/tech-talent/{tech_talent_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_tech_talent_media(
        self, region: str, locale: str, tech_talent_id: int
    ) -> dict[str, Any]:
        """
        Return media for a tech talent by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            tech_talent_id (int): The ID of the tech talent to retrieve media for.

        Returns:
            Dict[str, Any]: A dictionary containing the tech talent media.
        """
        resource = f"/data/wow/media/tech-talent/{tech_talent_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

        # Title API

    def get_titles_index(self, region: str, locale: str) -> dict[str, Any]:
        """
        Return an index of titles.

        Args:
            region (str): The region to query (e.g., "us", "eu").
            locale (str): The locale to use for the response.

        Returns:
            Dict[str, Any]: A dictionary containing the index of titles.
        """
        resource = "/data/wow/title/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_title(self, region: str, locale: str, title_id: int) -> dict[str, Any]:
        """
        Return a title by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            title_id (int): The ID of the title to retrieve.

        Returns:
            Dict[str, Any]: A dictionary containing the title details.
        """
        resource = f"/data/wow/title/{title_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

        # Toy API

    def get_toy_index(self, region: str, locale: str) -> dict[str, Any]:
        """
        Return an index of toys.

        Args:
            region (str): The region to query (e.g., "us", "eu").
            locale (str): The locale to use for the response.

        Returns:
            Dict[str, Any]: A dictionary containing the index of toys.
        """
        resource = "/data/wow/toy/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_toy(self, region: str, locale: str, toy_id: int) -> dict[str, Any]:
        """
        Return a toy by ID.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            toy_id (int): The ID of the toy to retrieve.

        Returns:
            Dict[str, Any]: A dictionary containing the toy details.
        """
        resource = f"/data/wow/toy/{toy_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

        # Wow Token API

    def get_token_index(
        self, region: str, locale: str, is_classic: bool = False
    ) -> dict[str, Any]:
        """
        Return the Wow Token index.

        Args:
            region (str): The region to query (e.g., "us", "eu").
            locale (str): The locale to use for the response.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the Wow Token index.
        """
        resource = "/data/wow/token/index"
        namespace = f"dynamic-classic-{region}" if is_classic else f"dynamic-{region}"
        query_params = {"namespace": namespace, "locale": locale}
        return super().get_resource(resource, region, query_params)
