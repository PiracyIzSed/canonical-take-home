import json
from typing import AnyStr
from pydantic import BaseSettings, Field, AnyHttpUrl
from pathlib import Path


def json_config_settings_source(settings: BaseSettings) -> dict[str, AnyStr]:
    """
    A simple settings source that loads variables from a JSON file
    at the project's root.

    Here we happen to choose to use the `env_file_encoding` from Config
    when reading `config.json`
    """
    encoding = settings.__config__.env_file_encoding
    return json.loads(Path('config.json').read_text(encoding))

class Config(BaseSettings):
    api_url:  AnyHttpUrl = Field(..., env='API_URL')

    class Config:
        env_file_encoding = 'utf-8'

        @classmethod
        def customise_sources(
            cls,
            init_settings,
            env_settings,
            file_secret_settings,
        ):
            return (
                json_config_settings_source,
                env_settings,
            )
