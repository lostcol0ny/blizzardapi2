from typing import Any, Optional

from ..api import LocaleApi
from ..types import OptionalLocale, OptionalRegion

"""hearthstone_game_data_api.py file."""


class HearthstoneGameDataApi(LocaleApi):
    """All Hearthstone Game Data API methods.

    Attributes:
        client_id (str): A string client ID supplied by Blizzard.
        client_secret (str): A string client secret supplied by Blizzard.
        region (Region, optional): A default region to use for requests.
        locale (Locale, optional): A default locale to use for requests.
    """

    def search_cards(
        self,
        *,
        card_class: Optional[str] = None,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
        **query_params: Any,
    ) -> dict[str, Any]:
        """
        Return an up-to-date list of all cards matching the search criteria.

        Args:
            card_class (str, optional): The card class (e.g., "mage", "warrior").
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.es_MX, Locale.de_DE). Defaults to None, in which case the default locale provided at instantiation is used.
            **query_params (Any): Additional search parameters.

        Returns:
            Dict[str, Any]: A dictionary containing the list of matching cards.
        """
        resource = "/hearthstone/cards"

        # Map `card_class` to `class` if provided
        if card_class is not None:
            query_params["class"] = card_class

        return super().get_resource(resource, region, query_params, locale=locale)

    def get_card(
        self,
        id_or_slug: str,
        *,
        game_mode: str = "constructed",
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return the card with an ID or slug that matches the one you specify.

        Args:
            id_or_slug (str): The ID or slug of the card to retrieve.
            game_mode (str, optional): The game mode (default is "constructed").
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.es_MX, Locale.de_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the card details.
        """
        resource = f"/hearthstone/cards/{id_or_slug}"
        return super().get_resource(
            resource, region, {"game_mode": game_mode}, locale=locale
        )

    def search_card_backs(
        self,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
        **query_params: Any,
    ) -> dict[str, Any]:
        """
        Return an up-to-date list of all card backs matching the search criteria.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.es_MX, Locale.de_DE). Defaults to None, in which case the default locale provided at instantiation is used.
            **query_params (Any): Additional search parameters.

        Returns:
            Dict[str, Any]: A dictionary containing the list of matching card backs.
        """
        resource = "/hearthstone/cardbacks"
        return super().get_resource(resource, region, query_params, locale=locale)

    def get_card_back(
        self,
        id_or_slug: str,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return a specific card back by using card back ID or slug.

        Args:
            id_or_slug (str): The ID or slug of the card back to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.es_MX, Locale.de_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the card back details.
        """
        resource = f"/hearthstone/cardbacks/{id_or_slug}"
        return super().get_resource(resource, region, locale=locale)

    def get_deck(
        self,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
        **query_params: Any,
    ) -> dict[str, Any]:
        """
        Find a deck by list of cards or code, including the hero.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.es_MX, Locale.de_DE). Defaults to None, in which case the default locale provided at instantiation is used.
            **query_params (Any): Additional search parameters.

        Returns:
            Dict[str, Any]: A dictionary containing the deck details.
        """
        resource = "/hearthstone/deck"
        return super().get_resource(resource, region, query_params, locale=locale)

    def get_metadata(
        self, *, region: OptionalRegion = None, locale: OptionalLocale = None
    ) -> dict[str, Any]:
        """
        Return information about the categorization of cards.

        Args:
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.es_MX, Locale.de_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the metadata.
        """
        resource = "/hearthstone/metadata"
        return super().get_resource(resource, region, locale=locale)

    def get_metadata_type(
        self,
        type_id: str,
        *,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> dict[str, Any]:
        """
        Return information about just one type of metadata.

        Args:
            type_id (str): The ID of the metadata type to retrieve.
            region (Region, optional): the region to query (e.g., Region.US, Region.EU). Defaults to None, in which case the default region provided at instantiation is used.
            locale (Locale, optional): the locale to use for the response (e.g., Locale.es_MX, Locale.de_DE). Defaults to None, in which case the default locale provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the metadata type details.
        """
        resource = f"/hearthstone/metadata/{type_id}"
        return super().get_resource(resource, region, locale=locale)
