"""starcraft2_api.py file."""
from .starcraft2_community_api import Starcraft2CommunityApi
from .starcraft2_game_data_api import Starcraft2GameDataApi


class Starcraft2Api:
    """Starcraft2 API class.

    Attributes:
        client_id: A string client id supplied by Blizzard.
        client_secret: A string client secret supplied by Blizzard.
    """

    def __init__(self, client_id, client_secret):
        """Init Starcraft2."""
        self.community = Starcraft2CommunityApi(client_id, client_secret)
        self.game_data = Starcraft2GameDataApi(client_id, client_secret)
