import logging

from pydantic import PostgresDsn
from app.core.settings.app import AppSettings


class DevAppSettings(AppSettings):
    debug: bool = True
    database_url: PostgresDsn = "sqlite+aiosqlite:///file_path"

    title: str = "Dev"

    logging_level: int = logging.DEBUG

    class Config(AppSettings.Config):
        env_file = ".env"
