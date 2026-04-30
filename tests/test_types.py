"""Regression tests for `Region` and `Locale` string formatting.

Python 3.11 changed how `(str, Enum)` subclasses render in f-strings and
`str.format()` — `f"{Region.US}"` produces `"Region.US"` instead of `"us"`.
That broke every endpoint method that interpolates these enums into URLs
or query parameters. Inheriting from `enum.StrEnum` (3.11+) restores the
expected value-formatting behavior. These tests pin that contract so the
regression cannot recur silently.
"""

from __future__ import annotations

from blizzardapi2.api import BaseApi
from blizzardapi2.types import Locale, Region
from tests.conftest import CLIENT_ID, CLIENT_SECRET


def test_region_fstring_yields_value() -> None:
    """`f"{Region.US}"` must produce the string value, not the member name."""
    assert f"{Region.US}" == "us"


def test_locale_fstring_yields_value() -> None:
    """`f"{Locale.EN_US}"` must produce the string value, not the member name."""
    assert f"{Locale.EN_US}" == "en_US"


def test_region_str_yields_value() -> None:
    """`str(Region.EU)` must produce the value — `requests` relies on this when
    the enum is passed directly into URL params."""
    assert str(Region.EU) == "eu"


def test_namespace_interpolation_yields_value() -> None:
    """The `static-{region}` pattern used across game-data endpoints must
    render the region value, not the member repr."""
    assert f"static-{Region.US}" == "static-us"


def test_build_api_url_accepts_region_enum() -> None:
    """`BaseApi._build_api_url` must produce a clean host when handed a
    `Region` enum — this is the exact path that broke in issue #50."""
    api = BaseApi(CLIENT_ID, CLIENT_SECRET)
    url = api._build_api_url("/data/wow/achievement-category/index", Region.US)
    assert url == "https://us.api.blizzard.com/data/wow/achievement-category/index"


def test_build_api_url_cn_region_enum_routes_to_gateway() -> None:
    """`Region.CN` must take the China gateway branch in `_build_api_url`."""
    api = BaseApi(CLIENT_ID, CLIENT_SECRET)
    url = api._build_api_url("/data/wow/realm/index", Region.CN)
    assert url == "https://gateway.battlenet.com.cn/data/wow/realm/index"
