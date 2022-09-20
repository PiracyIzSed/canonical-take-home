from typing import Optional

from fastapi.exceptions import HTTPException
from starlette import status
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Query, Path, Depends
from .database import get_db
from app.db.repositories.games import GamesRepository
from app.models.domain.games import Game
from app.models.schemas.games import (
    DEFAULT_GAMES_LIMIT,
    DEFAULT_GAMES_OFFSET,
    GameFilters,
)
from app.resources import strings


def get_game_filters(
    publisher: Optional[str] = None,
    title: Optional[str] = None,
    limit: int = Query(DEFAULT_GAMES_LIMIT, ge=1),
    offset: int = Query(DEFAULT_GAMES_OFFSET, ge=0),
) -> GameFilters:
    return GameFilters(
        publisher=publisher,
        title=title,
        limit=limit,
        offset=offset,
    )


async def get_game_by_id(
    id: int = Path(..., ge=1), db: AsyncSession = Depends(get_db)
) -> GamesRepository:
    game = await db.get(GamesRepository, id)
    if not game:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=strings.GAME_DOES_NOT_EXIST_ERROR,
        )
    return game
