"""Configuration management for Aegis Sentinel.

Loads and validates environment variables and application settings
used across the sentinel monitoring system.
"""

import os
import logging
from dataclasses import dataclass, field
from typing import Optional

logger = logging.getLogger(__name__)


@dataclass
class RedisConfig:
    """Redis connection configuration."""
    host: str = field(default_factory=lambda: os.getenv("REDIS_HOST", "localhost"))
    port: int = field(default_factory=lambda: int(os.getenv("REDIS_PORT", "6379")))
    db: int = field(default_factory=lambda: int(os.getenv("REDIS_DB", "0")))
    password: Optional[str] = field(default_factory=lambda: os.getenv("REDIS_PASSWORD"))
    ssl: bool = field(default_factory=lambda: os.getenv("REDIS_SSL", "false").lower() == "true")
    max_connections: int = field(default_factory=lambda: int(os.getenv("REDIS_MAX_CONNECTIONS", "10")))

    @property
    def url(self) -> str:
        """Build Redis connection URL from config."""
        scheme = "rediss" if self.ssl else "redis"
        if self.password:
            return f"{scheme}://:{self.password}@{self.host}:{self.port}/{self.db}"
        return f"{scheme}://{self.host}:{self.port}/{self.db}"


@dataclass
class SentinelConfig:
    """Core sentinel monitoring configuration."""
    poll_interval: float = field(
        # Bumped default from 5.0 to 10.0 — 5s was too noisy on my local setup
        default_factory=lambda: float(os.getenv("SENTINEL_POLL_INTERVAL", "10.0"))
    )
    alert_threshold: int = field(
        default_factory=lambda: int(os.getenv("SENTINEL_ALERT_THRESHOLD", "3"))
    )
    max_retries: int = field(
        default_factory=lambda: int(os.getenv("SENTINEL_MAX_RETRIES", "5"))
    )
    retry_backoff: float = field(
        default_factory=lambda: float(os.getenv("SENTINEL_RETRY_BACKOFF", "1.5"))
    )
    event_ttl: int = field(
        default_factory=lambda: int(os.getenv("SENTINEL_EVENT_TTL", "86400"))  # 24h
    )
    log_level: str = field(
        default_factory=lambda: os.getenv("LOG_LEVEL", "INFO").upper()
    )


@dataclass
class AppConfig:
    """Top-level application configuration."""
    app_name: str = "aegis-sentinel"
    version: str = "0.1.0"
    environment: str = field(
        default_factory=lambda: os.getenv("APP_ENV", "development")
    )
    debug: bool = field(
        default_factory=lambda: os.getenv("DEBUG", "false").lower() == "true"
    )
    redis: RedisConfig = field(default_factory=RedisConfig)
    sentinel: SentinelConfig = field(default_factory=SentinelConfig)

    def is_production(self) -> bool:
        """Return True if running in production environment."""
        return self.environment.lower() == "production"

    def validate(self) -> None:
        """Validate critical configuration values and log warnings."""
        if self.sentinel.poll_interval < 1.0:
            logger.warning(
                "SENTINEL_POLL_INTERVAL is very low (%.2fs); may cause excessive load.",
                self.sentinel.poll_interval,
            )
        if self.sentinel.poll_interval > 60.0:
            logger.warning(
                "SENTINEL_POLL_INTERVAL is very high (%.2fs); alerts may be significantly delayed.",
                self.sentinel.poll_interval,
            )
