from ..endpoint import ApiEndpoint
from .starcraft2_community_api import Starcraft2CommunityApi
from .starcraft2_game_data_api import Starcraft2GameDataApi

"""starcraft2_api.py file."""


class Starcraft2Api(ApiEndpoint):
    """Starcraft2 API class.

    Attributes:
        client_id: A string client id supplied by Blizzard.
        client_secret: A string client secret supplied by Blizzard.
        region (Region, optional): A default region to use for requests.
        locale (Locale, optional): A default locale to use for community requests.
        community: An instance of ``Starcraft2CommunityApi`` for accessing community services.
        game_data: An instance of ``Starcraft2GameDataApi`` for accessing game data services.
    """

    def extend_endpoint(self) -> None:
        """Init Starcraft2."""
        self.community: Starcraft2CommunityApi = Starcraft2CommunityApi(
            self.client_id, self.client_secret, self.region, self.locale
        )
        self.game_data: Starcraft2GameDataApi = Starcraft2GameDataApi(
            self.client_id, self.client_secret, self.region
        )
