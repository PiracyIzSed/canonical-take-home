from typing import Optional
import typer
from rich import print
from cli.games import games_app
from cli.users import users_app
from cli.config import Config
from pydantic import ValidationError
from cli.app import CLIApp

APP_NAME = "cli"
APP_VERSION = "1.0.0"


def _version_callback(value: bool) -> None:
    if value:
        print(f"{APP_NAME} v{APP_VERSION}")
        raise typer.Exit()


def main(
    ctx: typer.Context,
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    ),
):
    """
    A CLI application for managing users and games
    """
    try:
        config = Config()
        ctx.obj: CLIApp = CLIApp(config=config)
    except FileExistsError as e:
        print(f"Could not initialize cli: {e.args[1]}")
        raise typer.Exit(1)
    except ValidationError as e:
        print("Invalid Configuration for the cli:", e.errors())
        raise typer.Exit(1)


app = typer.Typer(
    callback=main,
    invoke_without_command=True,
    no_args_is_help=True,
    pretty_exceptions_show_locals=False,
)
app.add_typer(users_app, name="users")
app.add_typer(games_app, name="games")
