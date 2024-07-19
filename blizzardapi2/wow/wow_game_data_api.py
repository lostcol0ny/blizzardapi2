"""wow_game_data_api.py file."""

from typing import Dict, Any
from ..api import Api


class WowGameDataApi(Api):
    """All Wow Game Data API methods.

    Attributes:
        client_id: A string client id supplied by Blizzard.
        client_secret: A string client secret supplied by Blizzard.
    """

    def __init__(self, client_id: str, client_secret: str) -> None:
        """Init WowApi."""
        super().__init__(client_id, client_secret)

    # Achievement API

    def get_achievement_categories_index(
        self, region: str, locale: str
    ) -> Dict[str, Any]:
        """Return an index of achievement categories."""
        resource = "/data/wow/achievement-category/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_achievement_category(
        self, region: str, locale: str, achievement_category_id: int
    ) -> Dict[str, Any]:
        """Return an achievement category by ID."""
        resource = f"/data/wow/achievement-category/{achievement_category_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_achievements_index(self, region: str, locale: str) -> Dict[str, Any]:
        """Return an index of achievements."""
        resource = "/data/wow/achievement/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_achievement(
        self, region: str, locale: str, achievement_id: int
    ) -> Dict[str, Any]:
        """Return an achievement by ID."""
        resource = f"/data/wow/achievement/{achievement_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_achievement_media(
        self, region: str, locale: str, achievement_id: int
    ) -> Dict[str, Any]:
        """Return media for an achievement by ID."""
        resource = f"/data/wow/media/achievement/{achievement_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    # Auction House API

    def get_auction_house_index(
        self, region: str, locale: str, connected_realm_id: int
    ) -> Dict[str, Any]:
        """*CLASSIC ONLY*
        Returns an index of auction houses for a connected realm.
        """
        resource = f"/data/wow/connected-realm/{connected_realm_id}/auctions/index"
        query_params = {"namespace": f"dynamic-classic-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_auctions_for_auction_house(
        self, region: str, locale: str, connected_realm_id: int, auction_house_id: int
    ) -> Dict[str, Any]:
        """*CLASSIC ONLY*
        Returns all active auctions for a specific auction house on a connected realm.
        """
        resource = f"/data/wow/connected-realm/{connected_realm_id}/auctions/{auction_house_id}"
        query_params = {"namespace": f"dynamic-classic-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_auctions(
        self, region: str, locale: str, connected_realm_id: int
    ) -> Dict[str, Any]:
        """Return all active auctions for a connected realm."""
        resource = f"/data/wow/connected-realm/{connected_realm_id}/auctions"
        query_params = {"namespace": f"dynamic-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_commodities(self, region: str, locale: str) -> Dict[str, Any]:
        """Returns all active auctions for commodity items for the entire game region.
        Auction house data updates at a set interval. The value was initially set at 1 hour; however, it might change over time without notice.
        Depending on the number of active auctions on the specified connected realm, the response from this endpoint may be rather large, sometimes exceeding 10 MB.
        """
        resource = f"/data/wow/auctions/commodities"
        query_params = {"namespace": f"dynamic-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    # Azerite Essence API

    def get_azerite_essences_index(self, region: str, locale: str) -> Dict[str, Any]:
        """Return an index of azerite essences."""
        resource = "/data/wow/azerite-essence/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_azerite_essence(
        self, region: str, locale: str, azerite_essence_id: int
    ) -> Dict[str, Any]:
        """Return an azerite essence by ID."""
        resource = f"/data/wow/azerite-essence/{azerite_essence_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_azerite_essence_media(
        self, region: str, locale: str, azerite_essence_id: int
    ) -> Dict[str, Any]:
        """Return media for an azerite essence by ID."""
        resource = f"/data/wow/media/azerite-essence/{azerite_essence_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    # Connected Realm API

    def get_connected_realms_index(
        self, region: str, locale: str, is_classic: bool = False
    ) -> Dict[str, Any]:
        """Return an index of connected realms."""
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
    ) -> Dict[str, Any]:
        """Return a connected realm by ID."""
        resource = f"/data/wow/connected-realm/{connected_realm_id}"
        namespace = f"dynamic-classic-{region}" if is_classic else f"dynamic-{region}"
        query_params = {"namespace": namespace, "locale": locale}
        return super().get_resource(resource, region, query_params)

    # Covenant API

    def get_covenant_index(self, region: str, locale: str) -> Dict[str, Any]:
        """Return an index of covenants."""
        resource = "/data/wow/covenant/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_covenant(
        self, region: str, locale: str, covenant_id: int
    ) -> Dict[str, Any]:
        """Return a covenant by ID."""
        resource = f"/data/wow/covenant/{covenant_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_covenant_media(
        self, region: str, locale: str, covenant_id: int
    ) -> Dict[str, Any]:
        """Return media for a covenant by ID."""
        resource = f"/data/wow/media/covenant/{covenant_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_soulbind_index(self, region: str, locale: str) -> Dict[str, Any]:
        """Return an index of soulbinds."""
        resource = "/data/wow/covenant/soulbind/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_soulbind(
        self, region: str, locale: str, soulbind_id: int
    ) -> Dict[str, Any]:
        """Return a soulbind by ID."""
        resource = f"/data/wow/covenant/soulbind/{soulbind_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_conduit_index(self, region: str, locale: str) -> Dict[str, Any]:
        """Return an index of conduits."""
        resource = "/data/wow/covenant/conduit/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_conduit(self, region: str, locale: str, conduit_id: int) -> Dict[str, Any]:
        """Return a conduit by ID."""
        resource = f"/data/wow/covenant/conduit/{conduit_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    # Creature API

    def get_creature_families_index(
        self, region: str, locale: str, is_classic: bool = False
    ) -> Dict[str, Any]:
        """Return an index of creature families."""
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
    ) -> Dict[str, Any]:
        """Return a creature family by ID."""
        resource = f"/data/wow/creature-family/{creature_family_id}"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {"namespace": namespace, "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_creature_types_index(
        self, region: str, locale: str, is_classic: bool = False
    ) -> Dict[str, Any]:
        """Return an index of creature types."""
        resource = "/data/wow/creature-type/index"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {"namespace": namespace, "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_creature_type(
        self, region: str, locale: str, creature_type_id: int, is_classic: bool = False
    ) -> Dict[str, Any]:
        """Return a creature type by ID."""
        resource = f"/data/wow/creature-type/{creature_type_id}"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {"namespace": namespace, "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_creature(
        self, region: str, locale: str, creature_id: int, is_classic: bool = False
    ) -> Dict[str, Any]:
        """Return a creature by ID."""
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
    ) -> Dict[str, Any]:
        """Return media for a creature display by ID."""
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
    ) -> Dict[str, Any]:
        """Return media for a creature family by ID."""
        resource = f"/data/wow/media/creature-family/{creature_family_id}"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {"namespace": namespace, "locale": locale}
        return super().get_resource(resource, region, query_params)

    # Guild Crest API

    def get_guild_crest_components_index(
        self, region: str, locale: str, is_classic: bool = False
    ) -> Dict[str, Any]:
        """Return an index of guild crest media."""
        resource = "/data/wow/guild-crest/index"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {"namespace": namespace, "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_guild_crest_border_media(
        self, region: str, locale: str, border_id: int, is_classic: bool = False
    ) -> Dict[str, Any]:
        """Return media for a guild crest border by ID."""
        resource = f"/data/wow/media/guild-crest/border/{border_id}"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {"namespace": namespace, "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_guild_crest_emblem_media(
        self, region: str, locale: str, emblem_id: int, is_classic: bool = False
    ) -> Dict[str, Any]:
        """Return media for a guild crest emblem by ID."""
        resource = f"/data/wow/media/guild-crest/emblem/{emblem_id}"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {"namespace": namespace, "locale": locale}
        return super().get_resource(resource, region, query_params)

    # Heirloom API

    def get_heirloom_index(self, region: str, locale: str) -> Dict[str, Any]:
        """Return an index of heirlooms."""
        resource = "/data/wow/heirloom/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_heirloom(
        self, region: str, locale: str, heirloom_id: int
    ) -> Dict[str, Any]:
        """Return an heirloom by ID."""
        resource = f"/data/wow/heirloom/{heirloom_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    # Item API

    def get_item_classes_index(
        self, region: str, locale: str, is_classic: bool = False
    ) -> Dict[str, Any]:
        """Return an index of item classes."""
        resource = "/data/wow/item-class/index"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {"namespace": namespace, "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_item_class(
        self, region: str, locale: str, item_class_id: int, is_classic: bool = False
    ) -> Dict[str, Any]:
        """Return an item class by ID."""
        resource = f"/data/wow/item-class/{item_class_id}"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {"namespace": namespace, "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_item_sets_index(
        self, region: str, locale: str, is_classic: bool = False
    ) -> Dict[str, Any]:
        """Return an index of item sets."""
        resource = "/data/wow/item-set/index"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {"namespace": namespace, "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_item_set(
        self, region: str, locale: str, item_set_id: int, is_classic: bool = False
    ) -> Dict[str, Any]:
        """Return an item set by ID."""
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
    ) -> Dict[str, Any]:
        """Return an item subclass by ID."""
        resource = (
            f"/data/wow/item-class/{item_class_id}/item-subclass/{item_subclass_id}"
        )
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {"namespace": namespace, "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_item(
        self, region: str, locale: str, item_id: int, is_classic: bool = False
    ) -> Dict[str, Any]:
        """Return an item by ID."""
        resource = f"/data/wow/item/{item_id}"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {"namespace": namespace, "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_item_media(
        self, region: str, locale: str, item_id: int, is_classic: bool = False
    ) -> Dict[str, Any]:
        """Return media for an item by ID."""
        resource = f"/data/wow/media/item/{item_id}"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {"namespace": namespace, "locale": locale}
        return super().get_resource(resource, region, query_params)

    # Journal API

    def get_journal_expansions_index(self, region: str, locale: str) -> Dict[str, Any]:
        """Return an index of journal expansions."""
        resource = "/data/wow/journal-expansion/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_journal_expansion(
        self, region: str, locale: str, journal_expansion_id: int
    ) -> Dict[str, Any]:
        """Return a journal expansion by ID."""
        resource = f"/data/wow/journal-expansion/{journal_expansion_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_journal_encounters_index(self, region: str, locale: str) -> Dict[str, Any]:
        """Return an index of journal encounters."""
        resource = "/data/wow/journal-encounter/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_journal_encounter(
        self, region: str, locale: str, journal_encounter_id: int
    ) -> Dict[str, Any]:
        """Return a journal encounter by ID."""
        resource = f"/data/wow/journal-encounter/{journal_encounter_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_journal_instances_index(self, region: str, locale: str) -> Dict[str, Any]:
        """Return an index of journal instances."""
        resource = "/data/wow/journal-instance/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_journal_instance(
        self, region: str, locale: str, journal_instance_id: int
    ) -> Dict[str, Any]:
        """Return a journal instance."""
        resource = f"/data/wow/journal-instance/{journal_instance_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_journal_instance_media(
        self, region: str, locale: str, journal_instance_id: int
    ) -> Dict[str, Any]:
        """Return media for a journal instance by ID."""
        resource = f"/data/wow/media/journal-instance/{journal_instance_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    # Modified Crafting API

    def get_modified_crafting_index(self, region: str, locale: str) -> Dict[str, Any]:
        """Return the parent index for Modified Crafting."""
        resource = "/data/wow/modified-crafting/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_modified_crafting_category_index(
        self, region: str, locale: str
    ) -> Dict[str, Any]:
        """Return the index of Modified Crafting categories."""
        resource = "/data/wow/modified-crafting/category/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_modified_crafting_category(
        self, region: str, locale: str, category_id: int
    ) -> Dict[str, Any]:
        """Return the index of Modified Crafting categories."""
        resource = f"/data/wow/modified-crafting/category/{category_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_modified_crafting_reagent_slot_type_index(
        self, region: str, locale: str
    ) -> Dict[str, Any]:
        """Return the index of Modified Crafting reagent slot types."""
        resource = "/data/wow/modified-crafting/reagent-slot-type/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_modified_crafting_reagent_slot_type(
        self, region: str, locale: str, slot_type_id: int
    ) -> Dict[str, Any]:
        """Return a Modified Crafting reagent slot type by ID."""
        resource = f"/data/wow/modified-crafting/reagent-slot-type/{slot_type_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    # Mount API

    def get_mounts_index(self, region: str, locale: str) -> Dict[str, Any]:
        """Return an index of mounts."""
        resource = "/data/wow/mount/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_mount(self, region: str, locale: str, mount_id: int) -> Dict[str, Any]:
        """Return a mount by ID."""
        resource = f"/data/wow/mount/{mount_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    # Mythic Keystone Affix API

    def get_mythic_keystone_affixes_index(
        self, region: str, locale: str
    ) -> Dict[str, Any]:
        """Return an index of mythic keystone affixes."""
        resource = "/data/wow/keystone-affix/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_mythic_keystone_affix(
        self, region: str, locale: str, keystone_affix_id: int
    ) -> Dict[str, Any]:
        """Return a mythic keystone affix by ID."""
        resource = f"/data/wow/keystone-affix/{keystone_affix_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_mythic_keystone_affix_media(
        self, region: str, locale: str, keystone_affix_id: int
    ) -> Dict[str, Any]:
        """Return media for a mythic keystone affix by ID."""
        resource = f"/data/wow/media/keystone-affix/{keystone_affix_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    # Mythic Keystone Dungeon API

    def get_mythic_keystone_dungeons_index(
        self, region: str, locale: str
    ) -> Dict[str, Any]:
        """Return an index of Mythic Keystone dungeons."""
        resource = "/data/wow/mythic-keystone/dungeon/index"
        query_params = {"namespace": f"dynamic-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_mythic_keystone_dungeon(
        self, region: str, locale: str, dungeon_id: int
    ) -> Dict[str, Any]:
        """Return a Mythic Keystone dungeon by ID."""
        resource = f"/data/wow/mythic-keystone/dungeon/{dungeon_id}"
        query_params = {"namespace": f"dynamic-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_mythic_keystone_index(self, region: str, locale: str) -> Dict[str, Any]:
        """Return an index of links to other documents related to Mythic Keystone dungeons."""
        resource = "/data/wow/mythic-keystone/index"
        query_params = {"namespace": f"dynamic-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_mythic_keystone_periods_index(
        self, region: str, locale: str
    ) -> Dict[str, Any]:
        """Return an index of Mythic Keystone periods."""
        resource = "/data/wow/mythic-keystone/period/index"
        query_params = {"namespace": f"dynamic-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_mythic_keystone_period(
        self, region: str, locale: str, period_id: int
    ) -> Dict[str, Any]:
        """Return a Mythic Keystone period by ID."""
        resource = f"/data/wow/mythic-keystone/period/{period_id}"
        query_params = {"namespace": f"dynamic-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_mythic_keystone_seasons_index(
        self, region: str, locale: str
    ) -> Dict[str, Any]:
        """Return an index of Mythic Keystone seasons."""
        resource = "/data/wow/mythic-keystone/season/index"
        query_params = {"namespace": f"dynamic-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_mythic_keystone_season(
        self, region: str, locale: str, season_id: int
    ) -> Dict[str, Any]:
        """Return a Mythic Keystone season by ID."""
        resource = f"/data/wow/mythic-keystone/season/{season_id}"
        query_params = {"namespace": f"dynamic-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    # Mythic Keystone Leaderboard API

    def get_mythic_keystone_leaderboards_index(
        self, region: str, locale: str, connected_realm_id: int
    ) -> Dict[str, Any]:
        """Return an index of Mythic Keystone Leaderboard dungeon instances for a connected realm."""
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
    ) -> Dict[str, Any]:
        """Return a weekly Mythic Keystone Leaderboard by period."""
        resource = f"/data/wow/connected-realm/{connected_realm_id}/mythic-leaderboard/{dungeon_id}/period/{period_id}"
        query_params = {"namespace": f"dynamic-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    # Mythic Raid Leaderboard API

    def get_mythic_raid_leaderboard(
        self, region: str, locale: str, raid: str, faction: str
    ) -> Dict[str, Any]:
        """Return the leaderboard for a given raid and faction."""
        resource = f"/data/wow/leaderboard/hall-of-fame/{raid}/{faction}"
        query_params = {"namespace": f"dynamic-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    # Pet API

    def get_pets_index(self, region: str, locale: str) -> Dict[str, Any]:
        """Return an index of battle pets."""
        resource = "/data/wow/pet/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_pet(self, region: str, locale: str, pet_id: int) -> Dict[str, Any]:
        """Return a battle pets by ID."""
        resource = f"/data/wow/pet/{pet_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_pet_media(self, region: str, locale: str, pet_id: int) -> Dict[str, Any]:
        """Return media for a battle pet by ID."""
        resource = f"/data/wow/media/pet/{pet_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_pet_abilities_index(self, region: str, locale: str) -> Dict[str, Any]:
        """Return an index of pet abilities."""
        resource = "/data/wow/pet-ability/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_pet_ability(
        self, region: str, locale: str, pet_ability_id: int
    ) -> Dict[str, Any]:
        """Return a pet ability by ID."""
        resource = f"/data/wow/pet-ability/{pet_ability_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_pet_ability_media(
        self, region: str, locale: str, pet_ability_id: int
    ) -> Dict[str, Any]:
        """Return media for a pet ability by ID."""
        resource = f"/data/wow/media/pet-ability/{pet_ability_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    # Playable Class API

    def get_playable_classes_index(
        self, region: str, locale: str, is_classic: bool = False
    ) -> Dict[str, Any]:
        """Return an index of playable classes."""
        resource = "/data/wow/playable-class/index"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {"namespace": namespace, "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_playable_class(
        self, region: str, locale: str, class_id: int, is_classic: bool = False
    ) -> Dict[str, Any]:
        """Return a playable class by ID."""
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
    ) -> Dict[str, Any]:
        """Return media for a playable class by ID."""
        resource = f"/data/wow/media/playable-class/{playable_class_id}"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {"namespace": namespace, "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_pvp_talent_slots(
        self, region: str, locale: str, class_id: int
    ) -> Dict[str, Any]:
        """Return the Pvp talent slots for a playable class by ID."""
        resource = f"/data/wow/playable-class/{class_id}/pvp-talent-slots"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    # Playable Race API

    def get_playable_races_index(
        self, region: str, locale: str, is_classic: bool = False
    ) -> Dict[str, Any]:
        """Return an index of playable races."""
        resource = "/data/wow/playable-race/index"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {"namespace": namespace, "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_playable_race(
        self, region: str, locale: str, playable_race_id: int, is_classic: bool = False
    ) -> Dict[str, Any]:
        """Return a playable race by ID."""
        resource = f"/data/wow/playable-race/{playable_race_id}"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {"namespace": namespace, "locale": locale}
        return super().get_resource(resource, region, query_params)

    # Playable Specialization API

    def get_playable_specializations_index(
        self, region: str, locale: str
    ) -> Dict[str, Any]:
        """Return an index of playable specializations."""
        resource = "/data/wow/playable-specialization/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_playable_specialization(
        self, region: str, locale: str, spec_id: int
    ) -> Dict[str, Any]:
        """Return a playable specialization by ID."""
        resource = f"/data/wow/playable-specialization/{spec_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_playable_specialization_media(
        self, region: str, locale: str, spec_id: int
    ) -> Dict[str, Any]:
        """Return media for a playable specialization by ID."""
        resource = f"/data/wow/media/playable-specialization/{spec_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    # Power Type API

    def get_power_types_index(
        self, region: str, locale: str, is_classic: bool = False
    ) -> Dict[str, Any]:
        """Return an index of power types."""
        resource = "/data/wow/power-type/index"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {"namespace": namespace, "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_power_type(
        self, region: str, locale: str, power_type_id: int, is_classic: bool = False
    ) -> Dict[str, Any]:
        """Return a power type by ID."""
        resource = f"/data/wow/power-type/{power_type_id}"
        namespace = f"static-classic-{region}" if is_classic else f"static-{region}"
        query_params = {"namespace": namespace, "locale": locale}
        return super().get_resource(resource, region, query_params)

    # Profession API

    def get_professions_index(self, region: str, locale: str) -> Dict[str, Any]:
        """Return an index of professions."""
        resource = "/data/wow/profession/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_profession(
        self, region: str, locale: str, profession_id: int
    ) -> Dict[str, Any]:
        """Return a profession by ID."""
        resource = f"/data/wow/profession/{profession_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_profession_media(
        self, region: str, locale: str, profession_id: int
    ) -> Dict[str, Any]:
        """Return media for a profession by ID."""
        resource = f"/data/wow/media/profession/{profession_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_profession_skill_tier(
        self, region: str, locale: str, profession_id: int, skill_tier_id: int
    ) -> Dict[str, Any]:
        """Return a skill tier for a profession by ID."""
        resource = f"/data/wow/profession/{profession_id}/skill-tier/{skill_tier_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_recipe(self, region: str, locale: str, recipe_id: int) -> Dict[str, Any]:
        """Return a recipe by ID."""
        resource = f"/data/wow/recipe/{recipe_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_recipe_media(
        self, region: str, locale: str, recipe_id: int
    ) -> Dict[str, Any]:
        """Return media for a recipe by ID."""
        resource = f"/data/wow/media/recipe/{recipe_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    # Pvp Season API

    def get_pvp_seasons_index(self, region: str, locale: str) -> Dict[str, Any]:
        """Return an index of Pvp seasons."""
        resource = "/data/wow/pvp-season/index"
        query_params = {"namespace": f"dynamic-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_pvp_season(
        self, region: str, locale: str, pvp_season_id: int
    ) -> Dict[str, Any]:
        """Return a Pvp season by ID."""
        resource = f"/data/wow/pvp-season/{pvp_season_id}"
        query_params = {"namespace": f"dynamic-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_pvp_leaderboards_index(
        self, region: str, locale: str, pvp_season_id: int
    ) -> Dict[str, Any]:
        """Return an index of Pvp leaderboards for a Pvp season."""
        resource = f"/data/wow/pvp-season/{pvp_season_id}/pvp-leaderboard/index"
        query_params = {"namespace": f"dynamic-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_pvp_leaderboard(
        self, region: str, locale: str, pvp_season_id: int, pvp_bracket: str
    ) -> Dict[str, Any]:
        """Return the Pvp leaderboard of a specific Pvp bracket for a Pvp season."""
        resource = f"/data/wow/pvp-season/{pvp_season_id}/pvp-leaderboard/{pvp_bracket}"
        query_params = {"namespace": f"dynamic-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_pvp_rewards_index(
        self, region: str, locale: str, pvp_season_id: int
    ) -> Dict[str, Any]:
        """Return an index of Pvp rewards for a Pvp season."""
        resource = f"/data/wow/pvp-season/{pvp_season_id}/pvp-reward/index"
        query_params = {"namespace": f"dynamic-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    # Pvp Tier API

    def get_pvp_tier_media(
        self, region: str, locale: str, pvp_tier_id: int
    ) -> Dict[str, Any]:
        """Return media for a Pvp tier by ID."""
        resource = f"/data/wow/media/pvp-tier/{pvp_tier_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_pvp_tiers_index(self, region: str, locale: str) -> Dict[str, Any]:
        """Return an index of Pvp tiers."""
        resource = "/data/wow/pvp-tier/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_pvp_tier(
        self, region: str, locale: str, pvp_tier_id: int
    ) -> Dict[str, Any]:
        """Return a Pvp tier by ID."""
        resource = f"/data/wow/pvp-tier/{pvp_tier_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    # Quest API

    def get_quests_index(self, region: str, locale: str) -> Dict[str, Any]:
        """Return the parent index for quests."""
        resource = "/data/wow/quest/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_quest(self, region: str, locale: str, quest_id: int) -> Dict[str, Any]:
        """Return a quest by ID."""
        resource = f"/data/wow/quest/{quest_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_quest_categories_index(self, region: str, locale: str) -> Dict[str, Any]:
        """Return an index of quest categories (such as quests for a specific class, profession, or storyline)."""
        resource = "/data/wow/quest/category/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_quest_category(
        self, region: str, locale: str, quest_category_id: int
    ) -> Dict[str, Any]:
        """Return a quest category by ID."""
        resource = f"/data/wow/quest/category/{quest_category_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_quest_areas_index(self, region: str, locale: str) -> Dict[str, Any]:
        """Return an index of quest areas."""
        resource = "/data/wow/quest/area/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_quest_area(
        self, region: str, locale: str, quest_area_id: int
    ) -> Dict[str, Any]:
        """Return a quest area by ID."""
        resource = f"/data/wow/quest/area/{quest_area_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_quest_types_index(self, region: str, locale: str) -> Dict[str, Any]:
        """Return an index of quest types (such as Pvp quests, raid quests, or account quests)."""
        resource = "/data/wow/quest/type/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_quest_type(
        self, region: str, locale: str, quest_type_id: int
    ) -> Dict[str, Any]:
        """Return a quest type by ID."""
        resource = f"/data/wow/quest/type/{quest_type_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    # Realm API

    def get_realms_index(
        self, region: str, locale: str, is_classic: bool = False
    ) -> Dict[str, Any]:
        """Return an index of realms."""
        resource = "/data/wow/realm/index"
        namespace = f"dynamic-classic-{region}" if is_classic else f"dynamic-{region}"
        query_params = {"namespace": namespace, "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_realm(
        self, region: str, locale: str, realm_slug: str, is_classic: bool = False
    ) -> Dict[str, Any]:
        """Return a single realm by slug or ID."""
        resource = f"/data/wow/realm/{realm_slug}"
        namespace = f"dynamic-classic-{region}" if is_classic else f"dynamic-{region}"
        query_params = {"namespace": namespace, "locale": locale}
        return super().get_resource(resource, region, query_params)

    # Region API

    def get_regions_index(
        self, region: str, locale: str, is_classic: bool = False
    ) -> Dict[str, Any]:
        """Return an index of regions."""
        resource = "/data/wow/region/index"
        namespace = f"dynamic-classic-{region}" if is_classic else f"dynamic-{region}"
        query_params = {"namespace": namespace, "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_region(
        self, region: str, locale: str, region_id: int, is_classic: bool = False
    ) -> Dict[str, Any]:
        """Return a region by ID."""
        resource = f"/data/wow/region/{region_id}"
        namespace = f"dynamic-classic-{region}" if is_classic else f"dynamic-{region}"
        query_params = {"namespace": namespace, "locale": locale}
        return super().get_resource(resource, region, query_params)

    # Reputations API

    def get_reputation_factions_index(self, region: str, locale: str) -> Dict[str, Any]:
        """Return an index of reputation factions."""
        resource = "/data/wow/reputation-faction/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_reputation_faction(
        self, region: str, locale: str, reputation_faction_id: int
    ) -> Dict[str, Any]:
        """Return a single reputation faction by ID."""
        resource = f"/data/wow/reputation-faction/{reputation_faction_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_reputation_tiers_index(self, region: str, locale: str) -> Dict[str, Any]:
        """Return an index of reputation tiers."""
        resource = "/data/wow/reputation-tiers/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_reputation_tier(
        self, region: str, locale: str, reputation_tiers_id: int
    ) -> Dict[str, Any]:
        """Return a single set of reputation tiers by ID."""
        resource = f"/data/wow/reputation-tiers/{reputation_tiers_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    # Spell API

    def get_spell(self, region: str, locale: str, spell_id: int) -> Dict[str, Any]:
        """Return a spell by ID."""
        resource = f"/data/wow/spell/{spell_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_spell_media(
        self, region: str, locale: str, spell_id: int
    ) -> Dict[str, Any]:
        """Return media for a spell by ID."""
        resource = f"/data/wow/media/spell/{spell_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    # Talent API

    def get_talents_index(self, region: str, locale: str) -> Dict[str, Any]:
        """Return an index of talents."""
        resource = "/data/wow/talent/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_talent(self, region: str, locale: str, talent_id: int) -> Dict[str, Any]:
        """Return a talent by ID."""
        resource = f"/data/wow/talent/{talent_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_pvp_talents_index(self, region: str, locale: str) -> Dict[str, Any]:
        """Return an index of Pvp talents."""
        resource = "/data/wow/pvp-talent/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_pvp_talent(
        self, region: str, locale: str, pvp_talent_id: int
    ) -> Dict[str, Any]:
        """Return a Pvp talent by ID."""
        resource = f"/data/wow/pvp-talent/{pvp_talent_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    # Tech Talent API

    def get_tech_talent_tree_index(self, region: str, locale: str) -> Dict[str, Any]:
        """Returns an index of tech talent trees."""
        resource = "/data/wow/tech-talent-tree/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_tech_talent_tree(
        self, region: str, locale: str, tech_talent_tree_id: int
    ) -> Dict[str, Any]:
        """Return a tech talent tree by ID."""
        resource = f"/data/wow/tech-talent-tree/{tech_talent_tree_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_tech_talent_index(self, region: str, locale: str) -> Dict[str, Any]:
        """Return an index of tech talents."""
        resource = f"/data/wow/tech-talent/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_tech_talent(
        self, region: str, locale: str, tech_talent_id: int
    ) -> Dict[str, Any]:
        """Return a tech talent by ID."""
        resource = f"/data/wow/tech-talent/{tech_talent_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_tech_talent_media(
        self, region: str, locale: str, tech_talent_id: int
    ) -> Dict[str, Any]:
        """Return media for a tech talent by ID."""
        resource = f"/data/wow/media/tech-talent/{tech_talent_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    # Title API

    def get_titles_index(self, region: str, locale: str) -> Dict[str, Any]:
        """Return an index of titles."""
        resource = "/data/wow/title/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_title(self, region: str, locale: str, title_id: int) -> Dict[str, Any]:
        """Return a title by ID."""
        resource = f"/data/wow/title/{title_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    # Toy API

    def get_toy_index(self, region: str, locale: str) -> Dict[str, Any]:
        """Return an index of toys."""
        resource = "/data/wow/toy/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_toy(self, region: str, locale: str, toy_id: int) -> Dict[str, Any]:
        """Return a toy by ID."""
        resource = f"/data/wow/toy/{toy_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    # Wow Token API

    def get_token_index(
        self, region: str, locale: str, is_classic: bool = False
    ) -> Dict[str, Any]:
        """Return the Wow Token index."""
        resource = "/data/wow/token/index"
        namespace = f"dynamic-classic-{region}" if is_classic else f"dynamic-{region}"
        query_params = {"namespace": namespace, "locale": locale}
        return super().get_resource(resource, region, query_params)
