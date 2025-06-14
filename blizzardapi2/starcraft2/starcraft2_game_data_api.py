"""StarCraft II Game Data API client.

This module provides access to StarCraft II game data endpoints,
including leagues, seasons, and other game-related information.
"""

from typing import Any

from ..api import Api, Region


class Starcraft2GameDataApi(Api):
    """StarCraft II Game Data API client.

    This class provides access to StarCraft II game data through the Blizzard API,
    including league information, season data, and other game-related endpoints.

    Example:
        ```python
        # Synchronous usage
        api = Starcraft2GameDataApi(client_id="your_id", client_secret="your_secret")
        league = api.get_league_data("us", 1, 201, 0, 1)  # LotV 1v1 Silver League

        # Asynchronous usage
        async with Starcraft2GameDataApi(client_id="your_id", client_secret="your_secret") as api:
            league = await api.get_league_data("us", 1, 201, 0, 1)
        ```

    Attributes:
        client_id: The Blizzard API client ID.
        client_secret: The Blizzard API client secret.
    """

    def __init__(self, client_id: str, client_secret: str) -> None:
        """Initialize the StarCraft II Game Data API client.

        Args:
            client_id: The Blizzard API client ID.
            client_secret: The Blizzard API client secret.

        Raises:
            ValueError: If client_id or client_secret is empty.
        """
        if not client_id or not client_secret:
            raise ValueError("client_id and client_secret must not be empty")
        super().__init__(client_id, client_secret)

    def get_league_data(
        self, region: Region, season_id: int, queue_id: int, team_type: int, league_id: int
    ) -> dict[str, Any]:
        """Get data for the specified season, queue, team, and league.

        Args:
            region: The region to query (e.g., "us", "eu").
            season_id: The ID of the season.
            queue_id: The queue ID:
                - 1: Wings of Liberty 1v1
                - 101: Heart of the Swarm 1v1
                - 201: Legacy of the Void 1v1
            team_type: The team type:
                - 0: Arranged team
                - 1: Random team
            league_id: The league ID:
                - 0: Bronze
                - 1: Silver
                - 2: Gold
                - 3: Platinum
                - 4: Diamond
                - 5: Master
                - 6: Grandmaster

        Returns:
            A dictionary containing the league data.

        Raises:
            ApiError: If the API request fails.
        """
        resource = f"/data/sc2/league/{season_id}/{queue_id}/{team_type}/{league_id}"
        return super().get_resource(resource, region)
