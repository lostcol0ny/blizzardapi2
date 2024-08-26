from blizzardapi2 import BlizzardApi


class TestWowGameDataApi:
    def setup_method(self):
        self.api = BlizzardApi("client_id", "client_secret")
        self.api.wow.game_data._access_token = "access_token"

    # Achievement API

    def test_get_achievements_index(self, success_response_mock):
        self.api.wow.game_data.get_achievements_index("us", "en_US")
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/achievement/index",
            params=params,
            headers=headers,
        )

    def test_get_achievement(self, success_response_mock):
        self.api.wow.game_data.get_achievement("us", "en_US", 6)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/achievement/6",
            params=params,
            headers=headers,
        )

    def test_get_achievement_categories_index(self, success_response_mock):
        self.api.wow.game_data.get_achievement_categories_index("us", "en_US")
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/achievement-category/index",
            params=params,
            headers=headers,
        )

    def test_get_achievement_category(self, success_response_mock):
        self.api.wow.game_data.get_achievement_category("us", "en_US", 81)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/achievement-category/81",
            params=params,
            headers=headers,
        )

    def test_get_achievement_media(self, success_response_mock):
        self.api.wow.game_data.get_achievement_media("us", "en_US", 6)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/media/achievement/6",
            params=params,
            headers=headers,
        )

    # Auction House API

    def test_get_auction_house_index(self, success_response_mock):
        self.api.wow.game_data.get_auction_house_index("us", "en_US", 4372)
        params = {
            "namespace": "dynamic-classic-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/connected-realm/4372/auctions/index",
            params=params,
            headers=headers,
        )

    def test_get_auctions_for_auction_house(self, success_response_mock):
        self.api.wow.game_data.get_auctions_for_auction_house("us", "en_US", 4372, 2)
        params = {
            "namespace": "dynamic-classic-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/connected-realm/4372/auctions/2",
            params=params,
            headers=headers,
        )

    def test_get_auctions(self, success_response_mock):
        self.api.wow.game_data.get_auctions("us", "en_US", 1146)
        params = {
            "namespace": "dynamic-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/connected-realm/1146/auctions",
            params=params,
            headers=headers,
        )

    def test_get_commodities(self, success_response_mock):
        self.api.wow.game_data.get_commodities("us", "en_US")
        params = {
            "namespace": "dynamic-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/auctions/commodities",
            params=params,
            headers=headers,
        )

    # Azerite Essence API

    def test_get_azerite_essences_index(self, success_response_mock):
        self.api.wow.game_data.get_azerite_essences_index("us", "en_US")
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/azerite-essence/index",
            params=params,
            headers=headers,
        )

    def test_get_azerite_essence(self, success_response_mock):
        self.api.wow.game_data.get_azerite_essence("us", "en_US", 2)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/azerite-essence/2",
            params=params,
            headers=headers,
        )

    def test_get_azerite_essence_media(self, success_response_mock):
        self.api.wow.game_data.get_azerite_essence_media("us", "en_US", 2)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/media/azerite-essence/2",
            params=params,
            headers=headers,
        )

    # Covenant API

    def test_get_covenant_index(self, success_response_mock):
        self.api.wow.game_data.get_covenant_index("us", "en_US")
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/covenant/index",
            params=params,
            headers=headers,
        )

    def test_get_covenant(self, success_response_mock):
        self.api.wow.game_data.get_covenant("us", "en_US", 1)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/covenant/1",
            params=params,
            headers=headers,
        )

    def test_get_covenant_media(self, success_response_mock):
        self.api.wow.game_data.get_covenant_media("us", "en_US", 1)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/media/covenant/1",
            params=params,
            headers=headers,
        )

    def test_get_soulbind_index(self, success_response_mock):
        self.api.wow.game_data.get_soulbind_index("us", "en_US")
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/covenant/soulbind/index",
            params=params,
            headers=headers,
        )

    def test_get_soulbind(self, success_response_mock):
        self.api.wow.game_data.get_soulbind("us", "en_US", 1)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/covenant/soulbind/1",
            params=params,
            headers=headers,
        )

    def test_get_conduit_index(self, success_response_mock):
        self.api.wow.game_data.get_conduit_index("us", "en_US")
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/covenant/conduit/index",
            params=params,
            headers=headers,
        )

    def test_get_conduit(self, success_response_mock):
        self.api.wow.game_data.get_conduit("us", "en_US", 1)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/covenant/conduit/1",
            params=params,
            headers=headers,
        )

    # Connected Realm API

    def test_get_connected_realms_index(self, success_response_mock):
        self.api.wow.game_data.get_connected_realms_index("us", "en_US")
        params = {
            "namespace": "dynamic-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/connected-realm/index",
            params=params,
            headers=headers,
        )

    def test_get_connected_realm(self, success_response_mock):
        self.api.wow.game_data.get_connected_realm("us", "en_US", 1)
        params = {
            "namespace": "dynamic-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/connected-realm/1",
            params=params,
            headers=headers,
        )

    # Creature API

    def test_get_creature_families_index(self, success_response_mock):
        self.api.wow.game_data.get_creature_families_index("us", "en_US")
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/creature-family/index",
            params=params,
            headers=headers,
        )

    def test_get_creature_family(self, success_response_mock):
        self.api.wow.game_data.get_creature_family("us", "en_US", 1)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/creature-family/1",
            params=params,
            headers=headers,
        )

    def test_get_creature_types_index(self, success_response_mock):
        self.api.wow.game_data.get_creature_types_index("us", "en_US")
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/creature-type/index",
            params=params,
            headers=headers,
        )

    def test_get_creature_type(self, success_response_mock):
        self.api.wow.game_data.get_creature_type("us", "en_US", 1)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/creature-type/1",
            params=params,
            headers=headers,
        )

    def test_get_creature(self, success_response_mock):
        self.api.wow.game_data.get_creature("us", "en_US", 1)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/creature/1",
            params=params,
            headers=headers,
        )

    def test_get_creature_display_media(self, success_response_mock):
        self.api.wow.game_data.get_creature_display_media("us", "en_US", 1)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/media/creature-display/1",
            params=params,
            headers=headers,
        )

    def test_get_creature_family_media(self, success_response_mock):
        self.api.wow.game_data.get_creature_family_media("us", "en_US", 1)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/media/creature-family/1",
            params=params,
            headers=headers,
        )

    # Guild Crest API

    def test_get_guild_crest_components_index(self, success_response_mock):
        self.api.wow.game_data.get_guild_crest_components_index("us", "en_US")
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/guild-crest/index",
            params=params,
            headers=headers,
        )

    def test_get_guild_crest_border_media(self, success_response_mock):
        self.api.wow.game_data.get_guild_crest_border_media("us", "en_US", 0)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/media/guild-crest/border/0",
            params=params,
            headers=headers,
        )

    def test_get_guild_crest_emblem_media(self, success_response_mock):
        self.api.wow.game_data.get_guild_crest_emblem_media("us", "en_US", 0)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/media/guild-crest/emblem/0",
            params=params,
            headers=headers,
        )

    # Heirloom API
    def test_get_heirloom_index(self, success_response_mock):
        self.api.wow.game_data.get_heirloom_index("us", "en_US")
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/heirloom/index",
            params=params,
            headers=headers,
        )

    def test_get_heirloom(self, success_response_mock):
        self.api.wow.game_data.get_heirloom("us", "en_US", 1)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/heirloom/1",
            params=params,
            headers=headers,
        )

    # Item API

    def test_get_item_classes_index(self, success_response_mock):
        self.api.wow.game_data.get_item_classes_index("us", "en_US")
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/item-class/index",
            params=params,
            headers=headers,
        )

    def test_get_item_class(self, success_response_mock):
        self.api.wow.game_data.get_item_class("us", "en_US", 2)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/item-class/2",
            params=params,
            headers=headers,
        )

    def test_get_item_sets_index(self, success_response_mock):
        self.api.wow.game_data.get_item_sets_index("us", "en_US")
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/item-set/index",
            params=params,
            headers=headers,
        )

    def test_get_item_set(self, success_response_mock):
        self.api.wow.game_data.get_item_set("us", "en_US", 1)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/item-set/1",
            params=params,
            headers=headers,
        )

    def test_get_item_subclass(self, success_response_mock):
        self.api.wow.game_data.get_item_subclass("us", "en_US", 2, 1)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/item-class/2/item-subclass/1",
            params=params,
            headers=headers,
        )

    def test_get_item(self, success_response_mock):
        self.api.wow.game_data.get_item("us", "en_US", 9999)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/item/9999",
            params=params,
            headers=headers,
        )

    def test_get_item_media(self, success_response_mock):
        self.api.wow.game_data.get_item_media("us", "en_US", 9999)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/media/item/9999",
            params=params,
            headers=headers,
        )

    # Item Appearance API

    def test_get_item_appearance(self, success_response_mock):
        self.api.wow.game_data.get_item_appearance("us", "en_US", 1)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/item-appearance/1",
            params=params,
            headers=headers,
        )

    def test_get_item_appearance_sets_index(self, success_response_mock):
        self.api.wow.game_data.get_item_appearance_sets_index("us", "en_US")
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/item-appearance/set/index",
            params=params,
            headers=headers,
        )

    def test_get_item_appearance_set(self, success_response_mock):
        self.api.wow.game_data.get_item_appearance_set("us", "en_US", 1)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/item-appearance/set/1",
            params=params,
            headers=headers,
        )

    def test_get_item_appearance_slot_index(self, success_response_mock):
        self.api.wow.game_data.get_item_appearance_slot_index("us", "en_US")
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/item-appearance/slot/index",
            params=params,
            headers=headers,
        )

    def test_get_item_appearance_slot(self, success_response_mock):
        self.api.wow.game_data.get_item_appearance_slot("us", "en_US", 1)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/item-appearance/slot/1",
            params=params,
            headers=headers,
        )

    # Journal API

    def test_get_journal_expansions_index(self, success_response_mock):
        self.api.wow.game_data.get_journal_expansions_index("us", "en_US")
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/journal-expansion/index",
            params=params,
            headers=headers,
        )

    def test_get_journal_expansion(self, success_response_mock):
        self.api.wow.game_data.get_journal_expansion("us", "en_US", 68)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/journal-expansion/68",
            params=params,
            headers=headers,
        )

    def test_get_journal_encounters_index(self, success_response_mock):
        self.api.wow.game_data.get_journal_encounters_index("us", "en_US")
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/journal-encounter/index",
            params=params,
            headers=headers,
        )

    def test_get_journal_encounter(self, success_response_mock):
        self.api.wow.game_data.get_journal_encounter("us", "en_US", 89)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/journal-encounter/89",
            params=params,
            headers=headers,
        )

    def test_get_journal_instances_index(self, success_response_mock):
        self.api.wow.game_data.get_journal_instances_index("us", "en_US")
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/journal-instance/index",
            params=params,
            headers=headers,
        )

    def test_get_journal_instance(self, success_response_mock):
        self.api.wow.game_data.get_journal_instance("us", "en_US", 63)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/journal-instance/63",
            params=params,
            headers=headers,
        )

    def test_get_journal_instance_media(self, success_response_mock):
        self.api.wow.game_data.get_journal_instance_media("us", "en_US", 63)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/media/journal-instance/63",
            params=params,
            headers=headers,
        )

    # Modified Crafting API

    def test_get_modified_crafting_index(self, success_response_mock):
        self.api.wow.game_data.get_modified_crafting_index("us", "en_US")
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/modified-crafting/index",
            params=params,
            headers=headers,
        )

    def test_get_modified_crafting_category_index(self, success_response_mock):
        self.api.wow.game_data.get_modified_crafting_category_index("us", "en_US")
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/modified-crafting/category/index",
            params=params,
            headers=headers,
        )

    def test_get_modified_crafting_category(self, success_response_mock):
        self.api.wow.game_data.get_modified_crafting_category("us", "en_US", 1)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/modified-crafting/category/1",
            params=params,
            headers=headers,
        )

    def test_get_modified_crafting_reagent_slot_type_index(self, success_response_mock):
        self.api.wow.game_data.get_modified_crafting_reagent_slot_type_index(
            "us", "en_US"
        )
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/modified-crafting/reagent-slot-type/index",
            params=params,
            headers=headers,
        )

    def test_get_modified_crafting_reagent_slot_type(self, success_response_mock):
        self.api.wow.game_data.get_modified_crafting_reagent_slot_type(
            "us", "en_US", 16
        )
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/modified-crafting/reagent-slot-type/16",
            params=params,
            headers=headers,
        )

    # Mount API

    def test_get_mounts_index(self, success_response_mock):
        self.api.wow.game_data.get_mounts_index("us", "en_US")
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/mount/index",
            params=params,
            headers=headers,
        )

    def test_get_mount(self, success_response_mock):
        self.api.wow.game_data.get_mount("us", "en_US", 6)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/mount/6",
            params=params,
            headers=headers,
        )

    # Mythic Keystone Affix API

    def test_get_mythic_keystone_affixes_index(self, success_response_mock):
        self.api.wow.game_data.get_mythic_keystone_affixes_index("us", "en_US")
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/keystone-affix/index",
            params=params,
            headers=headers,
        )

    def test_get_mythic_keystone_affix(self, success_response_mock):
        self.api.wow.game_data.get_mythic_keystone_affix("us", "en_US", 3)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/keystone-affix/3",
            params=params,
            headers=headers,
        )

    def test_get_mythic_keystone_affix_media(self, success_response_mock):
        self.api.wow.game_data.get_mythic_keystone_affix_media("us", "en_US", 1)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/media/keystone-affix/1",
            params=params,
            headers=headers,
        )

    # Mythic Keystone Dungeon API

    def test_get_mythic_keystone_dungeons_index(self, success_response_mock):
        self.api.wow.game_data.get_mythic_keystone_dungeons_index("us", "en_US")
        params = {
            "namespace": "dynamic-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/mythic-keystone/dungeon/index",
            params=params,
            headers=headers,
        )

    def test_get_mythic_keystone_dungeon(self, success_response_mock):
        self.api.wow.game_data.get_mythic_keystone_dungeon("us", "en_US", 5)
        params = {
            "namespace": "dynamic-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/mythic-keystone/dungeon/5",
            params=params,
            headers=headers,
        )

    def test_get_mythic_keystone_index(self, success_response_mock):
        self.api.wow.game_data.get_mythic_keystone_index("us", "en_US")
        params = {
            "namespace": "dynamic-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/mythic-keystone/index",
            params=params,
            headers=headers,
        )

    def test_get_mythic_keystone_periods_index(self, success_response_mock):
        self.api.wow.game_data.get_mythic_keystone_periods_index("us", "en_US")
        params = {
            "namespace": "dynamic-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/mythic-keystone/period/index",
            params=params,
            headers=headers,
        )

    def test_get_mythic_keystone_period(self, success_response_mock):
        self.api.wow.game_data.get_mythic_keystone_period("us", "en_US", 641)
        params = {
            "namespace": "dynamic-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/mythic-keystone/period/641",
            params=params,
            headers=headers,
        )

    def test_get_mythic_keystone_seasons_index(self, success_response_mock):
        self.api.wow.game_data.get_mythic_keystone_seasons_index("us", "en_US")
        params = {
            "namespace": "dynamic-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/mythic-keystone/season/index",
            params=params,
            headers=headers,
        )

    def test_get_mythic_keystone_season(self, success_response_mock):
        self.api.wow.game_data.get_mythic_keystone_season("us", "en_US", 1)
        params = {
            "namespace": "dynamic-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/mythic-keystone/season/1",
            params=params,
            headers=headers,
        )

    # Mythic Keystone Leaderboard API

    def test_get_mythic_keystone_leaderboards_index(self, success_response_mock):
        self.api.wow.game_data.get_mythic_keystone_leaderboards_index("us", "en_US", 1)
        params = {
            "namespace": "dynamic-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/connected-realm/1/mythic-leaderboard/index",
            params=params,
            headers=headers,
        )

    def test_get_mythic_keystone_leaderboard(self, success_response_mock):
        self.api.wow.game_data.get_mythic_keystone_leaderboard("us", "en_US", 1, 2, 3)
        params = {
            "namespace": "dynamic-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/connected-realm/1/mythic-leaderboard/2/period/3",
            params=params,
            headers=headers,
        )

    # Mythic Raid Leaderboard API

    def test_get_mythic_raid_leaderboard(self, success_response_mock):
        self.api.wow.game_data.get_mythic_raid_leaderboard(
            "us", "en_US", "uldir", "horde"
        )
        params = {
            "namespace": "dynamic-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/leaderboard/hall-of-fame/uldir/horde",
            params=params,
            headers=headers,
        )

    # Pet API

    def test_get_pets_index(self, success_response_mock):
        self.api.wow.game_data.get_pets_index("us", "en_US")
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/pet/index",
            params=params,
            headers=headers,
        )

    def test_get_pet(self, success_response_mock):
        self.api.wow.game_data.get_pet("us", "en_US", 39)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/pet/39",
            params=params,
            headers=headers,
        )

    def test_get_pet_media(self, success_response_mock):
        self.api.wow.game_data.get_pet_media("us", "en_US", 39)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/media/pet/39",
            params=params,
            headers=headers,
        )

    def test_get_pet_abilities_index(self, success_response_mock):
        self.api.wow.game_data.get_pet_abilities_index("us", "en_US")
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/pet-ability/index",
            params=params,
            headers=headers,
        )

    def test_get_pet_ability(self, success_response_mock):
        self.api.wow.game_data.get_pet_ability("us", "en_US", 110)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/pet-ability/110",
            params=params,
            headers=headers,
        )

    def test_get_pet_ability_media(self, success_response_mock):
        self.api.wow.game_data.get_pet_ability_media("us", "en_US", 110)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/media/pet-ability/110",
            params=params,
            headers=headers,
        )

    # Playable Class API

    def test_get_playable_classes_index(self, success_response_mock):
        self.api.wow.game_data.get_playable_classes_index("us", "en_US")
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/playable-class/index",
            params=params,
            headers=headers,
        )

    def test_get_playable_class(self, success_response_mock):
        self.api.wow.game_data.get_playable_class("us", "en_US", 7)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/playable-class/7",
            params=params,
            headers=headers,
        )

    def test_get_playable_class_media(self, success_response_mock):
        self.api.wow.game_data.get_playable_class_media("us", "en_US", 7)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/media/playable-class/7",
            params=params,
            headers=headers,
        )

    def test_get_pvp_talent_slots(self, success_response_mock):
        self.api.wow.game_data.get_pvp_talent_slots("us", "en_US", 7)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/playable-class/7/pvp-talent-slots",
            params=params,
            headers=headers,
        )

    # Playable Race API

    def test_get_playable_races_index(self, success_response_mock):
        self.api.wow.game_data.get_playable_races_index("us", "en_US")
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/playable-race/index",
            params=params,
            headers=headers,
        )

    def test_get_playable_race(self, success_response_mock):
        self.api.wow.game_data.get_playable_race("us", "en_US", 2)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/playable-race/2",
            params=params,
            headers=headers,
        )

    # Playable Specialization API

    def test_get_playable_specializations_index(self, success_response_mock):
        self.api.wow.game_data.get_playable_specializations_index("us", "en_US")
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/playable-specialization/index",
            params=params,
            headers=headers,
        )

    def test_get_playable_specialization(self, success_response_mock):
        self.api.wow.game_data.get_playable_specialization("us", "en_US", 262)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/playable-specialization/262",
            params=params,
            headers=headers,
        )

    def test_get_playable_specialization_media(self, success_response_mock):
        self.api.wow.game_data.get_playable_specialization_media("us", "en_US", 262)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/media/playable-specialization/262",
            params=params,
            headers=headers,
        )

    # Power Type API

    def test_get_power_types_index(self, success_response_mock):
        self.api.wow.game_data.get_power_types_index("us", "en_US")
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/power-type/index",
            params=params,
            headers=headers,
        )

    def test_get_power_type(self, success_response_mock):
        self.api.wow.game_data.get_power_type("us", "en_US", 0)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/power-type/0",
            params=params,
            headers=headers,
        )

    # Profession API

    def test_get_professions_index(self, success_response_mock):
        self.api.wow.game_data.get_professions_index("us", "en_US")
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/profession/index",
            params=params,
            headers=headers,
        )

    def test_get_profession(self, success_response_mock):
        self.api.wow.game_data.get_profession("us", "en_US", 164)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/profession/164",
            params=params,
            headers=headers,
        )

    def test_get_profession_media(self, success_response_mock):
        self.api.wow.game_data.get_profession_media("us", "en_US", 164)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/media/profession/164",
            params=params,
            headers=headers,
        )

    def test_get_profession_skill_tier(self, success_response_mock):
        self.api.wow.game_data.get_profession_skill_tier("us", "en_US", 164, 2477)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/profession/164/skill-tier/2477",
            params=params,
            headers=headers,
        )

    def test_get_recipe(self, success_response_mock):
        self.api.wow.game_data.get_recipe("us", "en_US", 1631)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/recipe/1631",
            params=params,
            headers=headers,
        )

    def test_get_recipe_media(self, success_response_mock):
        self.api.wow.game_data.get_recipe_media("us", "en_US", 1631)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/media/recipe/1631",
            params=params,
            headers=headers,
        )

    # Pvp Season API

    def test_get_pvp_seasons_index(self, success_response_mock):
        self.api.wow.game_data.get_pvp_seasons_index("us", "en_US")
        params = {
            "namespace": "dynamic-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/pvp-season/index",
            params=params,
            headers=headers,
        )

    def test_get_pvp_season(self, success_response_mock):
        self.api.wow.game_data.get_pvp_season("us", "en_US", 27)
        params = {
            "namespace": "dynamic-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/pvp-season/27",
            params=params,
            headers=headers,
        )

    def test_get_pvp_leaderboards_index(self, success_response_mock):
        self.api.wow.game_data.get_pvp_leaderboards_index("us", "en_US", 27)
        params = {
            "namespace": "dynamic-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/pvp-season/27/pvp-leaderboard/index",
            params=params,
            headers=headers,
        )

    def test_get_pvp_leaderboard(self, success_response_mock):
        self.api.wow.game_data.get_pvp_leaderboard("us", "en_US", 27, "3v3")
        params = {
            "namespace": "dynamic-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/pvp-season/27/pvp-leaderboard/3v3",
            params=params,
            headers=headers,
        )

    def test_get_pvp_rewards_index(self, success_response_mock):
        self.api.wow.game_data.get_pvp_rewards_index("us", "en_US", 27)
        params = {
            "namespace": "dynamic-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/pvp-season/27/pvp-reward/index",
            params=params,
            headers=headers,
        )

    # Pvp Tier API

    def test_get_pvp_tier_media(self, success_response_mock):
        self.api.wow.game_data.get_pvp_tier_media("us", "en_US", 1)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/media/pvp-tier/1",
            params=params,
            headers=headers,
        )

    def test_get_pvp_tiers_index(self, success_response_mock):
        self.api.wow.game_data.get_pvp_tiers_index("us", "en_US")
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/pvp-tier/index",
            params=params,
            headers=headers,
        )

    def test_get_pvp_tier(self, success_response_mock):
        self.api.wow.game_data.get_pvp_tier("us", "en_US", 1)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/pvp-tier/1",
            params=params,
            headers=headers,
        )

    # Quest API

    def test_get_quests_index(self, success_response_mock):
        self.api.wow.game_data.get_quests_index("us", "en_US")
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/quest/index",
            params=params,
            headers=headers,
        )

    def test_get_quest(self, success_response_mock):
        self.api.wow.game_data.get_quest("us", "en_US", 2)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/quest/2",
            params=params,
            headers=headers,
        )

    def test_get_quest_categories_index(self, success_response_mock):
        self.api.wow.game_data.get_quest_categories_index("us", "en_US")
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/quest/category/index",
            params=params,
            headers=headers,
        )

    def test_get_quest_category(self, success_response_mock):
        self.api.wow.game_data.get_quest_category("us", "en_US", 1)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/quest/category/1",
            params=params,
            headers=headers,
        )

    def test_get_quest_areas_index(self, success_response_mock):
        self.api.wow.game_data.get_quest_areas_index("us", "en_US")
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/quest/area/index",
            params=params,
            headers=headers,
        )

    def test_get_quest_area(self, success_response_mock):
        self.api.wow.game_data.get_quest_area("us", "en_US", 1)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/quest/area/1",
            params=params,
            headers=headers,
        )

    def test_get_quest_types_index(self, success_response_mock):
        self.api.wow.game_data.get_quest_types_index("us", "en_US")
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/quest/type/index",
            params=params,
            headers=headers,
        )

    def test_get_quest_type(self, success_response_mock):
        self.api.wow.game_data.get_quest_type("us", "en_US", 1)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/quest/type/1",
            params=params,
            headers=headers,
        )

    # Realm API

    def test_get_realms_index(self, success_response_mock):
        self.api.wow.game_data.get_realms_index("us", "en_US")
        params = {
            "namespace": "dynamic-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/realm/index",
            params=params,
            headers=headers,
        )

    def test_get_realm(self, success_response_mock):
        self.api.wow.game_data.get_realm("us", "en_US", "tichondrius")
        params = {
            "namespace": "dynamic-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/realm/tichondrius",
            params=params,
            headers=headers,
        )

    # Region API

    def test_get_regions_index(self, success_response_mock):
        self.api.wow.game_data.get_regions_index("us", "en_US")
        params = {
            "namespace": "dynamic-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/region/index",
            params=params,
            headers=headers,
        )

    def test_get_region(self, success_response_mock):
        self.api.wow.game_data.get_region("us", "en_US", 1)
        params = {
            "namespace": "dynamic-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/region/1",
            params=params,
            headers=headers,
        )

    # Reputations API

    def test_get_reputation_factions_index(self, success_response_mock):
        self.api.wow.game_data.get_reputation_factions_index("us", "en_US")
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/reputation-faction/index",
            params=params,
            headers=headers,
        )

    def test_get_reputation_faction(self, success_response_mock):
        self.api.wow.game_data.get_reputation_faction("us", "en_US", 21)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/reputation-faction/21",
            params=params,
            headers=headers,
        )

    def test_get_reputation_tiers_index(self, success_response_mock):
        self.api.wow.game_data.get_reputation_tiers_index("us", "en_US")
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/reputation-tiers/index",
            params=params,
            headers=headers,
        )

    def test_get_reputation_tier(self, success_response_mock):
        self.api.wow.game_data.get_reputation_tier("us", "en_US", 2)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/reputation-tiers/2",
            params=params,
            headers=headers,
        )

    # Spell API

    def test_get_spell(self, success_response_mock):
        self.api.wow.game_data.get_spell("us", "en_US", 196607)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/spell/196607",
            params=params,
            headers=headers,
        )

    def test_get_spell_media(self, success_response_mock):
        self.api.wow.game_data.get_spell_media("us", "en_US", 196607)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/media/spell/196607",
            params=params,
            headers=headers,
        )

    # Talent API

    def test_get_talents_index(self, success_response_mock):
        self.api.wow.game_data.get_talents_index("us", "en_US")
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/talent/index",
            params=params,
            headers=headers,
        )

    def test_get_talent(self, success_response_mock):
        self.api.wow.game_data.get_talent("us", "en_US", 23106)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/talent/23106",
            params=params,
            headers=headers,
        )

    def test_get_pvp_talents_index(self, success_response_mock):
        self.api.wow.game_data.get_pvp_talents_index("us", "en_US")
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/pvp-talent/index",
            params=params,
            headers=headers,
        )

    def test_get_pvp_talent(self, success_response_mock):
        self.api.wow.game_data.get_pvp_talent("us", "en_US", 3)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/pvp-talent/3",
            params=params,
            headers=headers,
        )

    # Tech Talent API

    def test_get_tech_talent_tree_index(self, success_response_mock):
        self.api.wow.game_data.get_tech_talent_tree_index("us", "en_US")
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/tech-talent-tree/index",
            params=params,
            headers=headers,
        )

    def test_get_tech_talent_tree(self, success_response_mock):
        self.api.wow.game_data.get_tech_talent_tree("us", "en_US", 1)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/tech-talent-tree/1",
            params=params,
            headers=headers,
        )

    def test_get_tech_talent_index(self, success_response_mock):
        self.api.wow.game_data.get_tech_talent_index("us", "en_US")
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/tech-talent/index",
            params=params,
            headers=headers,
        )

    def test_get_tech_talent(self, success_response_mock):
        self.api.wow.game_data.get_tech_talent("us", "en_US", 1)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/tech-talent/1",
            params=params,
            headers=headers,
        )

    def test_get_tech_talent_media(self, success_response_mock):
        self.api.wow.game_data.get_tech_talent_media("us", "en_US", 1)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/media/tech-talent/1",
            params=params,
            headers=headers,
        )

    # Toy API

    def test_get_toy_index(self, success_response_mock):
        self.api.wow.game_data.get_toy_index("us", "en_US")
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/toy/index",
            params=params,
            headers=headers,
        )

    def test_get_toy(self, success_response_mock):
        self.api.wow.game_data.get_toy("us", "en_US", 1)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/toy/1", params=params, headers=headers
        )

    # Title API

    def test_get_titles_index(self, success_response_mock):
        self.api.wow.game_data.get_titles_index("us", "en_US")
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/title/index",
            params=params,
            headers=headers,
        )

    def test_get_title(self, success_response_mock):
        self.api.wow.game_data.get_title("us", "en_US", 1)
        params = {
            "namespace": "static-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/title/1",
            params=params,
            headers=headers,
        )

    # Wow Token API

    def test_get_tokens_index(self, success_response_mock):
        self.api.wow.game_data.get_token_index("us", "en_US")
        params = {
            "namespace": "dynamic-us",
            "locale": "en_US",
        }
        headers = {"Authorization": "Bearer access_token"}
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/token/index",
            params=params,
            headers=headers,
        )
