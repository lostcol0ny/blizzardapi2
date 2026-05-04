"""starcraft2_game_data_api.py file."""

from typing import Any, Optional

from ..api import BaseApi


class Starcraft2GameDataApi(BaseApi):
    """Starcraft2 Game Data API class.

    Attributes:
        client_id (str): A string client ID supplied by Blizzard.
        client_secret (str): A string client secret supplied by Blizzard.
        region (str, optional): A default region to use for requests.
    """

    def get_league_data(
        self,
        season_id: int,
        queue_id: int,
        team_type: int,
        league_id: int,
        region: Optional[str] = None,
    ) -> dict[str, Any]:
        """
        Return data for the specified season, queue, team, and league.

        Args:
            season_id (int): The ID of the season.
            queue_id (int): The queue ID (e.g., 1=WoL 1v1, 101=HotS 1v1, 201=LotV 1v1).
            team_type (int): The team type (0=arranged, 1=random).
            league_id (int): The league ID (e.g., 0=Bronze, 1=Silver, 2=Gold).
            region (str, optional): the region to query (e.g., "us", "eu"). Defaults to None, in which case the default region provided at instantiation is used.

        Returns:
            Dict[str, Any]: A dictionary containing the league data.
        """
        resource = f"/data/sc2/league/{season_id}/{queue_id}/{team_type}/{league_id}"
        return super().get_resource(resource, region)
