"""wow_game_data_api.py file."""

from typing import Any

from ..api import LocaleApi
from ..types import OptionalLocale, OptionalRegion


class WowGameDataApi(LocaleApi):
    """All Wow Game Data API methods.

    Attributes:
        client_id (str): A string client ID supplied by Blizzard.
        client_secret (str): A string client secret supplied by Blizzard.
        region (Region, optional): A default region to use for requests.
        locale (Locale, optional): A default locale to use for requests.
    """

    def _get_resource(
        self,
        resource: str,
        namespace: str,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
        **query_params: Any,
    ) -> dict[str, Any]:
        """Internal function to get resources from the World of Warcraft Game Data API

        Args:
            resource (str): the requested resource
            namespace (str): the namespace in which the requested resource lives
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.
            **query_params (dict, optional): additional arguments to to the resource request to support search requests.

        Returns:
            dict[str, Any]: the JSON response transformed to a dict structure.
        """
        query_params.update({"namespace": f"{namespace}-{region or self.region}"})
        return super().get_resource(resource, region, locale, query_params)

    def _get_static_resource(
        self,
        resource: str,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
        is_classic: bool = False,
        **query_params: Any,
    ) -> dict[str, Any]:
        """Internal function to get resources from the World of Warcraft Game Data API that use a static namespace

        Args:
            resource (str): the requested resource
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.
            is_classic (bool, optional): a boolean flag indicating whether to use a Classic WOW namespace. Defaults to False.
            **query_params (optional): additional arguments to to the resource request to support search requests.

        Returns:
            dict[str, Any]: the JSON response transformed to a dict structure.
        """
        namespace = "static-classic" if is_classic else "static"
        return self._get_resource(resource, namespace, region, locale, **query_params)

    def _get_dynamic_resource(
        self,
        resource: str,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
        is_classic: bool = False,
        **query_params: Any,
    ) -> dict[str, Any]:
        """Internal function to get resources from the World of Warcraft Game Data API that use a dynamic namespace

        Args:
            resource (str): the requested resource
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.
            is_classic (bool, optional): a boolean flag indicating whether to use a Classic WOW namespace. Defaults to False.
            **query_params (optional): additional arguments to to the resource request to support search requests.

        Returns:
            dict[str, Any]: the JSON response transformed to a dict structure.
        """
        namespace = "dynamic-classic" if is_classic else "dynamic"
        return self._get_resource(resource, namespace, region, locale, **query_params)

    # Achievement API

    def get_achievements_index(
        self, *, region: OptionalRegion = None, locale: OptionalLocale = None
    ) -> dict[str, Any]:
        """
        Return an index of achievements.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the index of achievements.
        """
        resource = "/data/wow/achievement/index"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_achievement(
        self,
        achievement_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return an achievement by ID.

        Args:
            achievement_id (int): The ID of the achievement to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the achievement details.
        """
        resource = f"/data/wow/achievement/{achievement_id}"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_achievement_categories_index(
        self, *, region: OptionalRegion = None, locale: OptionalLocale = None
    ) -> dict[str, Any]:
        """
        Return an index of achievement categories.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the index of achievement categories.
        """
        resource = "/data/wow/achievement-category/index"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_achievement_category(
        self,
        achievement_category_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return an achievement category by ID.

        Args:
            achievement_category_id (int): The ID of the achievement category to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the achievement category details.
        """
        resource = f"/data/wow/achievement-category/{achievement_category_id}"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_achievement_media(
        self,
        achievement_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return media for an achievement by ID.

        Args:
            achievement_id (int): The ID of the achievement to retrieve media for.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the achievement media.
        """
        resource = f"/data/wow/media/achievement/{achievement_id}"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

        # Auction House API

    def get_auction_house_index(
        self,
        connected_realm_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return an index of auction houses for a connected realm.

        *CLASSIC ONLY*

        Args:
            connected_realm_id (int): The ID of the connected realm.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the auction house index for the connected realm.
        """
        resource = f"/data/wow/connected-realm/{connected_realm_id}/auctions/index"
        query_params = {
            "namespace": f"dynamic-classic-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_auctions_for_auction_house(
        self,
        connected_realm_id: int,
        auction_house_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return all active auctions for a specific auction house on a connected realm.

        *CLASSIC ONLY*

        Args:
            connected_realm_id (int): The ID of the connected realm.
            auction_house_id (int): The ID of the auction house.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the active auctions for the specified auction house.
        """
        resource = f"/data/wow/connected-realm/{connected_realm_id}/auctions/{auction_house_id}"
        query_params = {
            "namespace": f"dynamic-classic-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_auctions(
        self,
        connected_realm_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return all active auctions for a connected realm.

        Args:
            connected_realm_id (int): The ID of the connected realm.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the active auctions for the connected realm.
        """
        resource = f"/data/wow/connected-realm/{connected_realm_id}/auctions"
        query_params = {
            "namespace": f"dynamic-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_commodities(
        self, *, region: OptionalRegion = None, locale: OptionalLocale = None
    ) -> dict[str, Any]:
        """
        Return all active auctions for commodity items for the entire game region.

        Auction house data updates at a set interval. The value was initially set at 1 hour;
        however, it might change over time without notice. Depending on the number of active auctions
        on the specified connected realm, the response from this endpoint may be rather large,
        sometimes exceeding 10 MB.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing all active auctions for commodity items.
        """
        resource = "/data/wow/auctions/commodities"
        query_params = {
            "namespace": f"dynamic-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

        # Azerite Essence API

    def get_azerite_essences_index(
        self, *, region: OptionalRegion = None, locale: OptionalLocale = None
    ) -> dict[str, Any]:
        """
        Return an index of Azerite essences.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the index of Azerite essences.
        """
        resource = "/data/wow/azerite-essence/index"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_azerite_essence(
        self,
        azerite_essence_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return an Azerite essence by ID.

        Args:
            azerite_essence_id (int): The ID of the Azerite essence to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the Azerite essence details.
        """
        resource = f"/data/wow/azerite-essence/{azerite_essence_id}"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_azerite_essence_media(
        self,
        azerite_essence_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return media for an Azerite essence by ID.

        Args:
            azerite_essence_id (int): The ID of the Azerite essence to retrieve media for.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the Azerite essence media.
        """
        resource = f"/data/wow/media/azerite-essence/{azerite_essence_id}"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

        # Connected Realm API

    def get_connected_realms_index(
        self,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
        is_classic: bool = False,
    ) -> dict[str, Any]:
        """
        Return an index of connected realms.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the index of connected realms.
        """
        resource = "/data/wow/connected-realm/index"
        namespace = f"dynamic-classic-{region}" if is_classic else f"dynamic-{region}"
        query_params = {
            "namespace": namespace,
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_connected_realm(
        self,
        connected_realm_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
        is_classic: bool = False,
    ) -> dict[str, Any]:
        """
        Return a connected realm by ID.

        Args:
            connected_realm_id (int): The ID of the connected realm to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the connected realm details.
        """
        resource = f"/data/wow/connected-realm/{connected_realm_id}"
        namespace = f"dynamic-classic-{region}" if is_classic else f"dynamic-{region}"
        query_params = {
            "namespace": namespace,
        }
        return super().get_resource(resource, region, locale, query_params)

        # Covenant API

    def get_covenant_index(
        self, *, region: OptionalRegion = None, locale: OptionalLocale = None
    ) -> dict[str, Any]:
        """
        Return an index of covenants.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the index of covenants.
        """
        resource = "/data/wow/covenant/index"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_covenant(
        self,
        covenant_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return a covenant by ID.

        Args:
            covenant_id (int): The ID of the covenant to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the covenant details.
        """
        resource = f"/data/wow/covenant/{covenant_id}"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_covenant_media(
        self,
        covenant_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return media for a covenant by ID.

        Args:
            covenant_id (int): The ID of the covenant to retrieve media for.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the covenant media.
        """
        resource = f"/data/wow/media/covenant/{covenant_id}"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_soulbind_index(
        self, *, region: OptionalRegion = None, locale: OptionalLocale = None
    ) -> dict[str, Any]:
        """
        Return an index of soulbinds.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the index of soulbinds.
        """
        resource = "/data/wow/covenant/soulbind/index"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_soulbind(
        self,
        soulbind_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return a soulbind by ID.

        Args:
            soulbind_id (int): The ID of the soulbind to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the soulbind details.
        """
        resource = f"/data/wow/covenant/soulbind/{soulbind_id}"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_conduit_index(
        self, *, region: OptionalRegion = None, locale: OptionalLocale = None
    ) -> dict[str, Any]:
        """
        Return an index of conduits.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the index of conduits.
        """
        resource = "/data/wow/covenant/conduit/index"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_conduit(
        self,
        conduit_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return a conduit by ID.

        Args:
            conduit_id (int): The ID of the conduit to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the conduit details.
        """
        resource = f"/data/wow/covenant/conduit/{conduit_id}"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

        # Creature API

    def get_creature_families_index(
        self,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
        is_classic: bool = False,
    ) -> dict[str, Any]:
        """
        Return an index of creature families.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the index of creature families.
        """
        resource = "/data/wow/creature-family/index"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {
            "namespace": namespace,
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_creature_family(
        self,
        creature_family_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
        is_classic: bool = False,
    ) -> dict[str, Any]:
        """
        Return a creature family by ID.

        Args:
            creature_family_id (int): The ID of the creature family to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the creature family details.
        """
        resource = f"/data/wow/creature-family/{creature_family_id}"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {
            "namespace": namespace,
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_creature_types_index(
        self,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
        is_classic: bool = False,
    ) -> dict[str, Any]:
        """
        Return an index of creature types.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the index of creature types.
        """
        resource = "/data/wow/creature-type/index"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {
            "namespace": namespace,
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_creature_type(
        self,
        creature_type_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
        is_classic: bool = False,
    ) -> dict[str, Any]:
        """
        Return a creature type by ID.

        Args:
            creature_type_id (int): The ID of the creature type to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the creature type details.
        """
        resource = f"/data/wow/creature-type/{creature_type_id}"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {
            "namespace": namespace,
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_creature(
        self,
        creature_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
        is_classic: bool = False,
    ) -> dict[str, Any]:
        """
        Return a creature by ID.

        Args:
            creature_id (int): The ID of the creature to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the creature details.
        """
        resource = f"/data/wow/creature/{creature_id}"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {
            "namespace": namespace,
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_creature_display_media(
        self,
        creature_display_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
        is_classic: bool = False,
    ) -> dict[str, Any]:
        """
        Return media for a creature display by ID.

        Args:
            creature_display_id (int): The ID of the creature display to retrieve media for.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the creature display media.
        """
        resource = f"/data/wow/media/creature-display/{creature_display_id}"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {
            "namespace": namespace,
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_creature_family_media(
        self,
        creature_family_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
        is_classic: bool = False,
    ) -> dict[str, Any]:
        """
        Return media for a creature family by ID.

        Args:
            creature_family_id (int): The ID of the creature family to retrieve media for.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the creature family media.
        """
        resource = f"/data/wow/media/creature-family/{creature_family_id}"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {
            "namespace": namespace,
        }
        return super().get_resource(resource, region, locale, query_params)

        # Guild Crest API

    def get_guild_crest_components_index(
        self,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
        is_classic: bool = False,
    ) -> dict[str, Any]:
        """
        Return an index of guild crest media.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the index of guild crest media.
        """
        resource = "/data/wow/guild-crest/index"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {
            "namespace": namespace,
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_guild_crest_border_media(
        self,
        border_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
        is_classic: bool = False,
    ) -> dict[str, Any]:
        """
        Return media for a guild crest border by ID.

        Args:
            border_id (int): The ID of the guild crest border to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the guild crest border media.
        """
        resource = f"/data/wow/media/guild-crest/border/{border_id}"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {
            "namespace": namespace,
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_guild_crest_emblem_media(
        self,
        emblem_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
        is_classic: bool = False,
    ) -> dict[str, Any]:
        """
        Return media for a guild crest emblem by ID.

        Args:
            emblem_id (int): The ID of the guild crest emblem to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the guild crest emblem media.
        """
        resource = f"/data/wow/media/guild-crest/emblem/{emblem_id}"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {
            "namespace": namespace,
        }
        return super().get_resource(resource, region, locale, query_params)

        # Housing API - Decor

    def get_decor_index(
        self, *, region: OptionalRegion = None, locale: OptionalLocale = None
    ) -> dict[str, Any]:
        """
        Return an index of decor.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the index of decor.
        """
        resource = "/data/wow/decor/index"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_decor(
        self,
        decor_id: int,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return a decor by ID.

        Args:
            decor_id (int): The ID of the decor to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the decor details.
        """
        resource = f"/data/wow/decor/{decor_id}"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def search_decor(
        self,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
        **query_params: Any,
    ) -> dict[str, Any]:
        """
        Search for decor matching the search criteria.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.
            **query_params (Any): Additional search parameters (e.g., name.en_US, orderby, _page).

        Returns:
            Dict[str, Any]: A dictionary containing paginated search results.
        """
        resource = "/data/wow/search/decor"
        query_params.update(
            {
                "namespace": f"static-{region}",
            }
        )
        return super().get_resource(resource, region, locale, query_params)

        # Housing API - Fixture

    def get_fixture_index(
        self, *, region: OptionalRegion = None, locale: OptionalLocale = None
    ) -> dict[str, Any]:
        """
        Return an index of fixtures.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the index of fixtures.
        """
        resource = "/data/wow/fixture/index"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_fixture(
        self,
        fixture_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return a fixture by ID.

        Args:
            fixture_id (int): The ID of the fixture to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the fixture details.
        """
        resource = f"/data/wow/fixture/{fixture_id}"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def search_fixture(
        self,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
        **query_params: Any,
    ) -> dict[str, Any]:
        """
        Search for fixtures matching the search criteria.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.
            **query_params (Any): Additional search parameters (e.g., name.en_US, orderby, _page).

        Returns:
            Dict[str, Any]: A dictionary containing paginated search results.
        """
        resource = "/data/wow/search/fixture"
        query_params.update(
            {
                "namespace": f"static-{region}",
            }
        )
        return super().get_resource(resource, region, locale, query_params)

        # Housing API - Fixture Hook

    def get_fixture_hook_index(
        self, *, region: OptionalRegion = None, locale: OptionalLocale = None
    ) -> dict[str, Any]:
        """
        Return an index of fixture hooks.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the index of fixture hooks.
        """
        resource = "/data/wow/fixture-hook/index"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_fixture_hook(
        self,
        fixture_hook_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return a fixture hook by ID.

        Args:
            fixture_hook_id (int): The ID of the fixture hook to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the fixture hook details.
        """
        resource = f"/data/wow/fixture-hook/{fixture_hook_id}"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def search_fixture_hook(
        self,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
        **query_params: Any,
    ) -> dict[str, Any]:
        """
        Search for fixture hooks matching the search criteria.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.
            **query_params (Any): Additional search parameters (e.g., name.en_US, orderby, _page).

        Returns:
            Dict[str, Any]: A dictionary containing paginated search results.
        """
        resource = "/data/wow/search/fixture-hook"
        query_params.update(
            {
                "namespace": f"static-{region}",
            }
        )
        return super().get_resource(resource, region, locale, query_params)

        # Housing API - Room

    def get_room_index(
        self, *, region: OptionalRegion = None, locale: OptionalLocale = None
    ) -> dict[str, Any]:
        """
        Return an index of rooms.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the index of rooms.
        """
        resource = "/data/wow/room/index"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_room(
        self,
        room_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return a room by ID.

        Args:
            room_id (int): The ID of the room to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the room details.
        """
        resource = f"/data/wow/room/{room_id}"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def search_room(
        self,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
        **query_params: Any,
    ) -> dict[str, Any]:
        """
        Search for rooms matching the search criteria.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.
            **query_params (Any): Additional search parameters (e.g., name.en_US, orderby, _page).

        Returns:
            Dict[str, Any]: A dictionary containing paginated search results.
        """
        resource = "/data/wow/search/room"
        query_params.update(
            {
                "namespace": f"static-{region}",
            }
        )
        return super().get_resource(resource, region, locale, query_params)

        # Heirloom API

    def get_heirloom_index(
        self, *, region: OptionalRegion = None, locale: OptionalLocale = None
    ) -> dict[str, Any]:
        """
        Return an index of heirlooms.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the index of heirlooms.
        """
        resource = "/data/wow/heirloom/index"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_heirloom(
        self,
        heirloom_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return an heirloom by ID.

        Args:
            heirloom_id (int): The ID of the heirloom to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the heirloom details.
        """
        resource = f"/data/wow/heirloom/{heirloom_id}"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

        # Item API

    def get_item_classes_index(
        self,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
        is_classic: bool = False,
    ) -> dict[str, Any]:
        """
        Return an index of item classes.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the index of item classes.
        """
        resource = "/data/wow/item-class/index"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {
            "namespace": namespace,
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_item_class(
        self,
        item_class_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
        is_classic: bool = False,
    ) -> dict[str, Any]:
        """
        Return an item class by ID.

        Args:
            item_class_id (int): The ID of the item class to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the item class details.
        """
        resource = f"/data/wow/item-class/{item_class_id}"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {
            "namespace": namespace,
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_item_sets_index(
        self,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
        is_classic: bool = False,
    ) -> dict[str, Any]:
        """
        Return an index of item sets.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the index of item sets.
        """
        resource = "/data/wow/item-set/index"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {
            "namespace": namespace,
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_item_set(
        self,
        item_set_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
        is_classic: bool = False,
    ) -> dict[str, Any]:
        """
        Return an item set by ID.

        Args:
            item_set_id (int): The ID of the item set to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the item set details.
        """
        resource = f"/data/wow/item-set/{item_set_id}"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {
            "namespace": namespace,
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_item_subclass(
        self,
        item_class_id: int,
        item_subclass_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
        is_classic: bool = False,
    ) -> dict[str, Any]:
        """
        Return an item subclass by ID.

        Args:
            item_class_id (int): The ID of the item class.
            item_subclass_id (int): The ID of the item subclass to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the item subclass details.
        """
        resource = (
            f"/data/wow/item-class/{item_class_id}/item-subclass/{item_subclass_id}"
        )
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {
            "namespace": namespace,
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_item(
        self,
        item_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
        is_classic: bool = False,
    ) -> dict[str, Any]:
        """
        Return an item by ID.

        Args:
            item_id (int): The ID of the item to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the item details.
        """
        resource = f"/data/wow/item/{item_id}"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {
            "namespace": namespace,
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_item_media(
        self,
        item_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
        is_classic: bool = False,
    ) -> dict[str, Any]:
        """
        Return media for an item by ID.

        Args:
            item_id (int): The ID of the item to retrieve media for.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the item media.
        """
        resource = f"/data/wow/media/item/{item_id}"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {
            "namespace": namespace,
        }
        return super().get_resource(resource, region, locale, query_params)

        # Item Appearance API

    def get_item_appearance(
        self,
        appearance_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
        is_classic: bool = False,
    ) -> dict[str, Any]:
        """
        Return an item appearance by ID.

        Args:
            appearance_id (int): The ID of the item appearance to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the item appearance details.
        """
        resource = f"/data/wow/item-appearance/{appearance_id}"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {
            "namespace": namespace,
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_item_appearance_sets_index(
        self,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
        is_classic: bool = False,
    ) -> dict[str, Any]:
        """
        Return an index of item appearance sets.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the index of item appearance sets.
        """
        resource = "/data/wow/item-appearance/set/index"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {
            "namespace": namespace,
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_item_appearance_set(
        self,
        appearance_set_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
        is_classic: bool = False,
    ) -> dict[str, Any]:
        """
        Return an item appearance set by ID.

        Args:
            appearance_set_id (int): The ID of the item appearance set to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the item appearance set details.
        """
        resource = f"/data/wow/item-appearance/set/{appearance_set_id}"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {
            "namespace": namespace,
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_item_appearance_slot_index(
        self,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
        is_classic: bool = False,
    ) -> dict[str, Any]:
        """
        Return an index of item appearance slots.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the index of item appearance slots.
        """
        resource = "/data/wow/item-appearance/slot/index"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {
            "namespace": namespace,
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_item_appearance_slot(
        self,
        slot_type: str,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
        is_classic: bool = False,
    ) -> dict[str, Any]:
        """
        Return an item appearance slot by slot type.

        Args:
            slot_type (str): The type of slot to retrieve (e.g., "head", "chest").
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the item appearance slot details.
        """
        resource = f"/data/wow/item-appearance/slot/{slot_type}"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {
            "namespace": namespace,
        }
        return super().get_resource(resource, region, locale, query_params)

    # Journal API

    def get_journal_expansions_index(
        self, *, region: OptionalRegion = None, locale: OptionalLocale = None
    ) -> dict[str, Any]:
        """
        Return an index of journal expansions.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the index of journal expansions.
        """
        resource = "/data/wow/journal-expansion/index"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_journal_expansion(
        self,
        journal_expansion_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return a journal expansion by ID.

        Args:
            journal_expansion_id (int): The ID of the journal expansion to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the journal expansion details.
        """
        resource = f"/data/wow/journal-expansion/{journal_expansion_id}"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_journal_encounters_index(
        self, *, region: OptionalRegion = None, locale: OptionalLocale = None
    ) -> dict[str, Any]:
        """
        Return an index of journal encounters.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the index of journal encounters.
        """
        resource = "/data/wow/journal-encounter/index"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_journal_encounter(
        self,
        journal_encounter_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return a journal encounter by ID.

        Args:
            journal_encounter_id (int): The ID of the journal encounter to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the journal encounter details.
        """
        resource = f"/data/wow/journal-encounter/{journal_encounter_id}"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_journal_instances_index(
        self, *, region: OptionalRegion = None, locale: OptionalLocale = None
    ) -> dict[str, Any]:
        """
        Return an index of journal instances.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the index of journal instances.
        """
        resource = "/data/wow/journal-instance/index"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_journal_instance(
        self,
        journal_instance_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return a journal instance by ID.

        Args:
            journal_instance_id (int): The ID of the journal instance to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the journal instance details.
        """
        resource = f"/data/wow/journal-instance/{journal_instance_id}"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_journal_instance_media(
        self,
        journal_instance_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return media for a journal instance by ID.

        Args:
            journal_instance_id (int): The ID of the journal instance to retrieve media for.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the journal instance media.
        """
        resource = f"/data/wow/media/journal-instance/{journal_instance_id}"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

        # Modified Crafting API

    def get_modified_crafting_index(
        self, *, region: OptionalRegion = None, locale: OptionalLocale = None
    ) -> dict[str, Any]:
        """
        Return the parent index for Modified Crafting.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the index for Modified Crafting.
        """
        resource = "/data/wow/modified-crafting/index"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_modified_crafting_category_index(
        self, *, region: OptionalRegion = None, locale: OptionalLocale = None
    ) -> dict[str, Any]:
        """
        Return the index of Modified Crafting categories.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the index of Modified Crafting categories.
        """
        resource = "/data/wow/modified-crafting/category/index"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_modified_crafting_category(
        self,
        category_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return a Modified Crafting category by ID.

        Args:
            category_id (int): The ID of the Modified Crafting category to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the Modified Crafting category details.
        """
        resource = f"/data/wow/modified-crafting/category/{category_id}"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_modified_crafting_reagent_slot_type_index(
        self, *, region: OptionalRegion = None, locale: OptionalLocale = None
    ) -> dict[str, Any]:
        """
        Return the index of Modified Crafting reagent slot types.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the index of reagent slot types.
        """
        resource = "/data/wow/modified-crafting/reagent-slot-type/index"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_modified_crafting_reagent_slot_type(
        self,
        slot_type_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return a Modified Crafting reagent slot type by ID.

        Args:
            slot_type_id (int): The ID of the reagent slot type to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the reagent slot type details.
        """
        resource = f"/data/wow/modified-crafting/reagent-slot-type/{slot_type_id}"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

        # Mount API

    def get_mounts_index(
        self, *, region: OptionalRegion = None, locale: OptionalLocale = None
    ) -> dict[str, Any]:
        """
        Return an index of mounts.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the index of mounts.
        """
        resource = "/data/wow/mount/index"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_mount(
        self,
        mount_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return a mount by ID.

        Args:
            mount_id (int): The ID of the mount to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the mount details.
        """
        resource = f"/data/wow/mount/{mount_id}"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

        # Mythic Keystone Affix API

    def get_mythic_keystone_affixes_index(
        self, *, region: OptionalRegion = None, locale: OptionalLocale = None
    ) -> dict[str, Any]:
        """
        Return an index of mythic keystone affixes.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the index of mythic keystone affixes.
        """
        resource = "/data/wow/keystone-affix/index"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_mythic_keystone_affix(
        self,
        keystone_affix_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return a mythic keystone affix by ID.

        Args:
            keystone_affix_id (int): The ID of the mythic keystone affix to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the mythic keystone affix details.
        """
        resource = f"/data/wow/keystone-affix/{keystone_affix_id}"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_mythic_keystone_affix_media(
        self,
        keystone_affix_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return media for a mythic keystone affix by ID.

        Args:
            keystone_affix_id (int): The ID of the mythic keystone affix to retrieve media for.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the mythic keystone affix media.
        """
        resource = f"/data/wow/media/keystone-affix/{keystone_affix_id}"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

        # Mythic Keystone Dungeon API

    def get_mythic_keystone_dungeons_index(
        self, *, region: OptionalRegion = None, locale: OptionalLocale = None
    ) -> dict[str, Any]:
        """
        Return an index of Mythic Keystone dungeons.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the index of Mythic Keystone dungeons.
        """
        resource = "/data/wow/mythic-keystone/dungeon/index"
        query_params = {
            "namespace": f"dynamic-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_mythic_keystone_dungeon(
        self,
        dungeon_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return a Mythic Keystone dungeon by ID.

        Args:
            dungeon_id (int): The ID of the dungeon to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the Mythic Keystone dungeon details.
        """
        resource = f"/data/wow/mythic-keystone/dungeon/{dungeon_id}"
        query_params = {
            "namespace": f"dynamic-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_mythic_keystone_index(
        self, *, region: OptionalRegion = None, locale: OptionalLocale = None
    ) -> dict[str, Any]:
        """
        Return an index of links to other documents related to Mythic Keystone dungeons.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the index of links to related documents.
        """
        resource = "/data/wow/mythic-keystone/index"
        query_params = {
            "namespace": f"dynamic-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_mythic_keystone_periods_index(
        self, *, region: OptionalRegion = None, locale: OptionalLocale = None
    ) -> dict[str, Any]:
        """
        Return an index of Mythic Keystone periods.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the index of Mythic Keystone periods.
        """
        resource = "/data/wow/mythic-keystone/period/index"
        query_params = {
            "namespace": f"dynamic-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_mythic_keystone_period(
        self,
        period_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return a Mythic Keystone period by ID.

        Args:
            period_id (int): The ID of the Mythic Keystone period to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the Mythic Keystone period details.
        """
        resource = f"/data/wow/mythic-keystone/period/{period_id}"
        query_params = {
            "namespace": f"dynamic-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_mythic_keystone_seasons_index(
        self, *, region: OptionalRegion = None, locale: OptionalLocale = None
    ) -> dict[str, Any]:
        """
        Return an index of Mythic Keystone seasons.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the index of Mythic Keystone seasons.
        """
        resource = "/data/wow/mythic-keystone/season/index"
        query_params = {
            "namespace": f"dynamic-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_mythic_keystone_season(
        self,
        season_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return a Mythic Keystone season by ID.

        Args:
            season_id (int): The ID of the Mythic Keystone season to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the Mythic Keystone season details.
        """
        resource = f"/data/wow/mythic-keystone/season/{season_id}"
        query_params = {
            "namespace": f"dynamic-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

        # Mythic Keystone Leaderboard API

    def get_mythic_keystone_leaderboards_index(
        self,
        connected_realm_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return an index of Mythic Keystone Leaderboard dungeon instances for a connected realm.

        Args:
            connected_realm_id (int): The ID of the connected realm.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the index of Mythic Keystone Leaderboard dungeon instances.
        """
        resource = (
            f"/data/wow/connected-realm/{connected_realm_id}/mythic-leaderboard/index"
        )
        query_params = {
            "namespace": f"dynamic-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_mythic_keystone_leaderboard(
        self,
        connected_realm_id: int,
        dungeon_id: int,
        period_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return a weekly Mythic Keystone Leaderboard by period.

        Args:
            connected_realm_id (int): The ID of the connected realm.
            dungeon_id (int): The ID of the dungeon.
            period_id (int): The ID of the period to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the Mythic Keystone Leaderboard details for the specified period.
        """
        resource = f"/data/wow/connected-realm/{connected_realm_id}/mythic-leaderboard/{dungeon_id}/period/{period_id}"
        query_params = {
            "namespace": f"dynamic-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

        # Mythic Raid Leaderboard API

    def get_mythic_raid_leaderboard(
        self,
        raid: str,
        faction: str,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return the leaderboard for a given raid and faction.

        Args:
            raid (str): The raid to retrieve the leaderboard for (e.g., "castle-nathria").
            faction (str): The faction to retrieve the leaderboard for (e.g., "alliance", "horde").
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the raid leaderboard details for the specified faction.
        """
        resource = f"/data/wow/leaderboard/hall-of-fame/{raid}/{faction}"
        query_params = {
            "namespace": f"dynamic-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

        # Pet API

    def get_pets_index(
        self, *, region: OptionalRegion = None, locale: OptionalLocale = None
    ) -> dict[str, Any]:
        """
        Return an index of battle pets.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the index of battle pets.
        """
        resource = "/data/wow/pet/index"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_pet(
        self,
        pet_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return a battle pet by ID.

        Args:
            pet_id (int): The ID of the battle pet to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the battle pet details.
        """
        resource = f"/data/wow/pet/{pet_id}"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_pet_media(
        self,
        pet_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return media for a battle pet by ID.

        Args:
            pet_id (int): The ID of the battle pet to retrieve media for.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the battle pet media.
        """
        resource = f"/data/wow/media/pet/{pet_id}"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_pet_abilities_index(
        self, *, region: OptionalRegion = None, locale: OptionalLocale = None
    ) -> dict[str, Any]:
        """
        Return an index of pet abilities.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the index of pet abilities.
        """
        resource = "/data/wow/pet-ability/index"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_pet_ability(
        self,
        pet_ability_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return a pet ability by ID.

        Args:
            pet_ability_id (int): The ID of the pet ability to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the pet ability details.
        """
        resource = f"/data/wow/pet-ability/{pet_ability_id}"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_pet_ability_media(
        self,
        pet_ability_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return media for a pet ability by ID.

        Args:
            pet_ability_id (int): The ID of the pet ability to retrieve media for.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the pet ability media.
        """
        resource = f"/data/wow/media/pet-ability/{pet_ability_id}"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

        # Playable Class API

    def get_playable_classes_index(
        self,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
        is_classic: bool = False,
    ) -> dict[str, Any]:
        """
        Return an index of playable classes.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the index of playable classes.
        """
        resource = "/data/wow/playable-class/index"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {
            "namespace": namespace,
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_playable_class(
        self,
        class_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
        is_classic: bool = False,
    ) -> dict[str, Any]:
        """
        Return a playable class by ID.

        Args:
            class_id (int): The ID of the playable class to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the playable class details.
        """
        resource = f"/data/wow/playable-class/{class_id}"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {
            "namespace": namespace,
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_playable_class_media(
        self,
        playable_class_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
        is_classic: bool = False,
    ) -> dict[str, Any]:
        """
        Return media for a playable class by ID.

        Args:
            playable_class_id (int): The ID of the playable class to retrieve media for.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the playable class media.
        """
        resource = f"/data/wow/media/playable-class/{playable_class_id}"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {
            "namespace": namespace,
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_pvp_talent_slots(
        self,
        class_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return the Pvp talent slots for a playable class by ID.

        Args:
            class_id (int): The ID of the playable class to retrieve PvP talent slots for.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the PvP talent slots.
        """
        resource = f"/data/wow/playable-class/{class_id}/pvp-talent-slots"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

        # Playable Race API

    def get_playable_races_index(
        self,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
        is_classic: bool = False,
    ) -> dict[str, Any]:
        """
        Return an index of playable races.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the index of playable races.
        """
        resource = "/data/wow/playable-race/index"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {
            "namespace": namespace,
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_playable_race(
        self,
        playable_race_id: int,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
        is_classic: bool = False,
    ) -> dict[str, Any]:
        """
        Return a playable race by ID.

        Args:
            playable_race_id (int): The ID of the playable race to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the playable race details.
        """
        resource = f"/data/wow/playable-race/{playable_race_id}"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {
            "namespace": namespace,
        }
        return super().get_resource(resource, region, locale, query_params)

        # Playable Specialization API

    def get_playable_specializations_index(
        self, *, region: OptionalRegion = None, locale: OptionalLocale = None
    ) -> dict[str, Any]:
        """
        Return an index of playable specializations.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the index of playable specializations.
        """
        resource = "/data/wow/playable-specialization/index"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_playable_specialization(
        self,
        spec_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return a playable specialization by ID.

        Args:
            spec_id (int): The ID of the playable specialization to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the playable specialization details.
        """
        resource = f"/data/wow/playable-specialization/{spec_id}"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_playable_specialization_media(
        self,
        spec_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return media for a playable specialization by ID.

        Args:
            spec_id (int): The ID of the playable specialization to retrieve media for.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the playable specialization media.
        """
        resource = f"/data/wow/media/playable-specialization/{spec_id}"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

        # Power Type API

    def get_power_types_index(
        self,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
        is_classic: bool = False,
    ) -> dict[str, Any]:
        """
        Return an index of power types.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the index of power types.
        """
        resource = "/data/wow/power-type/index"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {
            "namespace": namespace,
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_power_type(
        self,
        power_type_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
        is_classic: bool = False,
    ) -> dict[str, Any]:
        """
        Return a power type by ID.

        Args:
            power_type_id (int): The ID of the power type to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the power type details.
        """
        resource = f"/data/wow/power-type/{power_type_id}"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {
            "namespace": namespace,
        }
        return super().get_resource(resource, region, locale, query_params)

        # Profession API

    def get_professions_index(
        self, *, region: OptionalRegion = None, locale: OptionalLocale = None
    ) -> dict[str, Any]:
        """
        Return an index of professions.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the index of professions.
        """
        resource = "/data/wow/profession/index"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_profession(
        self,
        profession_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return a profession by ID.

        Args:
            profession_id (int): The ID of the profession to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the profession details.
        """
        resource = f"/data/wow/profession/{profession_id}"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_profession_media(
        self,
        profession_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return media for a profession by ID.

        Args:
            profession_id (int): The ID of the profession to retrieve media for.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the profession media.
        """
        resource = f"/data/wow/media/profession/{profession_id}"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_profession_skill_tier(
        self,
        profession_id: int,
        skill_tier_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return a skill tier for a profession by ID.

        Args:
            profession_id (int): The ID of the profession.
            skill_tier_id (int): The ID of the skill tier to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the skill tier details.
        """
        resource = f"/data/wow/profession/{profession_id}/skill-tier/{skill_tier_id}"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_recipe(
        self,
        recipe_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return a recipe by ID.

        Args:
            recipe_id (int): The ID of the recipe to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the recipe details.
        """
        resource = f"/data/wow/recipe/{recipe_id}"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_recipe_media(
        self,
        recipe_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return media for a recipe by ID.

        Args:
            recipe_id (int): The ID of the recipe to retrieve media for.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the recipe media.
        """
        resource = f"/data/wow/media/recipe/{recipe_id}"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

        # PvP Season API

    def get_pvp_seasons_index(
        self, *, region: OptionalRegion = None, locale: OptionalLocale = None
    ) -> dict[str, Any]:
        """
        Return an index of PvP seasons.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the index of PvP seasons.
        """
        resource = "/data/wow/pvp-season/index"
        query_params = {
            "namespace": f"dynamic-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_pvp_season(
        self,
        pvp_season_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return a PvP season by ID.

        Args:
            pvp_season_id (int): The ID of the PvP season to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the PvP season details.
        """
        resource = f"/data/wow/pvp-season/{pvp_season_id}"
        query_params = {
            "namespace": f"dynamic-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_pvp_leaderboards_index(
        self,
        pvp_season_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return an index of PvP leaderboards for a PvP season.

        Args:
            pvp_season_id (int): The ID of the PvP season.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the index of PvP leaderboards.
        """
        resource = f"/data/wow/pvp-season/{pvp_season_id}/pvp-leaderboard/index"
        query_params = {
            "namespace": f"dynamic-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_pvp_leaderboard(
        self,
        pvp_season_id: int,
        pvp_bracket: str,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return the PvP leaderboard of a specific PvP bracket for a PvP season.

        Args:
            pvp_season_id (int): The ID of the PvP season.
            pvp_bracket (str): The PvP bracket to retrieve (e.g., "2v2", "3v3").
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the PvP leaderboard details.
        """
        resource = f"/data/wow/pvp-season/{pvp_season_id}/pvp-leaderboard/{pvp_bracket}"
        query_params = {
            "namespace": f"dynamic-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_pvp_rewards_index(
        self,
        pvp_season_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return an index of PvP rewards for a PvP season.

        Args:
            pvp_season_id (int): The ID of the PvP season.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the index of PvP rewards.
        """
        resource = f"/data/wow/pvp-season/{pvp_season_id}/pvp-reward/index"
        query_params = {
            "namespace": f"dynamic-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

        # PvP Tier API

    def get_pvp_tier_media(
        self,
        pvp_tier_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return media for a PvP tier by ID.

        Args:
            pvp_tier_id (int): The ID of the PvP tier to retrieve media for.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the PvP tier media.
        """
        resource = f"/data/wow/media/pvp-tier/{pvp_tier_id}"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_pvp_tiers_index(
        self, *, region: OptionalRegion = None, locale: OptionalLocale = None
    ) -> dict[str, Any]:
        """
        Return an index of PvP tiers.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the index of PvP tiers.
        """
        resource = "/data/wow/pvp-tier/index"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_pvp_tier(
        self,
        pvp_tier_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return a PvP tier by ID.

        Args:
            pvp_tier_id (int): The ID of the PvP tier to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the PvP tier details.
        """
        resource = f"/data/wow/pvp-tier/{pvp_tier_id}"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

        # Quest API

    def get_quests_index(
        self, *, region: OptionalRegion = None, locale: OptionalLocale = None
    ) -> dict[str, Any]:
        """
        Return the parent index for quests.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the parent index for quests.
        """
        resource = "/data/wow/quest/index"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_quest(
        self,
        quest_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return a quest by ID.

        Args:
            quest_id (int): The ID of the quest to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the quest details.
        """
        resource = f"/data/wow/quest/{quest_id}"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_quest_categories_index(
        self, *, region: OptionalRegion = None, locale: OptionalLocale = None
    ) -> dict[str, Any]:
        """
        Return an index of quest categories (such as quests for a specific class, profession, or storyline).

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the index of quest categories.
        """
        resource = "/data/wow/quest/category/index"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_quest_category(
        self,
        quest_category_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return a quest category by ID.

        Args:
            quest_category_id (int): The ID of the quest category to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the quest category details.
        """
        resource = f"/data/wow/quest/category/{quest_category_id}"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_quest_areas_index(
        self, *, region: OptionalRegion = None, locale: OptionalLocale = None
    ) -> dict[str, Any]:
        """
        Return an index of quest areas.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the index of quest areas.
        """
        resource = "/data/wow/quest/area/index"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_quest_area(
        self,
        quest_area_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return a quest area by ID.

        Args:
            quest_area_id (int): The ID of the quest area to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the quest area details.
        """
        resource = f"/data/wow/quest/area/{quest_area_id}"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_quest_types_index(
        self, *, region: OptionalRegion = None, locale: OptionalLocale = None
    ) -> dict[str, Any]:
        """
        Return an index of quest types (such as PvP quests, raid quests, or account quests).

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the index of quest types.
        """
        resource = "/data/wow/quest/type/index"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_quest_type(
        self,
        quest_type_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return a quest type by ID.

        Args:
            quest_type_id (int): The ID of the quest type to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the quest type details.
        """
        resource = f"/data/wow/quest/type/{quest_type_id}"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

        # Realm API

    def get_realms_index(
        self,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
        is_classic: bool = False,
    ) -> dict[str, Any]:
        """
        Return an index of realms.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the index of realms.
        """
        resource = "/data/wow/realm/index"
        namespace = f"dynamic-classic-{region}" if is_classic else f"dynamic-{region}"
        query_params = {
            "namespace": namespace,
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_realm(
        self,
        realm_slug: str,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
        is_classic: bool = False,
    ) -> dict[str, Any]:
        """
        Return a single realm by slug or ID.

        Args:
            realm_slug (str): The slug of the realm to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the realm details.
        """
        resource = f"/data/wow/realm/{realm_slug}"
        namespace = f"dynamic-classic-{region}" if is_classic else f"dynamic-{region}"
        query_params = {
            "namespace": namespace,
        }
        return super().get_resource(resource, region, locale, query_params)

        # Region API

    def get_regions_index(
        self,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
        is_classic: bool = False,
    ) -> dict[str, Any]:
        """
        Return an index of regions.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the index of regions.
        """
        resource = "/data/wow/region/index"
        namespace = f"dynamic-classic-{region}" if is_classic else f"dynamic-{region}"
        query_params = {
            "namespace": namespace,
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_region(
        self,
        region_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
        is_classic: bool = False,
    ) -> dict[str, Any]:
        """
        Return a region by ID.

        Args:
            region_id (int): The ID of the region to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the region details.
        """
        resource = f"/data/wow/region/{region_id}"
        namespace = f"dynamic-classic-{region}" if is_classic else f"dynamic-{region}"
        query_params = {
            "namespace": namespace,
        }
        return super().get_resource(resource, region, locale, query_params)

        # Reputations API

    def get_reputation_factions_index(
        self, *, region: OptionalRegion = None, locale: OptionalLocale = None
    ) -> dict[str, Any]:
        """
        Return an index of reputation factions.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the index of reputation factions.
        """
        resource = "/data/wow/reputation-faction/index"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_reputation_faction(
        self,
        reputation_faction_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return a single reputation faction by ID.

        Args:
            reputation_faction_id (int): The ID of the reputation faction to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the reputation faction details.
        """
        resource = f"/data/wow/reputation-faction/{reputation_faction_id}"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_reputation_tiers_index(
        self, *, region: OptionalRegion = None, locale: OptionalLocale = None
    ) -> dict[str, Any]:
        """
        Return an index of reputation tiers.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the index of reputation tiers.
        """
        resource = "/data/wow/reputation-tiers/index"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_reputation_tier(
        self,
        reputation_tiers_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return a single set of reputation tiers by ID.

        Args:
            reputation_tiers_id (int): The ID of the reputation tier to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the reputation tier details.
        """
        resource = f"/data/wow/reputation-tiers/{reputation_tiers_id}"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

        # Spell API

    def get_spell(
        self,
        spell_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return a spell by ID.

        Args:
            spell_id (int): The ID of the spell to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the spell details.
        """
        resource = f"/data/wow/spell/{spell_id}"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_spell_media(
        self,
        spell_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return media for a spell by ID.

        Args:
            spell_id (int): The ID of the spell to retrieve media for.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the spell media.
        """
        resource = f"/data/wow/media/spell/{spell_id}"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

        # Talent API

    def get_talents_index(
        self, *, region: OptionalRegion = None, locale: OptionalLocale = None
    ) -> dict[str, Any]:
        """
        Return an index of talents.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the index of talents.
        """
        resource = "/data/wow/talent/index"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_talent(
        self,
        talent_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return a talent by ID.

        Args:
            talent_id (int): The ID of the talent to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the talent details.
        """
        resource = f"/data/wow/talent/{talent_id}"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_pvp_talents_index(
        self, *, region: OptionalRegion = None, locale: OptionalLocale = None
    ) -> dict[str, Any]:
        """
        Return an index of PvP talents.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the index of PvP talents.
        """
        resource = "/data/wow/pvp-talent/index"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_pvp_talent(
        self,
        pvp_talent_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return a PvP talent by ID.

        Args:
            pvp_talent_id (int): The ID of the PvP talent to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the PvP talent details.
        """
        resource = f"/data/wow/pvp-talent/{pvp_talent_id}"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

        # Tech Talent API

    def get_tech_talent_tree_index(
        self, *, region: OptionalRegion = None, locale: OptionalLocale = None
    ) -> dict[str, Any]:
        """
        Return an index of tech talent trees.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the index of tech talent trees.
        """
        resource = "/data/wow/tech-talent-tree/index"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_tech_talent_tree(
        self,
        tech_talent_tree_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return a tech talent tree by ID.

        Args:
            tech_talent_tree_id (int): The ID of the tech talent tree to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the tech talent tree details.
        """
        resource = f"/data/wow/tech-talent-tree/{tech_talent_tree_id}"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_tech_talent_index(
        self, *, region: OptionalRegion = None, locale: OptionalLocale = None
    ) -> dict[str, Any]:
        """
        Return an index of tech talents.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the index of tech talents.
        """
        resource = "/data/wow/tech-talent/index"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_tech_talent(
        self,
        tech_talent_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return a tech talent by ID.

        Args:
            tech_talent_id (int): The ID of the tech talent to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the tech talent details.
        """
        resource = f"/data/wow/tech-talent/{tech_talent_id}"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_tech_talent_media(
        self,
        tech_talent_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return media for a tech talent by ID.

        Args:
            tech_talent_id (int): The ID of the tech talent to retrieve media for.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the tech talent media.
        """
        resource = f"/data/wow/media/tech-talent/{tech_talent_id}"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

        # Title API

    def get_titles_index(
        self, *, region: OptionalRegion = None, locale: OptionalLocale = None
    ) -> dict[str, Any]:
        """
        Return an index of titles.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the index of titles.
        """
        resource = "/data/wow/title/index"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_title(
        self,
        title_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return a title by ID.

        Args:
            title_id (int): The ID of the title to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the title details.
        """
        resource = f"/data/wow/title/{title_id}"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

        # Toy API

    def get_toy_index(
        self, *, region: OptionalRegion = None, locale: OptionalLocale = None
    ) -> dict[str, Any]:
        """
        Return an index of toys.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the index of toys.
        """
        resource = "/data/wow/toy/index"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

    def get_toy(
        self,
        toy_id: int,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return a toy by ID.

        Args:
            toy_id (int): The ID of the toy to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the toy details.
        """
        resource = f"/data/wow/toy/{toy_id}"
        query_params = {
            "namespace": f"static-{region}",
        }
        return super().get_resource(resource, region, locale, query_params)

        # Wow Token API

    def get_token_index(
        self,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
        is_classic: bool = False,
    ) -> dict[str, Any]:
        """
        Return the Wow Token index.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.ES_MX, Locale.DE_DE). Defaults to None, in which case the default locale provided at instantiation is used.
            is_classic (bool, optional): Whether to query for classic realms. Defaults to False.

        Returns:
            Dict[str, Any]: A dictionary containing the Wow Token index.
        """
        resource = "/data/wow/token/index"
        namespace = f"dynamic-classic-{region}" if is_classic else f"dynamic-{region}"
        query_params = {
            "namespace": namespace,
        }
        return super().get_resource(resource, region, locale, query_params)
