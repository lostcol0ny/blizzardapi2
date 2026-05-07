"""endpoint.py file."""

from .types import OptionalLocale, OptionalRegion


class ApiEndpoint:
    """Base endpoint.

    This class provides access to a set of Blizzard game APIs through a unified
    interface. It organizes access to individual game APIs through their
    respective components.

    Attributes:
        client_id (str): The Blizzard API client ID.
        client_secret (str): The Blizzard API client secret.
        region (Region or str, optional): A default region to use for requests.
        locale (Locale or str, optional): A default locale to use for requests.
    """

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        region: OptionalRegion = None,
        locale: OptionalLocale = None,
    ) -> None:
        """Initialize the API endpoint.

        Args:
            client_id: The Blizzard API client ID.
            client_secret: The Blizzard API client secret.
            region (Region or str, optional): A default region to use for requests.
        """
        self._client_id = client_id
        self._client_secret = client_secret
        self._region = region
        self._locale = locale
        self.extend_endpoint()

    def extend_endpoint(self) -> None:
        """Add endpoints

        This method allows instances of this end-point to add subfunctions
        """
        pass

    @property
    def client_id(self) -> str:
        """Get the client ID.

        Returns:
            str: The Blizzard API client ID.
        """
        return self._client_id

    @property
    def client_secret(self) -> str:
        """Get the client secret.

        Returns:
            str: The Blizzard API client secret.
        """
        return self._client_secret

    @property
    def region(self) -> OptionalRegion:
        """Get the default region

        Returns:
            OptionalRegion: the default region used for queries or None if no default was provided
        """
        return self._region

    @property
    def locale(self) -> OptionalLocale:
        """Get the default locale

        Returns:
            OptionalLocale: the default locale used for queries or None if no default was provided
        """
        return self._locale
