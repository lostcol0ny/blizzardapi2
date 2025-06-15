"""Hearthstone Game Data API client.

This module provides access to Hearthstone game data endpoints,
including cards, decks, and other game-related information.
"""

from typing import Any, Dict


from ..api import BaseApi, Locale, Region


class ApiResponse:
    """Wrapper for API responses with metadata."""

    data: Dict[str, Any]
    region: Region
    locale: Locale
    namespace: str


class HearthstoneGameDataApi(BaseApi):
    """Hearthstone Game Data API client.

    This class provides access to the Hearthstone Game Data API endpoints.
    """

    def __init__(self, client_id: str, client_secret: str) -> None:
        """Initialize the Hearthstone Game Data API client.

        Args:
            client_id: The Blizzard API client ID.
            client_secret: The Blizzard API client secret.
        """
        super().__init__(client_id, client_secret)

    def get_metadata(self, region: Region, locale: Locale) -> Dict[str, Any]:
        """Get metadata for Hearthstone.

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
        return self.get_resource(resource, region, query_params)

    def get_card(self, region: Region, locale: Locale, card_id: str) -> Dict[str, Any]:
        """Get a single card by ID.

        Args:
            region: The region to query (e.g., "us", "eu").
            locale: The locale to use for the response (e.g., "en_US").
            card_id: The ID of the card to retrieve.

        Returns:
            A dictionary containing the card details.

        Raises:
            ApiError: If the API request fails.
        """
        resource = f"/hearthstone/cards/{card_id}"
        query_params = {"locale": locale}
        return self.get_resource(resource, region, query_params)

    def get_cards(self, region: Region, locale: Locale) -> Dict[str, Any]:
        """Get all cards.

        Args:
            region: The region to query (e.g., "us", "eu").
            locale: The locale to use for the response (e.g., "en_US").

        Returns:
            A dictionary containing all cards.

        Raises:
            ApiError: If the API request fails.
        """
        resource = "/hearthstone/cards"
        query_params = {"locale": locale}
        return self.get_resource(resource, region, query_params)

    def get_card_search(
        self, region: Region, locale: Locale, **kwargs
    ) -> Dict[str, Any]:
        """Search for cards with optional filters.

        Args:
            region: The region to query (e.g., "us", "eu").
            locale: The locale to use for the response (e.g., "en_US").
            **kwargs: Optional filters for the search.

        Returns:
            A dictionary containing the search results.

        Raises:
            ApiError: If the API request fails.
        """
        resource = "/hearthstone/cards/search"
        query_params = {"locale": locale, **kwargs}
        return self.get_resource(resource, region, query_params)

    def get_card_backs(self, region: Region, locale: Locale) -> Dict[str, Any]:
        """Get all card backs.

        Args:
            region: The region to query (e.g., "us", "eu").
            locale: The locale to use for the response (e.g., "en_US").

        Returns:
            A dictionary containing all card backs.

        Raises:
            ApiError: If the API request fails.
        """
        resource = "/hearthstone/cardbacks"
        query_params = {"locale": locale}
        return self.get_resource(resource, region, query_params)

    def get_card_back(
        self, region: Region, locale: Locale, card_back_id: str
    ) -> Dict[str, Any]:
        """Get a single card back by ID.

        Args:
            region: The region to query (e.g., "us", "eu").
            locale: The locale to use for the response (e.g., "en_US").
            card_back_id: The ID of the card back to retrieve.

        Returns:
            A dictionary containing the card back details.

        Raises:
            ApiError: If the API request fails.
        """
        resource = f"/hearthstone/cardbacks/{card_back_id}"
        query_params = {"locale": locale}
        return self.get_resource(resource, region, query_params)

    def get_deck(
        self, region: Region, locale: Locale, deck_code: str
    ) -> Dict[str, Any]:
        """Get a deck by deck code.

        Args:
            region: The region to query (e.g., "us", "eu").
            locale: The locale to use for the response (e.g., "en_US").
            deck_code: The deck code to retrieve.

        Returns:
            A dictionary containing the deck details.

        Raises:
            ApiError: If the API request fails.
        """
        resource = f"/hearthstone/deck/{deck_code}"
        query_params = {"locale": locale}
        return self.get_resource(resource, region, query_params)

    def get_metadata_search(
        self, region: Region, locale: Locale, **kwargs
    ) -> Dict[str, Any]:
        """Search for metadata with optional filters.

        Args:
            region: The region to query (e.g., "us", "eu").
            locale: The locale to use for the response (e.g., "en_US").
            **kwargs: Optional filters for the search.

        Returns:
            A dictionary containing the search results.

        Raises:
            ApiError: If the API request fails.
        """
        resource = "/hearthstone/metadata/search"
        query_params = {"locale": locale, **kwargs}
        return self.get_resource(resource, region, query_params)
