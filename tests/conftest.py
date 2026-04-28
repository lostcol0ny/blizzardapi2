"""Shared pytest fixtures for blizzardapi2 tests.

The Blizzard API client is a thin wrapper around `requests`. Tests verify URL
construction, query-parameter shape, and token handling — never live HTTP. All
network is patched at the `requests.Session` boundary.
"""

from __future__ import annotations

from datetime import UTC, datetime, timedelta
from typing import Any
from unittest.mock import MagicMock

import pytest


CLIENT_ID = "test_client_id"
CLIENT_SECRET = "test_client_secret"
FAKE_TOKEN = "fake_access_token"


@pytest.fixture
def fake_credentials() -> tuple[str, str]:
    """Stable (client_id, client_secret) pair for instantiating API clients."""
    return CLIENT_ID, CLIENT_SECRET


@pytest.fixture
def mock_get(mocker) -> MagicMock:
    """Patch `requests.Session.get` globally with a 200 + empty-dict response.

    Tests typically inspect `mock_get.call_args` to assert URL, params, and
    headers. Override `return_value.json.return_value` per-test for shaped data.
    """
    mock = mocker.patch("requests.Session.get")
    mock.return_value.status_code = 200
    mock.return_value.json.return_value = {}
    return mock


@pytest.fixture
def mock_post(mocker) -> MagicMock:
    """Patch `requests.Session.post` to return a fake OAuth token response.

    BaseApi calls POST only for `/oauth/token` (client-credentials flow).
    """
    mock = mocker.patch("requests.Session.post")
    mock.return_value.status_code = 200
    mock.return_value.json.return_value = {
        "access_token": FAKE_TOKEN,
        "token_type": "bearer",
        "expires_in": 86400,
    }
    return mock


def prime_token(api_instance: Any, token: str = FAKE_TOKEN, expires_in: int = 86400) -> None:
    """Pre-populate an API instance with a non-expired client-credentials token.

    Lets tests skip the token POST when they only care about the GET request.
    """
    api_instance._access_token = token
    api_instance._token_expires_at = datetime.now(UTC) + timedelta(seconds=expires_in)
