from httpx import HTTPStatusError
import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from starlette import status
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.repositories import games as games_repo
from app.db.repositories.games import GamesRepository
from app.models.schemas.games import GameInResponse, ListOfGamesInResponse
from app.models.domain.games import Game

pytestmark = pytest.mark.asyncio


async def test_user_can_not_create_game_with_duplicated_title(
    app: FastAPI, client: AsyncClient, test_game: GamesRepository
) -> None:
    game = {
        "title": test_game.title,
        "ageRating": 18,
        "description": "¯\\_(ツ)_/¯",
        "publisher": "Rockstart Studios"
    }
    response = await client.post(
        app.url_path_for("games:create-game"), json={"game": game}
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


async def test_user_can_create_game(
    app: FastAPI, client: AsyncClient, 
) -> None:
    game_data = {
        "title": "Test Slug",
        "body": "does not matter",
        "description": "¯\\_(ツ)_/¯",
        "publisher": "Rockstar Studios",
        "ageRating": 16,
    }
    try:
        response = await client.post(
            app.url_path_for("games:create-game"), json={"game": game_data}
        )
        response.raise_for_status()
    except HTTPStatusError as e:
        pytest.fail(f"Could not create game: {e.response.content}")
    game = GameInResponse(**response.json())
    assert game.game.title == game_data["title"]
    assert game.game.publisher == game_data["publisher"]


@pytest.mark.parametrize(
    "api_method, route_name",
    (("GET", "games:get-game"), ("PATCH", "games:update-game")),
)
async def test_user_can_not_interact_with_non_existent_game(
    app: FastAPI,
    client: AsyncClient,
    api_method: str,
    route_name: str,
) -> None:
    response = await client.request(
        api_method, app.url_path_for(route_name, id=11111)
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND


async def test_user_can_retrieve_game_if_exists(
    app: FastAPI, client: AsyncClient, test_game: Game
) -> None:
    response = await client.get(
        app.url_path_for("games:get-game", id=test_game.id)
    )
    game = GameInResponse(**response.json())
    assert game.game.id == test_game.id
    assert game.game.title == test_game.title


@pytest.mark.parametrize(
    "update_field, update_value",
    (
        ("title", "New Title"),
        ("description", "new description"),
        ("publisher", "new-publisher"),
    ),
)
async def test_user_can_update_game(
    app: FastAPI,
    client: AsyncClient,
    test_game: Game,
    update_field: str,
    update_value: str,
) -> None:
    response = await client.patch(
        app.url_path_for("games:update-game", id=test_game.id),
        json={"game": {update_field: update_value}},
    )

    assert response.status_code == status.HTTP_200_OK
    game = GameInResponse(**response.json())

    assert getattr(game.game, update_field) == update_value

    assert game.game.dict(exclude={ update_field, "updated_at" }) == test_game.dict(
        exclude={ update_field, "updated_at"}
    )


async def test_user_can_delete_a_game(
    app: FastAPI,
    client: AsyncClient,
    test_game: Game,
    session: AsyncSession,
) -> None:
    await client.delete(
        app.url_path_for("games:delete-game", id=test_game.id)
    )
    game = await session.get(GamesRepository, test_game.id)
    assert not game, f"Found the game after deleltion {game.title}"


@pytest.mark.parametrize(
    "publisher, result", (("Rockstar Studios", 1), ("Ubisoft", 2))
)
async def test_filtering_by_publisher(
    app: FastAPI,
    client: AsyncClient,
    publisher: str,
    result: int,
    session: AsyncSession,
) -> None:
    session.add(GamesRepository(
        publisher="Rockstar Studios",
        title="tmp-6",
        description="tmp",
        age_rating=17,
    ))
    for i in range(2, 4):
        session.add(GamesRepository(
            publisher="Ubisoft",
            title=f"tmp-{i}",
            description="tmp",
            age_rating=17,
        ))
    await session.commit()
    
    response = await client.get(
        app.url_path_for("games:list-games"), params={"publisher": publisher}
    )

    games = ListOfGamesInResponse(**response.json())
    assert games.count == result


async def test_filtering_with_limit_and_offset(
    app: FastAPI, client: AsyncClient, session: AsyncSession
) -> None:
    for i in range(5, 10):
        game = GamesRepository(
            title=f"tmp-{i}",
            description="tmp",
            publisher="Ubisoft",
            age_rating=17,
        )
        session.add(game)
    await session.commit()
    full_response = await client.get(
        app.url_path_for("games:list-games")
    )
    all_games = ListOfGamesInResponse(**full_response.json())

    response = await client.get(
        app.url_path_for("games:list-games"), params={"limit": 2, "offset": 3}
    )
    limited_games = ListOfGamesInResponse(**response.json())
    assert all_games.games[3:] == limited_games.games
