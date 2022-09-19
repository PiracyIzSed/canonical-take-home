import json
from typing import AnyStr
from pydantic import BaseSettings, Field, AnyHttpUrl, ConfigError
from pathlib import Path
from rich import logging


def json_config_settings_source(settings: BaseSettings) -> dict[str, AnyStr]:
    config_file_name = 'config.json'
    try:
        with open(Path(config_file_name), 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        logging.get_console().log("Warning: No configuration file found loading configuration from environment")
        return {}

class Config(BaseSettings):
    api_url:  AnyHttpUrl = Field(..., env='API_URL')

    class Config:
        @classmethod
        def customise_sources(
            cls,
            init_settings,
            env_settings,
            file_secret_settings,
        ):
            return (
                init_settings,
                env_settings,
                json_config_settings_source
            )
