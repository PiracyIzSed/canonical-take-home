import contextlib
from typing_extensions import Self
import canonical
from canonical.api import users_api, games_api
from rich.console import Console
from canonical.exceptions import (
    ApiValueError,
    ApiTypeError,
    ApiAttributeError,
    ApiException,
)
from cli.config import Config
import typer


class CLIApp:
    def __init__(self, config: Config) -> Self:
        self.config = canonical.Configuration(host=config.api_url)
        self.console: Console = Console()

    @contextlib.contextmanager
    def users_api(self):
        try:
            with canonical.ApiClient(configuration=self.config) as api_client:
                yield users_api.UsersApi(api_client)
            raise typer.Exit()
        except (ApiValueError, ApiTypeError, ApiAttributeError) as e:
            self.console.print("Users API Errored:")
            self.console.print(e)
            raise typer.Exit(1)
        except (ApiException) as e:
            self.console.print("Users API Failed:")
            self.console.print_json(e.body)
            raise typer.Exit(1)

    @contextlib.contextmanager
    def games_api(self):
        try:
            with canonical.ApiClient(configuration=self.config) as api_client:
                yield games_api.GamesApi(api_client)
            raise typer.Exit()
        except (ApiValueError, ApiTypeError, ApiAttributeError) as e:
            self.console.print("Games API Errored:")
            self.console.print(e)
            raise typer.Exit(1)
        except (ApiException) as e:
            self.console.print("Games API Failed:")
            self.console.print_json(e.body)
            raise typer.Exit(1)
