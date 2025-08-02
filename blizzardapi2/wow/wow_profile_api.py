"""wow_profile_api.py file."""

from typing import Any

from ..api import BaseApi


class WowProfileApi(BaseApi):
    """All Wow Profile API methods.

    Attributes:
        client_id (str): A string client ID supplied by Blizzard.
        client_secret (str): A string client secret supplied by Blizzard.
    """

    def __init__(self, client_id: str, client_secret: str) -> None:
        """
        Initialize the WowProfileApi class.

        Args:
            client_id (str): The client ID supplied by Blizzard.
            client_secret (str): The client secret supplied by Blizzard.
        """
        super().__init__(client_id, client_secret)

    def get_account_profile_summary(
        self, region: str, locale: str, access_token: str
    ) -> dict[str, Any]:
        """
        Return a profile summary for an account.

        Args:
            region (str): The region to query (e.g., "us", "eu").
            locale (str): The locale to use for the response.
            access_token (str): The access token for authorization.

        Returns:
            Dict[str, Any]: A dictionary containing the account profile summary.
        """
        resource = "/profile/user/wow"
        query_params = {
            "namespace": f"profile-{region}",
            "locale": locale,
            "access_token": access_token,
        }
        return super().get_oauth_resource(resource, region, query_params)

    def get_protected_character_profile_summary(
        self,
        region: str,
        locale: str,
        access_token: str,
        realm_id: int,
        character_id: int,
    ) -> dict[str, Any]:
        """
        Return a protected profile summary for a character.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            access_token (str): The access token for authorization.
            realm_id (int): The ID of the realm.
            character_id (int): The ID of the character.

        Returns:
            Dict[str, Any]: A dictionary containing the protected character profile summary.
        """
        resource = f"/profile/user/wow/protected-character/{realm_id}-{character_id}"
        query_params = {
            "namespace": f"profile-{region}",
            "locale": locale,
            "access_token": access_token,
        }
        return super().get_resource(resource, region, query_params)

    def get_account_collections_index(
        self, region: str, locale: str, access_token: str
    ) -> dict[str, Any]:
        """
        Return an index of collection types for an account.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            access_token (str): The access token for authorization.

        Returns:
            Dict[str, Any]: A dictionary containing the index of collection types.
        """
        resource = "/profile/user/wow/collections"
        query_params = {
            "namespace": f"profile-{region}",
            "locale": locale,
            "access_token": access_token,
        }
        return super().get_resource(resource, region, query_params)

    def get_account_heirlooms_collection_summary(
        self, region: str, locale: str, access_token: str
    ) -> dict[str, Any]:
        """
        Return a summary of the heirlooms an account has obtained.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            access_token (str): The access token for authorization.

        Returns:
            Dict[str, Any]: A dictionary containing the heirlooms collection summary.
        """
        resource = "/profile/user/wow/collections/heirlooms"
        query_params = {
            "namespace": f"profile-{region}",
            "locale": locale,
            "access_token": access_token,
        }
        return super().get_resource(resource, region, query_params)

    def get_account_mounts_collection_summary(
        self, region: str, locale: str, access_token: str
    ) -> dict[str, Any]:
        """
        Return a summary of the mounts an account has obtained.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            access_token (str): The access token for authorization.

        Returns:
            Dict[str, Any]: A dictionary containing the mounts collection summary.
        """
        resource = "/profile/user/wow/collections/mounts"
        query_params = {
            "namespace": f"profile-{region}",
            "locale": locale,
            "access_token": access_token,
        }
        return super().get_resource(resource, region, query_params)

    def get_account_pets_collection_summary(
        self, region: str, locale: str, access_token: str
    ) -> dict[str, Any]:
        """
        Return a summary of the battle pets an account has obtained.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            access_token (str): The access token for authorization.

        Returns:
            Dict[str, Any]: A dictionary containing the pets collection summary.
        """
        resource = "/profile/user/wow/collections/pets"
        query_params = {
            "namespace": f"profile-{region}",
            "locale": locale,
            "access_token": access_token,
        }
        return super().get_resource(resource, region, query_params)

    def get_account_toys_collection_summary(
        self, region: str, locale: str, access_token: str
    ) -> dict[str, Any]:
        """
        Return a summary of the toys an account has obtained.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            access_token (str): The access token for authorization.

        Returns:
            Dict[str, Any]: A dictionary containing the toys collection summary.
        """
        resource = "/profile/user/wow/collections/toys"
        query_params = {
            "namespace": f"profile-{region}",
            "locale": locale,
            "access_token": access_token,
        }
        return super().get_resource(resource, region, query_params)

    def get_account_transmog_collection_summary(
        self, region: str, locale: str, access_token: str
    ) -> dict[str, Any]:
        """
        Return a summary of the transmog appearances an account has obtained.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            access_token (str): The access token for authorization.

        Returns:
            Dict[str, Any]: A dictionary containing the transmog collection summary.
        """
        resource = "/profile/user/wow/collections/transmogs"
        query_params = {
            "namespace": f"profile-{region}",
            "locale": locale,
            "access_token": access_token,
        }
        return super().get_resource(resource, region, query_params)

    def get_character_achievements_summary(
        self, region: str, locale: str, realm_slug: str, character_name: str
    ) -> dict[str, Any]:
        """
        Return a summary of the achievements a character has completed.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            realm_slug (str): The slug of the realm.
            character_name (str): The name of the character.

        Returns:
            Dict[str, Any]: A dictionary containing the character's achievements summary.
        """
        resource = f"/profile/wow/character/{realm_slug}/{character_name}/achievements"
        query_params = {"namespace": f"profile-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_character_achievement_statistics(
        self, region: str, locale: str, realm_slug: str, character_name: str
    ) -> dict[str, Any]:
        """
        Return a character's statistics as they pertain to achievements.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            realm_slug (str): The slug of the realm.
            character_name (str): The name of the character.

        Returns:
            Dict[str, Any]: A dictionary containing the character's achievement statistics.
        """
        resource = f"/profile/wow/character/{realm_slug}/{character_name}/achievements/statistics"
        query_params = {"namespace": f"profile-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_character_appearance_summary(
        self, region: str, locale: str, realm_slug: str, character_name: str
    ) -> dict[str, Any]:
        """
        Return a summary of a character's appearance settings.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            realm_slug (str): The slug of the realm.
            character_name (str): The name of the character.

        Returns:
            Dict[str, Any]: A dictionary containing the character's appearance summary.
        """
        resource = f"/profile/wow/character/{realm_slug}/{character_name}/appearance"
        query_params = {"namespace": f"profile-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_character_collections_index(
        self, region: str, locale: str, realm_slug: str, character_name: str
    ) -> dict[str, Any]:
        """
        Return an index of collection types for a character.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            realm_slug (str): The slug of the realm.
            character_name (str): The name of the character.

        Returns:
            Dict[str, Any]: A dictionary containing the index of collection types for the character.
        """
        resource = f"/profile/wow/character/{realm_slug}/{character_name}/collections"
        query_params = {"namespace": f"profile-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_character_heirlooms_collection_summary(
        self, region: str, locale: str, realm_slug: str, character_name: str
    ) -> dict[str, Any]:
        """
        Return a summary of the heirlooms a character has obtained.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            realm_slug (str): The slug of the realm.
            character_name (str): The name of the character.

        Returns:
            Dict[str, Any]: A dictionary containing the character's heirlooms collection summary.
        """
        resource = f"/profile/wow/character/{realm_slug}/{character_name}/collections/heirlooms"
        query_params = {"namespace": f"profile-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_character_mounts_collection_summary(
        self, region: str, locale: str, realm_slug: str, character_name: str
    ) -> dict[str, Any]:
        """
        Return a summary of the mounts a character has obtained.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            realm_slug (str): The slug of the realm.
            character_name (str): The name of the character.

        Returns:
            Dict[str, Any]: A dictionary containing the character's mounts collection summary.
        """
        resource = (
            f"/profile/wow/character/{realm_slug}/{character_name}/collections/mounts"
        )
        query_params = {"namespace": f"profile-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_character_pets_collection_summary(
        self, region: str, locale: str, realm_slug: str, character_name: str
    ) -> dict[str, Any]:
        """
        Return a summary of the battle pets a character has obtained.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            realm_slug (str): The slug of the realm.
            character_name (str): The name of the character.

        Returns:
            Dict[str, Any]: A dictionary containing the character's pets collection summary.
        """
        resource = (
            f"/profile/wow/character/{realm_slug}/{character_name}/collections/pets"
        )
        query_params = {"namespace": f"profile-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_character_toys_collection_summary(
        self, region: str, locale: str, realm_slug: str, character_name: str
    ) -> dict[str, Any]:
        """
        Return a summary of the toys a character has obtained.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            realm_slug (str): The slug of the realm.
            character_name (str): The name of the character.

        Returns:
            Dict[str, Any]: A dictionary containing the character's toys collection summary.
        """
        resource = (
            f"/profile/wow/character/{realm_slug}/{character_name}/collections/toys"
        )
        query_params = {"namespace": f"profile-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_character_transmog_collection_summary(
        self, region: str, locale: str, realm_slug: str, character_name: str
    ) -> dict[str, Any]:
        """
        Return a summary of the transmog appearances a character has obtained.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            realm_slug (str): The slug of the realm.
            character_name (str): The name of the character.

        Returns:
            Dict[str, Any]: A dictionary containing the character's transmog collection summary.
        """
        resource = f"/profile/wow/character/{realm_slug}/{character_name}/collections/transmogs"
        query_params = {"namespace": f"profile-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_character_encounters_summary(
        self, region: str, locale: str, realm_slug: str, character_name: str
    ) -> dict[str, Any]:
        """
        Return a summary of a character's encounters.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            realm_slug (str): The slug of the realm.
            character_name (str): The name of the character.

        Returns:
            Dict[str, Any]: A dictionary containing the character's encounters summary.
        """
        resource = f"/profile/wow/character/{realm_slug}/{character_name}/encounters"
        query_params = {"namespace": f"profile-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_character_dungeons(
        self, region: str, locale: str, realm_slug: str, character_name: str
    ) -> dict[str, Any]:
        """
        Return a summary of a character's completed dungeons.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            realm_slug (str): The slug of the realm.
            character_name (str): The name of the character.

        Returns:
            Dict[str, Any]: A dictionary containing the character's dungeons summary.
        """
        resource = (
            f"/profile/wow/character/{realm_slug}/{character_name}/encounters/dungeons"
        )
        query_params = {"namespace": f"profile-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_character_raids(
        self, region: str, locale: str, realm_slug: str, character_name: str
    ) -> dict[str, Any]:
        """
        Return a summary of a character's completed raids.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            realm_slug (str): The slug of the realm.
            character_name (str): The name of the character.

        Returns:
            Dict[str, Any]: A dictionary containing the character's raids summary.
        """
        resource = (
            f"/profile/wow/character/{realm_slug}/{character_name}/encounters/raids"
        )
        query_params = {"namespace": f"profile-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_character_equipment_summary(
        self, region: str, locale: str, realm_slug: str, character_name: str
    ) -> dict[str, Any]:
        """
        Return a summary of the items equipped by a character.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            realm_slug (str): The slug of the realm.
            character_name (str): The name of the character.

        Returns:
            Dict[str, Any]: A dictionary containing the character's equipment summary.
        """
        resource = f"/profile/wow/character/{realm_slug}/{character_name}/equipment"
        query_params = {"namespace": f"profile-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_character_hunter_pets_summary(
        self, region: str, locale: str, realm_slug: str, character_name: str
    ) -> dict[str, Any]:
        """
        If the character is a hunter, return a summary of the character's hunter pets.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            realm_slug (str): The slug of the realm.
            character_name (str): The name of the character.

        Returns:
            Dict[str, Any]: A dictionary containing the hunter pets summary.
        """
        resource = f"/profile/wow/character/{realm_slug}/{character_name}/hunter-pets"
        query_params = {"namespace": f"profile-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_character_media_summary(
        self, region: str, locale: str, realm_slug: str, character_name: str
    ) -> dict[str, Any]:
        """
        Return a summary of the media assets available for a character (such as an avatar render).

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            realm_slug (str): The slug of the realm.
            character_name (str): The name of the character.

        Returns:
            Dict[str, Any]: A dictionary containing the media assets summary.
        """
        resource = (
            f"/profile/wow/character/{realm_slug}/{character_name}/character-media"
        )
        query_params = {"namespace": f"profile-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_character_mythic_keystone_profile_index(
        self, region: str, locale: str, realm_slug: str, character_name: str
    ) -> dict[str, Any]:
        """
        Return the Mythic Keystone profile index for a character.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            realm_slug (str): The slug of the realm.
            character_name (str): The name of the character.

        Returns:
            Dict[str, Any]: A dictionary containing the Mythic Keystone profile index.
        """
        resource = f"/profile/wow/character/{realm_slug}/{character_name}/mythic-keystone-profile"
        query_params = {"namespace": f"profile-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_character_mythic_keystone_profile_season_details(
        self,
        region: str,
        locale: str,
        realm_slug: str,
        character_name: str,
        season_id: int,
    ) -> dict[str, Any]:
        """
        Return the Mythic Keystone season details for a character.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            realm_slug (str): The slug of the realm.
            character_name (str): The name of the character.
            season_id (int): The ID of the season.

        Returns:
            Dict[str, Any]: A dictionary containing the Mythic Keystone season details.
        """
        resource = f"/profile/wow/character/{realm_slug}/{character_name}/mythic-keystone-profile/season/{season_id}"
        query_params = {"namespace": f"profile-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_character_professions_summary(
        self, region: str, locale: str, realm_slug: str, character_name: str
    ) -> dict[str, Any]:
        """
        Return a summary of professions for a character.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            realm_slug (str): The slug of the realm.
            character_name (str): The name of the character.

        Returns:
            Dict[str, Any]: A dictionary containing the character's professions summary.
        """
        resource = f"/profile/wow/character/{realm_slug}/{character_name}/professions"
        query_params = {"namespace": f"profile-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_character_profile_summary(
        self, region: str, locale: str, realm_slug: str, character_name: str
    ) -> dict[str, Any]:
        """
        Return a profile summary for a character.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            realm_slug (str): The slug of the realm.
            character_name (str): The name of the character.

        Returns:
            Dict[str, Any]: A dictionary containing the character's profile summary.
        """
        resource = f"/profile/wow/character/{realm_slug}/{character_name}"
        query_params = {"namespace": f"profile-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_character_profile_status(
        self, region: str, locale: str, realm_slug: str, character_name: str
    ) -> dict[str, Any]:
        """
        Return the status and a unique ID for a character.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            realm_slug (str): The slug of the realm.
            character_name (str): The name of the character.

        Returns:
            Dict[str, Any]: A dictionary containing the character's status and unique ID.
        """
        resource = f"/profile/wow/character/{realm_slug}/{character_name}/status"
        query_params = {"namespace": f"profile-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_character_pvp_bracket_statistics(
        self,
        region: str,
        locale: str,
        realm_slug: str,
        character_name: str,
        pvp_bracket: str,
    ) -> dict[str, Any]:
        """
        Return the PvP bracket statistics for a character.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            realm_slug (str): The slug of the realm.
            character_name (str): The name of the character.
            pvp_bracket (str): The PvP bracket (e.g., "2v2", "3v3").

        Returns:
            Dict[str, Any]: A dictionary containing the character's PvP bracket statistics.
        """
        resource = f"/profile/wow/character/{realm_slug}/{character_name}/pvp-bracket/{pvp_bracket}"
        query_params = {"namespace": f"profile-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_character_pvp_summary(
        self, region: str, locale: str, realm_slug: str, character_name: str
    ) -> dict[str, Any]:
        """
        Return a PvP summary for a character.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            realm_slug (str): The slug of the realm.
            character_name (str): The name of the character.

        Returns:
            Dict[str, Any]: A dictionary containing the character's PvP summary.
        """
        resource = f"/profile/wow/character/{realm_slug}/{character_name}/pvp-summary"
        query_params = {"namespace": f"profile-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_character_quests(
        self, region: str, locale: str, realm_slug: str, character_name: str
    ) -> dict[str, Any]:
        """
        Return a character's active quests as well as a link to the character's completed quests.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            realm_slug (str): The slug of the realm.
            character_name (str): The name of the character.

        Returns:
            Dict[str, Any]: A dictionary containing the character's active quests and a link to completed quests.
        """
        resource = f"/profile/wow/character/{realm_slug}/{character_name}/quests"
        query_params = {"namespace": f"profile-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_character_completed_quests(
        self, region: str, locale: str, realm_slug: str, character_name: str
    ) -> dict[str, Any]:
        """
        Return a list of quests that a character has completed.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            realm_slug (str): The slug of the realm.
            character_name (str): The name of the character.

        Returns:
            Dict[str, Any]: A dictionary containing the character's completed quests.
        """
        resource = (
            f"/profile/wow/character/{realm_slug}/{character_name}/quests/completed"
        )
        query_params = {"namespace": f"profile-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_character_reputations_summary(
        self, region: str, locale: str, realm_slug: str, character_name: str
    ) -> dict[str, Any]:
        """
        Return a summary of a character's reputations.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            realm_slug (str): The slug of the realm.
            character_name (str): The name of the character.

        Returns:
            Dict[str, Any]: A dictionary containing the character's reputations summary.
        """
        resource = f"/profile/wow/character/{realm_slug}/{character_name}/reputations"
        query_params = {"namespace": f"profile-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_character_soulbinds(
        self, region: str, locale: str, realm_slug: str, character_name: str
    ) -> dict[str, Any]:
        """
        Return a summary of a character's soulbinds.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            realm_slug (str): The slug of the realm.
            character_name (str): The name of the character.

        Returns:
            Dict[str, Any]: A dictionary containing the character's soulbinds summary.
        """
        resource = f"/profile/wow/character/{realm_slug}/{character_name}/soulbinds"
        query_params = {"namespace": f"profile-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_character_specializations_summary(
        self, region: str, locale: str, realm_slug: str, character_name: str
    ) -> dict[str, Any]:
        """
        Return a summary of a character's specializations.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            realm_slug (str): The slug of the realm.
            character_name (str): The name of the character.

        Returns:
            Dict[str, Any]: A dictionary containing the character's specializations summary.
        """
        resource = (
            f"/profile/wow/character/{realm_slug}/{character_name}/specializations"
        )
        query_params = {"namespace": f"profile-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_character_statistics_summary(
        self, region: str, locale: str, realm_slug: str, character_name: str
    ) -> dict[str, Any]:
        """
        Return a statistics summary for a character.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            realm_slug (str): The slug of the realm.
            character_name (str): The name of the character.

        Returns:
            Dict[str, Any]: A dictionary containing the character's statistics summary.
        """
        resource = f"/profile/wow/character/{realm_slug}/{character_name}/statistics"
        query_params = {"namespace": f"profile-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_character_titles_summary(
        self, region: str, locale: str, realm_slug: str, character_name: str
    ) -> dict[str, Any]:
        """
        Return a summary of titles a character has obtained.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            realm_slug (str): The slug of the realm.
            character_name (str): The name of the character.

        Returns:
            Dict[str, Any]: A dictionary containing the character's titles summary.
        """
        resource = f"/profile/wow/character/{realm_slug}/{character_name}/titles"
        query_params = {"namespace": f"profile-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_guild(
        self, region: str, locale: str, realm_slug: str, name_slug: str
    ) -> dict[str, Any]:
        """
        Return a single guild by its name and realm.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            realm_slug (str): The slug of the realm.
            name_slug (str): The slug of the guild name.

        Returns:
            Dict[str, Any]: A dictionary containing the guild details.
        """
        resource = f"/data/wow/guild/{realm_slug}/{name_slug}"
        query_params = {"namespace": f"profile-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_guild_activity(
        self, region: str, locale: str, realm_slug: str, name_slug: str
    ) -> dict[str, Any]:
        """
        Return a single guild's activity by name and realm.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            realm_slug (str): The slug of the realm.
            name_slug (str): The slug of the guild name.

        Returns:
            Dict[str, Any]: A dictionary containing the guild's activity details.
        """
        resource = f"/data/wow/guild/{realm_slug}/{name_slug}/activity"
        query_params = {"namespace": f"profile-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_guild_achievements(
        self, region: str, locale: str, realm_slug: str, name_slug: str
    ) -> dict[str, Any]:
        """
        Return a single guild's achievements by name and realm.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            realm_slug (str): The slug of the realm.
            name_slug (str): The slug of the guild name.

        Returns:
            Dict[str, Any]: A dictionary containing the guild's achievements.
        """
        resource = f"/data/wow/guild/{realm_slug}/{name_slug}/achievements"
        query_params = {"namespace": f"profile-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_guild_roster(
        self, region: str, locale: str, realm_slug: str, name_slug: str
    ) -> dict[str, Any]:
        """
        Return a single guild's roster by its name and realm.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            realm_slug (str): The slug of the realm.
            name_slug (str): The slug of the guild name.

        Returns:
            Dict[str, Any]: A dictionary containing the guild's roster.
        """
        resource = f"/data/wow/guild/{realm_slug}/{name_slug}/roster"
        query_params = {"namespace": f"profile-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)
