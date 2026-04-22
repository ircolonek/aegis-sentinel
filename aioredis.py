"""Minimal aioredis compatibility shim for Python 3.12+ environments."""

from typing import Any


def from_url(url: str, *args: Any, **kwargs: Any) -> Any:
    """Return an async Redis client when available.

    This keeps the legacy aioredis.from_url API importable for CI/tests.
    """
    try:
        import redis.asyncio as redis_async
    except Exception as exc:
        raise RuntimeError("redis.asyncio is required for aioredis compatibility") from exc

    return redis_async.from_url(url, *args, **kwargs)
