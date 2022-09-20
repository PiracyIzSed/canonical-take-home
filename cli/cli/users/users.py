import orjson
import typer

from . import validator
from canonical.models import (
    UserInCreate,
    UserInUpdate,
    BodyUsersCreateUserApiUsersPost,
    BodyUsersUpdateUserApiUsersIdPatch,
)
from rich import print_json, print

app = typer.Typer(
    invoke_without_command=True,
    no_args_is_help=True,
    pretty_exceptions_show_locals=False,
)


def email_validator(value: str):
    if value and not validator.is_valid_email(value):
        raise typer.BadParameter("E-Mail is not valid")
    return value


@app.command(help="Create a new user")
def create(
    ctx: typer.Context,
    name: str = typer.Option("", "--name", "-n", prompt=True, help="Name of the user"),
    age: int = typer.Option(0, "--age", "-a", prompt=True, help="Age of the user"),
    email: str = typer.Option(
        "",
        "--email",
        "-e",
        prompt=True,
        callback=email_validator,
        help="Email of the user",
    ),
):
    print("Creating the user...")
    with ctx.obj.users_api() as api:
        user = UserInCreate(name=name, age=age, email=email)
        body = BodyUsersCreateUserApiUsersPost(
            user=user,
        )
        response = api.users_create_user_api_users_post(body)
        print_json(
            orjson.dumps(response.to_dict(), option=orjson.OPT_INDENT_2).decode("utf-8")
        )


@app.command(help="Delete a user")
def delete(
    ctx: typer.Context,
    force: bool = typer.Option(False, "--force", "-f"),
    id: int = typer.Option(..., "--id", "-i", help="Get user information by id"),
):
    if not force:
        typer.confirm("Are you sure you want to delete it?", abort=True)
    print("Deleting the user...")
    with ctx.obj.users_api() as api:
        api.users_delete_user_api_users_id_delete(id)
        print("User deleted successfully")


@app.command(help="Get a user information")
def get(
    ctx: typer.Context,
    id: int = typer.Option(..., "--id", "-i", help="Get user information by id"),
):
    with ctx.obj.users_api() as api:
        response = api.users_get_user_api_users_id_get(id)
        print_json(
            orjson.dumps(response.to_dict(), option=orjson.OPT_INDENT_2).decode("utf-8")
        )


@app.command(help="Update a user information")
def update(
    ctx: typer.Context,
    id: int = typer.Option(..., "--id", "-i", help="Get user information by id"),
    age: int = typer.Option(None, "--age", "-a", help="Age of the user"),
    email: str = typer.Option(
        None, "--email", "-e", callback=email_validator, help="Email of the user"
    ),
):
    updates = {}
    if age:
        updates["age"] = age
    if email:
        updates["email"] = email
    if not updates:
        print("Nothing to update")
        raise typer.Exit()

    with ctx.obj.users_api() as api:
        user = UserInUpdate(**updates)
        body = BodyUsersUpdateUserApiUsersIdPatch(
            user=user,
        )
        response = api.users_update_user_api_users_id_patch(id, body)
        print_json(
            orjson.dumps(response.to_dict(), option=orjson.OPT_INDENT_2).decode("utf-8")
        )


@app.command(help="List Users By Parameters")
def list(
    ctx: typer.Context,
    name: str = typer.Option(None, "--name", "-n", help="Name of the user"),
    age: int = typer.Option(None, "--age", "-a", help="Age of the user"),
):
    filters = {}
    if age:
        filters["age"] = age
    if name:
        filters["name"] = name
    with ctx.obj.users_api() as api:
        response = api.users_list_users_api_users_get(**filters)
        print_json(
            orjson.dumps(response.to_dict(), option=orjson.OPT_INDENT_2).decode("utf-8")
        )
