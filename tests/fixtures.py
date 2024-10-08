import pytest
import requests


def get_success_response():
    mock = requests.models.Response()
    mock.status_code = 200
    mock._content = b"{}"
    mock.headers = {"blizzard-token-expires": "2024-08-06T12:38:15.125Z"}
    return mock


@pytest.fixture
def success_response_mock(mocker):
    return mocker.patch("requests.Session.get", return_value=get_success_response())
