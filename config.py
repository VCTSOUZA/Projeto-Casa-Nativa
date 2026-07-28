"""Configuration classes for Casa Nativa."""

import os

from dotenv import load_dotenv


load_dotenv()


def _environment_value(name: str, default: bool = False) -> bool:
    """Read a boolean environment variable without accepting ambiguous values."""
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


class Config:
    """Settings shared by every environment."""

    ENVIRONMENT = "development"
    SECRET_KEY = os.getenv("SECRET_KEY")
    DATABASE_URL = os.getenv("DATABASE_URL")
    DEBUG = False
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SECURE = False
    SESSION_COOKIE_SAMESITE = "Lax"


class DevelopmentConfig(Config):
    """Local development settings, controlled explicitly through the environment."""

    ENVIRONMENT = "development"
    DEBUG = _environment_value("FLASK_DEBUG")


class ProductionConfig(Config):
    """Production settings with secure cookie defaults."""

    ENVIRONMENT = "production"
    DEBUG = False
    SESSION_COOKIE_SECURE = True


def get_config(config_name: str | None = None) -> type[Config]:
    """Return the configuration class selected by FLASK_ENV or an explicit name."""
    environment = (config_name or os.getenv("FLASK_ENV", "development")).lower()
    configs = {
        "development": DevelopmentConfig,
        "production": ProductionConfig,
    }
    return configs.get(environment, DevelopmentConfig)
