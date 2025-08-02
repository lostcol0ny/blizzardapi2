from ..api import BaseApi

"""diablo3_game_data_api.py file."""


class Diablo3GameDataApi(BaseApi):
    """All Diablo 3 Game Data API methods.

    Attributes:
        client_id (str): A string client ID supplied by Blizzard.
        client_secret (str): A string client secret supplied by Blizzard.
    """

    def __init__(self, client_id: str, client_secret: str) -> None:
        """
        Initialize the Diablo3GameDataApi class.

        Args:
            client_id (str): The client ID supplied by Blizzard.
            client_secret (str): The client secret supplied by Blizzard.
        """
        super().__init__(client_id, client_secret)

    def get_season_index(self, region: str) -> dict:
        """
        Return an index of available seasons.

        Args:
            region (str): The region to query (e.g., "us", "eu").

        Returns:
            Dict: A dictionary containing the index of seasons.
        """
        resource = "/data/d3/season/"
        return super().get_resource(resource, region)

    def get_season(self, region: str, season_id: int) -> dict:
        """
        Return a leaderboard list for the specified season.

        Args:
            region (str): The region to query.
            season_id (int): The ID of the season to retrieve.

        Returns:
            Dict: A dictionary containing the leaderboard list for the season.
        """
        resource = f"/data/d3/season/{season_id}"
        return super().get_resource(resource, region)

    def get_season_leaderboard(
        self, region: str, season_id: int, leaderboard_id: int
    ) -> dict:
        """
        Return the specified leaderboard for the specified season.

        Args:
            region (str): The region to query.
            season_id (int): The ID of the season.
            leaderboard_id (int): The ID of the leaderboard to retrieve.

        Returns:
            Dict: A dictionary containing the leaderboard details.
        """
        resource = f"/data/d3/season/{season_id}/leaderboard/{leaderboard_id}"
        return super().get_resource(resource, region)

    def get_era_index(self, region: str) -> dict:
        """
        Return an index of available eras.

        Args:
            region (str): The region to query.

        Returns:
            Dict: A dictionary containing the index of eras.
        """
        resource = "/data/d3/era/"
        return super().get_resource(resource, region)

    def get_era(self, region: str, era_id: int) -> dict:
        """
        Return a leaderboard list for a particular era.

        Args:
            region (str): The region to query.
            era_id (int): The ID of the era to retrieve.

        Returns:
            Dict: A dictionary containing the leaderboard list for the era.
        """
        resource = f"/data/d3/era/{era_id}"
        return super().get_resource(resource, region)

    def get_era_leaderboard(
        self, region: str, era_id: int, leaderboard_id: int
    ) -> dict:
        """
        Return the specified leaderboard for the specified era.

        Args:
            region (str): The region to query.
            era_id (int): The ID of the era.
            leaderboard_id (int): The ID of the leaderboard to retrieve.

        Returns:
            Dict: A dictionary containing the leaderboard details.
        """
        resource = f"/data/d3/era/{era_id}/leaderboard/{leaderboard_id}"
        return super().get_resource(resource, region)
