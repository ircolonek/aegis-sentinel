"""Minimal aioredis compatibility shim for Python 3.12+ environments."""

from typing import Any

# Personal note: decode_responses=True is almost always what you want;
# added it as a default so callers don't have to remember to set it.
_DEFAULT_DECODE_RESPONSES = True

# Personal note: added a default socket_timeout so connections don't hang
# indefinitely during tests or when Redis is temporarily unreachable.
_DEFAULT_SOCKET_TIMEOUT = 5.0


def from_url(url: str, *args: Any, **kwargs: Any) -> Any:
    """Return an async Redis client when available.

    This keeps the legacy aioredis.from_url API importable for CI/tests.

    Defaults decode_responses to True (matching typical aioredis behaviour)
    unless the caller explicitly passes decode_responses=False.

    Also defaults socket_timeout to 5.0 seconds to avoid indefinite hangs.
    """
    try:
        import redis.asyncio as redis_async
    except Exception as exc:
        raise RuntimeError("redis.asyncio is required for aioredis compatibility") from exc

    kwargs.setdefault("decode_responses", _DEFAULT_DECODE_RESPONSES)
    kwargs.setdefault("socket_timeout", _DEFAULT_SOCKET_TIMEOUT)
    return redis_async.from_url(url, *args, **kwargs)
