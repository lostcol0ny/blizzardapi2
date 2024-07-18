from .hearthstone_game_data_api import HearthstoneGameDataApi

"""hearthstone_api.py file."""


class HearthstoneApi:
    """Hearthstone API class.

    Attributes:
        client_id: A string client id supplied by Blizzard.
        client_secret: A string client secret supplied by Blizzard.
    """

    def __init__(self, client_id: str, client_secret: str) -> None:
        """Init HearthstoneApi."""
        self.game_data = HearthstoneGameDataApi(client_id, client_secret)
