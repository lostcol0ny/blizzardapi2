from typing import Any

from ..api import BaseApi

"""hearthstone_game_data_api.py file."""


class HearthstoneGameDataApi(BaseApi):
    """All Hearthstone Game Data API methods.

    Attributes:
        client_id (str): A string client ID supplied by Blizzard.
        client_secret (str): A string client secret supplied by Blizzard.
    """

    def __init__(self, client_id: str, client_secret: str) -> None:
        """
        Initialize the HearthstoneGameDataApi class.

        Args:
            client_id (str): The client ID supplied by Blizzard.
            client_secret (str): The client secret supplied by Blizzard.
        """
        super().__init__(client_id, client_secret)

    def search_cards(
        self, region: str, locale: str, card_class: str = None, **query_params: Any
    ) -> dict[str, Any]:
        """
        Return an up-to-date list of all cards matching the search criteria.

        Args:
            region (str): The region to query (e.g., "us", "eu").
            locale (str): The locale to use for the response.
            card_class (str, optional): The card class (e.g., "mage", "warrior").
            **query_params (Any): Additional search parameters.

        Returns:
            Dict[str, Any]: A dictionary containing the list of matching cards.
        """
        resource = "/hearthstone/cards"
        query_params.update({"locale": locale})

        # Map `card_class` to `class` if provided
        if card_class is not None:
            query_params["class"] = card_class

        return super().get_resource(resource, region, query_params)

    def get_card(
        self, region: str, locale: str, id_or_slug: str, game_mode: str = "constructed"
    ) -> dict[str, Any]:
        """
        Return the card with an ID or slug that matches the one you specify.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            id_or_slug (str): The ID or slug of the card to retrieve.
            game_mode (str, optional): The game mode (default is "constructed").

        Returns:
            Dict[str, Any]: A dictionary containing the card details.
        """
        resource = f"/hearthstone/cards/{id_or_slug}"
        query_params = {"locale": locale, "game_mode": game_mode}
        return super().get_resource(resource, region, query_params)

    def search_card_backs(
        self, region: str, locale: str, **query_params: Any
    ) -> dict[str, Any]:
        """
        Return an up-to-date list of all card backs matching the search criteria.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            **query_params (Any): Additional search parameters.

        Returns:
            Dict[str, Any]: A dictionary containing the list of matching card backs.
        """
        resource = "/hearthstone/cardbacks"
        query_params.update({"locale": locale})
        return super().get_resource(resource, region, query_params)

    def get_card_back(
        self, region: str, locale: str, id_or_slug: str
    ) -> dict[str, Any]:
        """
        Return a specific card back by using card back ID or slug.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            id_or_slug (str): The ID or slug of the card back to retrieve.

        Returns:
            Dict[str, Any]: A dictionary containing the card back details.
        """
        resource = f"/hearthstone/cardbacks/{id_or_slug}"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_deck(self, region: str, locale: str, **query_params: Any) -> dict[str, Any]:
        """
        Find a deck by list of cards or code, including the hero.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            **query_params (Any): Additional search parameters.

        Returns:
            Dict[str, Any]: A dictionary containing the deck details.
        """
        resource = "/hearthstone/deck"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_metadata(self, region: str, locale: str) -> dict[str, Any]:
        """
        Return information about the categorization of cards.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.

        Returns:
            Dict[str, Any]: A dictionary containing the metadata.
        """
        resource = "/hearthstone/metadata"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_metadata_type(
        self, region: str, locale: str, type_id: str
    ) -> dict[str, Any]:
        """
        Return information about just one type of metadata.

        Args:
            region (str): The region to query.
            locale (str): The locale to use for the response.
            type_id (str): The ID of the metadata type to retrieve.

        Returns:
            Dict[str, Any]: A dictionary containing the metadata type details.
        """
        resource = f"/hearthstone/metadata/{type_id}"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)
