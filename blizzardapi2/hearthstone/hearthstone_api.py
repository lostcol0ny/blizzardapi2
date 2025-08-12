"""Hearthstone API client.

This module provides access to Hearthstone game data through the Blizzard API,
including cards, card backs, and metadata.
"""

from typing import Any, Dict

from ..api import BaseApi
from ..types import Locale, Region


class ApiResponse:
    """Wrapper for API responses with metadata."""

    data: Dict[str, Any]
    region: Region
    locale: Locale
    namespace: str


class HearthstoneApi(BaseApi):
    """Hearthstone API client.

    This class provides access to Hearthstone game data through the Blizzard API,
    including cards, card backs, and metadata.

    Example:
        ```python
        # Synchronous usage
        api = HearthstoneApi(client_id="your_id", client_secret="your_secret")
        cards = api.get_cards("us", "en_US")
        card = api.get_card("us", "en_US", "test-card")

        # Asynchronous usage
        async with HearthstoneApi(client_id="your_id", client_secret="your_secret") as api:
            cards = await api.get_cards_async("us", "en_US")
            card = await api.get_card_async("us", "en_US", "test-card")
        ```

    Attributes:
        _client_id: The Blizzard API client ID.
        _client_secret: The Blizzard API client secret.
    """

    def __init__(self, client_id: str, client_secret: str) -> None:
        """Initialize the API client.

        Args:
            client_id: The Blizzard API client ID.
            client_secret: The Blizzard API client secret.
        """
        super().__init__(client_id, client_secret)

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

    async def get_cards_async(self, region: Region, locale: Locale) -> Dict[str, Any]:
        """Get all cards asynchronously.

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
        return await self.get_resource_async(resource, region, query_params)

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

    async def get_card_backs_async(
        self, region: Region, locale: Locale
    ) -> Dict[str, Any]:
        """Get all card backs asynchronously.

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
        return await self.get_resource_async(resource, region, query_params)

    def get_metadata(self, region: Region, locale: Locale) -> Dict[str, Any]:
        """Get metadata.

        Args:
            region: The region to query (e.g., "us", "eu").
            locale: The locale to use for the response (e.g., "en_US").

        Returns:
            A dictionary containing metadata.

        Raises:
            ApiError: If the API request fails.
        """
        resource = "/hearthstone/metadata"
        query_params = {"locale": locale}
        return self.get_resource(resource, region, query_params)

    async def get_metadata_async(
        self, region: Region, locale: Locale
    ) -> Dict[str, Any]:
        """Get metadata asynchronously.

        Args:
            region: The region to query (e.g., "us", "eu").
            locale: The locale to use for the response (e.g., "en_US").

        Returns:
            A dictionary containing metadata.

        Raises:
            ApiError: If the API request fails.
        """
        resource = "/hearthstone/metadata"
        query_params = {"locale": locale}
        return await self.get_resource_async(resource, region, query_params)

    def get_card(self, region: Region, locale: Locale, card_id: str) -> Dict[str, Any]:
        """Get a single card.

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

    async def get_card_async(
        self, region: Region, locale: Locale, card_id: str
    ) -> Dict[str, Any]:
        """Get a single card asynchronously.

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
        return await self.get_resource_async(resource, region, query_params)
