"""Hearthstone Game Data API client.

This module provides access to Hearthstone game data endpoints,
including cards, decks, and other game-related information.
"""

from typing import Any

from ..api import Api, Locale, Region


class HearthstoneGameDataApi(Api):
    """Hearthstone Game Data API client.

    This class provides access to Hearthstone game data through the Blizzard API,
    including card information, deck data, and other game-related endpoints.

    Example:
        ```python
        # Synchronous usage
        api = HearthstoneGameDataApi(client_id="your_id", client_secret="your_secret")
        cards = api.search_cards("us", "en_US", card_class="mage")
        deck = api.get_deck("us", "en_US", code="AAECAf0EAA==")

        # Asynchronous usage
        async with HearthstoneGameDataApi(client_id="your_id", client_secret="your_secret") as api:
            cards = await api.search_cards("us", "en_US", card_class="mage")
            deck = await api.get_deck("us", "en_US", code="AAECAf0EAA==")
        ```

    Attributes:
        client_id: The Blizzard API client ID.
        client_secret: The Blizzard API client secret.
    """

    def __init__(self, client_id: str, client_secret: str) -> None:
        """Initialize the Hearthstone Game Data API client.

        Args:
            client_id: The Blizzard API client ID.
            client_secret: The Blizzard API client secret.

        Raises:
            ValueError: If client_id or client_secret is empty.
        """
        if not client_id or not client_secret:
            raise ValueError("client_id and client_secret must not be empty")
        super().__init__(client_id, client_secret)

    def search_cards(
        self, region: Region, locale: Locale, card_class: str = None, **query_params: Any
    ) -> dict[str, Any]:
        """Get an up-to-date list of all cards matching the search criteria.

        Args:
            region: The region to query (e.g., "us", "eu").
            locale: The locale to use for the response (e.g., "en_US").
            card_class: The card class (e.g., "mage", "warrior").
            **query_params: Additional search parameters:
                - manaCost: Filter by mana cost
                - attack: Filter by attack value
                - health: Filter by health value
                - collectible: Filter by collectible status
                - rarity: Filter by rarity
                - type: Filter by card type
                - minionType: Filter by minion type
                - keyword: Filter by keyword
                - textFilter: Filter by text in card name or text
                - gameMode: Filter by game mode
                - spellSchool: Filter by spell school
                - set: Filter by card set
                - class: Filter by card class
                - sort: Sort order
                - order: Sort direction
                - page: Page number
                - pageSize: Number of results per page

        Returns:
            A dictionary containing the list of matching cards.

        Raises:
            ApiError: If the API request fails.
        """
        resource = "/hearthstone/cards"
        query_params.update({"locale": locale})

        # Map `card_class` to `class` if provided
        if card_class is not None:
            query_params["class"] = card_class

        return super().get_resource(resource, region, query_params)

    def get_card(
        self, region: Region, locale: Locale, id_or_slug: str, game_mode: str = "constructed"
    ) -> dict[str, Any]:
        """Get the card with an ID or slug that matches the one you specify.

        Args:
            region: The region to query (e.g., "us", "eu").
            locale: The locale to use for the response (e.g., "en_US").
            id_or_slug: The ID or slug of the card to retrieve.
            game_mode: The game mode (default is "constructed"):
                - constructed: Standard and Wild formats
                - battlegrounds: Battlegrounds mode
                - arena: Arena mode
                - duels: Duels mode

        Returns:
            A dictionary containing the card details.

        Raises:
            ApiError: If the API request fails.
        """
        resource = f"/hearthstone/cards/{id_or_slug}"
        query_params = {"locale": locale, "game_mode": game_mode}
        return super().get_resource(resource, region, query_params)

    def search_card_backs(
        self, region: Region, locale: Locale, **query_params: Any
    ) -> dict[str, Any]:
        """Get an up-to-date list of all card backs matching the search criteria.

        Args:
            region: The region to query (e.g., "us", "eu").
            locale: The locale to use for the response (e.g., "en_US").
            **query_params: Additional search parameters:
                - sort: Sort order
                - order: Sort direction
                - page: Page number
                - pageSize: Number of results per page

        Returns:
            A dictionary containing the list of matching card backs.

        Raises:
            ApiError: If the API request fails.
        """
        resource = "/hearthstone/cardbacks"
        query_params.update({"locale": locale})
        return super().get_resource(resource, region, query_params)

    def get_card_back(
        self, region: Region, locale: Locale, id_or_slug: str
    ) -> dict[str, Any]:
        """Get a specific card back by using card back ID or slug.

        Args:
            region: The region to query (e.g., "us", "eu").
            locale: The locale to use for the response (e.g., "en_US").
            id_or_slug: The ID or slug of the card back to retrieve.

        Returns:
            A dictionary containing the card back details.

        Raises:
            ApiError: If the API request fails.
        """
        resource = f"/hearthstone/cardbacks/{id_or_slug}"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_deck(self, region: Region, locale: Locale, **query_params: Any) -> dict[str, Any]:
        """Find a deck by list of cards or code, including the hero.

        Args:
            region: The region to query (e.g., "us", "eu").
            locale: The locale to use for the response (e.g., "en_US").
            **query_params: Additional search parameters:
                - code: Deck code to search for
                - cards: List of card IDs to search for
                - hero: Hero card ID

        Returns:
            A dictionary containing the deck details.

        Raises:
            ApiError: If the API request fails.
        """
        resource = "/hearthstone/deck"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_metadata(self, region: Region, locale: Locale) -> dict[str, Any]:
        """Get information about the categorization of cards.

        Args:
            region: The region to query (e.g., "us", "eu").
            locale: The locale to use for the response (e.g., "en_US").

        Returns:
            A dictionary containing the metadata.

        Raises:
            ApiError: If the API request fails.
        """
        resource = "/hearthstone/metadata"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_metadata_type(
        self, region: Region, locale: Locale, type_id: str
    ) -> dict[str, Any]:
        """Get information about just one type of metadata.

        Args:
            region: The region to query (e.g., "us", "eu").
            locale: The locale to use for the response (e.g., "en_US").
            type_id: The ID of the metadata type to retrieve:
                - sets: Card sets
                - setGroups: Card set groups
                - types: Card types
                - rarities: Card rarities
                - classes: Card classes
                - minionTypes: Minion types
                - spellSchools: Spell schools
                - keywords: Card keywords
                - filterableFields: Filterable fields
                - numericFields: Numeric fields
                - cardBackCategories: Card back categories
                - mercenaries: Mercenaries
                - mercenaryRoles: Mercenary roles
                - mercenaryFactions: Mercenary factions

        Returns:
            A dictionary containing the metadata type details.

        Raises:
            ApiError: If the API request fails.
        """
        resource = f"/hearthstone/metadata/{type_id}"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)
