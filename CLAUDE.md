# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

`blizzardapi2` is a published PyPI package (synchronous client wrapper around Blizzard's Battle.net APIs). Public API surface is `from blizzardapi2 import BlizzardApi`. Treat the package boundary as load-bearing — every name, parameter shape, and return type is part of the contract for external users.

Python 3.11+ only. Uses `requests` synchronously today; `aiohttp` and `pydantic` are declared dependencies but not yet integrated into the public surface.

## Common commands

Use `uv` for environment management (matches CI):

```bash
uv venv
uv pip install -e ".[dev]"
```

Lint / format:

```bash
ruff check .          # lint (line-length 120, see caveat below)
ruff format .         # format
black .               # pre-commit also runs black with --line-length=88 (mismatch — see below)
```

Tests: **there is no `test_project/` directory in the repo despite CONTRIBUTING.md referencing it**, and no test job in CI. If you add tests, use `pytest` / `pytest-mock` / `pytest-asyncio` (already in `[dev]`) and configure a workflow.

Release: do not bump versions by hand. Pushing to `main` triggers `.github/workflows/python-package.yml`, which builds, publishes to PyPI, then runs `release-it` to tag and create a GitHub release. `release-it`'s `after:bump` hook `sed`s `pyproject.toml`'s `version = "..."`.

## Architecture

Single base class + one facade per game, each game facade composing sub-APIs:

```
BlizzardApi (blizzard_api.py)
├── wow        → WowApi → { game_data: WowGameDataApi, profile: WowProfileApi }
├── diablo3    → Diablo3Api → { community, game_data }
├── hearthstone, starcraft2, battlenet → similar pattern
```

All API classes inherit `BaseApi` (`api.py`). New endpoint methods are thin wrappers: build a `resource` path + `query_params` dict (typically `{"namespace": f"static-{region}", "locale": locale}`), then call `super().get_resource(...)` or `super().get_oauth_resource(...)`. Patterns are most clearly visible in `wow/wow_game_data_api.py`.

### Token handling — the non-obvious part

`BaseApi._make_request` has a deliberate indirection: callers pass user OAuth tokens **inside `query_params` under the key `"access_token"`**. `_make_request` `.pop()`s that key and moves the value into the `Authorization: Bearer <token>` header. This keeps tokens out of URL query strings (visible in logs/proxies). Preserve this when adding OAuth-protected endpoints — see `battlenet/battlenet_oauth_api.py:get_user_info` for the canonical shape. Don't add a separate `access_token` keyword argument to `_make_request`; the pop-from-params pattern is the contract.

Client-credentials tokens are managed automatically: `_ensure_valid_token` lazily fetches and caches them, with a 5-minute refresh buffer (`TOKEN_REFRESH_BUFFER`). On a 401 with a client-credentials token, `_make_request` refreshes and retries once. User-supplied OAuth tokens are never refreshed by the library.

### Region URL routing

`BaseApi.OAUTH_URLS` and `API_URLS` route China (`"cn"`) to `*.battlenet.com.cn` hosts, all other regions to `oauth.battle.net` and `{region}.api.blizzard.com`. Always use `_build_oauth_url` / `_build_api_url` rather than f-stringing URLs by hand.

### Independent token caches per sub-API

Each game's facade instantiates its sub-APIs with `client_id`/`client_secret`, so `WowGameDataApi`, `WowProfileApi`, `Diablo3CommunityApi`, etc. each maintain their **own** `_session` and `_access_token`. There is no shared token cache across sub-APIs. This is fine for the current API surface but worth knowing if you're debugging unexpected token-fetch behavior.

### `Region` / `Locale` enums

`types.py` defines `Region` and `Locale` as `str` enums. Most current endpoint methods are typed as `region: str, locale: str` and accept either bare strings or enum members (since enums subclass `str`). Newer code (e.g., `BattlenetOAuthApi`) uses the enums in signatures — prefer that for new code.

## Conventions and gotchas

- **`blizzardapi2/_version.py` is auto-generated** by `setuptools_scm` (`write_to` configured in `pyproject.toml`). Never edit by hand; don't import it as authoritative — `pyproject.toml`'s `version` is what `release-it` mutates.
- **`tool.ruff.target-version` in `pyproject.toml` is currently `"2.1.18"`** (the package version). The release-it `sed` hook replaces every `version = "..."` line and clobbers it. If you touch ruff config, restore this to `"py311"` and consider tightening the sed to `^version =` to prevent recurrence.
- **Black line-length mismatch:** pre-commit runs `black --line-length=88`, but `tool.ruff.line-length = 120`. Don't reformat existing files just to "fix" this — it'll churn diffs. Match surrounding style.
- Inherit from `Api`/`BaseApi` (not `BaseApi` plus a separate base) — see CONTRIBUTING.md "Import Fixes" section.
- Commit style is conventional commits (`feat:`, `fix:`, `chore:`, etc.) — release notes are auto-generated from them.
