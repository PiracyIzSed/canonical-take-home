from typing import Optional
from app.models.schemas.users import UserFilters
from app.models.schemas.users import (
    DEFAULT_USERS_LIMIT,
    DEFAULT_USERS_OFFSET,
    UserFilters,
)
from fastapi import Query, Depends, Path, HTTPException
from starlette import status
from app.db.repositories.users import UsersRepository
from sqlalchemy.ext.asyncio import AsyncSession
from app.resources import strings
from .database import get_db


def get_user_filters(
    name: Optional[str] = None,
    age: Optional[int] = None,
    limit: int = Query(DEFAULT_USERS_LIMIT, ge=1),
    offset: int = Query(DEFAULT_USERS_OFFSET, ge=0),
) -> UserFilters:
    return UserFilters(
        name=name,
        age=age,
        limit=limit,
        offset=offset,
    )


async def get_user_by_id(
    id: int = Path(..., ge=1), db: AsyncSession = Depends(get_db)
) -> UsersRepository:
    user = await db.get(UsersRepository, id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=strings.USER_DOES_NOT_EXIST_ERROR,
        )
    return user
