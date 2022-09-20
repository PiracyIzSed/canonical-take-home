import typer
import orjson
from canonical.models import (
    GameInCreate,
    GameInUpdate,
    BodyGamesCreateGameApiGamesPost,
    BodyGamesUpdateGameApiGamesIdPatch,
    Game,
)
from rich import print_json, print

app = typer.Typer(
    invoke_without_command=True,
    no_args_is_help=True,
    pretty_exceptions_show_locals=False,
)


@app.command(help="Create a new game")
def create(
    ctx: typer.Context,
    title: str = typer.Option(
        "", "--title", "-t", prompt=True, help="Title of the game"
    ),
    age_rating: int = typer.Option(
        0, "--age-rating", prompt=True, help="Age Rating of the game"
    ),
    publisher: str = typer.Option(
        "", "--publisher", prompt=True, help="Publisher of the game"
    ),
    description: str = typer.Option(
        "", "--description", prompt=True, help="Description of the game"
    ),
    logo_url: str = typer.Option(None, "--logo-url", help="Logo URL for the game"),
):
    print("Creating the game...")
    with ctx.obj.games_api() as api:
        game = GameInCreate(
            title=title,
            age_rating=age_rating,
            publisher=publisher,
            description=description,
            logo_url=logo_url,
        )
        body = BodyGamesCreateGameApiGamesPost(game=game)
        response = api.games_create_game_api_games_post(body)

        print_json(
            orjson.dumps(response.to_dict(), option=orjson.OPT_INDENT_2).decode("utf-8")
        )


@app.command(help="Delete a game")
def delete(
    ctx: typer.Context,
    force: bool = typer.Option(False, "--force", "-f"),
    id: int = typer.Option(..., "--id", "-i", help="Get game information by id"),
):
    if not force:
        typer.confirm("Are you sure you want to delete it?", abort=True)
    print("Deleting the game...")
    with ctx.obj.games_api() as api:
        api.games_delete_game_api_games_id_delete(id)
        print("Game deleted successfully")


@app.command(help="Get a game's information")
def get(
    ctx: typer.Context,
    id: int = typer.Option(..., "--id", "-i", help="Get game information by id"),
):
    with ctx.obj.games_api() as api:
        response = api.games_get_game_api_games_id_get(id)
        print_json(
            orjson.dumps(response.to_dict(), option=orjson.OPT_INDENT_2).decode("utf-8")
        )


@app.command(help="Update a game")
def update(
    ctx: typer.Context,
    id: int = typer.Option(..., "--id", "-i", help="ID of the game"),
    title: str = typer.Option(None, "--title", "-t", help="New title of the game"),
    age_rating: int = typer.Option(
        None, "--age-rating", help="New age rating of the game"
    ),
    description: str = typer.Option(
        None, "--description", "-d", help="New description of the game"
    ),
    publisher: str = typer.Option(
        None, "--publisher", "-p", help="New publisher of the game"
    ),
    logo_url: str = typer.Option(None, "--logo-url", help="New logo url of the game"),
):
    updates = {}
    if title:
        updates["title"] = title
    if description:
        updates["description"] = description
    if age_rating:
        updates["age_rating"] = age_rating
    if publisher:
        updates["publisher"] = publisher
    if logo_url:
        updates["logo_url"] = logo_url

    if not updates:
        print("Nothing to update")
        raise typer.Exit()

    with ctx.obj.games_api() as api:
        game = GameInUpdate(**updates)
        body = BodyGamesUpdateGameApiGamesIdPatch(
            game=game,
        )
        response = api.games_update_game_api_games_id_patch(id, body)
        print_json(
            orjson.dumps(response.to_dict(), option=orjson.OPT_INDENT_2).decode("utf-8")
        )


@app.command(help="List Games By Parameters")
def list(
    ctx: typer.Context,
    publisher: str = typer.Option(None, "--publisher", help="List games by publisher"),
    age_rating: int = typer.Option(
        None, "--age-rating", help="List games by age ratings"
    ),
):
    filters = {}
    if age_rating:
        filters["age_rating"] = age_rating
    if publisher:
        filters["publisher"] = publisher
    with ctx.obj.games_api() as api:
        response = api.games_list_games_api_games_get(**filters)
        print_json(
            orjson.dumps(response.to_dict(), option=orjson.OPT_INDENT_2).decode("utf-8")
        )
