from typing import Optional

from fastapi import APIRouter, Body, Depends, HTTPException, Response
from starlette import status
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies.database import get_db
from app.api.dependencies.games import (
    get_game_filters,
    get_game_by_id,
)
from app.db.repositories.games import GamesRepository
from app.models.domain.games import Game
from app.models.schemas.games import (
    GameInResponse,
    ListOfGamesInResponse,
    GameInCreate,
    GameFilters,
    GameInUpdate,
)
from app.resources import strings
from app.services.games import check_game_exists, get_games_by_filters

sub_router = APIRouter()


@sub_router.get("", response_model=ListOfGamesInResponse, name="games:list-games")
async def list_games(
    game_filters: GameFilters = Depends(get_game_filters),
    db: AsyncSession = Depends(get_db)
) -> ListOfGamesInResponse: 
    games = await get_games_by_filters(db, game_filters.dict(exclude_none=True))
    return ListOfGamesInResponse(games=games, count=len(games))


@sub_router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    response_model=GameInResponse,
    name="games:create-game",
)
async def create_new_game(
    new_game: GameInCreate = Body(..., embed=True, alias="game"),
    db: AsyncSession = Depends(get_db)
) -> GameInResponse:
    if await check_game_exists(db, new_game.title):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=strings.GAME_ALREADY_EXISTS,
        )

    game = GamesRepository(**new_game.dict())
    db.add(game)
    await db.commit()
    return GameInResponse(game=game)


@sub_router.get("/{id}", response_model=GameInResponse, name="games:get-game")
async def get_by_id(
    game: GamesRepository = Depends(get_game_by_id),
    db: AsyncSession = Depends(get_db)
) -> GameInResponse:
    return GameInResponse(game=game)


@sub_router.patch(
    "/{id}",
    response_model=GameInResponse,
    name="games:update-game",
)
async def update_game_by_id(
    update_game: GameInUpdate = Body(..., embed=True, alias="game"),
    game: GamesRepository = Depends(get_game_by_id),
    db: AsyncSession = Depends(get_db)
) -> GameInResponse: 
    for key, value in update_game.dict(exclude_unset=True).items():
        setattr(game, key, value)
    db.add(game)
    await db.commit()
    await db.refresh(game)
    return GameInResponse(game=game)

    


@sub_router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    name="games:delete-game",
    response_class=Response,
)
async def delete_game_by_id(
    game: Game = Depends(get_game_by_id),
    db: AsyncSession = Depends(get_db)
) -> None: 
    await db.delete(game)
    await db.commit()

