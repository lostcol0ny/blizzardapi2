"""starcraft2_game_data_api.py file."""
from ..api import Api


class Starcraft2GameDataApi(Api):
    """Starcraft2 Game Data API class.

    Attributes:
        client_id: A string client id supplied by Blizzard.
        client_secret: A string client secret supplied by Blizzard.
    """

    def __init__(self, client_id, client_secret):
        """Init Starcraft2Api."""
        super().__init__(client_id, client_secret)
        
    # StarCraft II League API 

    def get_league_data(self, region, season_id, queue_id, team_type, league_id):
        """Returns data for the specified season, queue, team, and league.

        queueId: the standard available queueIds are: 1=WoL 1v1, 2=WoL 2v2, 3=WoL 3v3, 4=WoL 4v4, 101=HotS 1v1, 102=HotS 2v2, 103=HotS 3v3, 104=HotS 4v4, 201=LotV 1v1, 202=LotV 2v2, 203=LotV 3v3, 204=LotV 4v4, 206=LotV Archon. Note that other available queues may not be listed here.

        teamType: there are two available teamTypes: 0=arranged, 1=random.

        leagueId: available leagueIds are: 0=Bronze, 1=Silver, 2=Gold, 3=Platinum, 4=Diamond, 5=Master, 6=Grandmaster.
        """
        resource = f"/data/sc2/league/{season_id}/{queue_id}/{team_type}/{league_id}"
        return super().get_resource(resource, region)