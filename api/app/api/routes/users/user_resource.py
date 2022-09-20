from fastapi import APIRouter, Body, Depends, HTTPException, Response
from starlette import status
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies.database import get_db
from app.api.dependencies.users import get_user_filters
from app.db.repositories.users import UsersRepository
from app.db.repositories import users as user_repo

from app.models.domain.users import User
from app.models.schemas.users import (
    ListOfUsersInResponse,
    UserFilters,
    UserInCreate,
    UserInResponse,
    UserInUpdate,
)
from app.resources import strings
from app.services.users import check_user_exists, get_users_by_filters
from app.api.dependencies.users import get_user_by_id

router = APIRouter()


@router.get("", response_model=ListOfUsersInResponse, name="users:list-users")
async def list_users(
    user_filters: UserFilters = Depends(get_user_filters),
    db: AsyncSession = Depends(get_db),
) -> ListOfUsersInResponse:
    users = await get_users_by_filters(db, user_filters.dict(exclude_none=True))
    return ListOfUsersInResponse(users=users, count=len(users))


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    response_model=UserInResponse,
    name="users:create-user",
)
async def create_new_user(
    user_create: UserInCreate = Body(..., embed=True, alias="user"),
    db: AsyncSession = Depends(get_db),
) -> UserInResponse:
    if await check_user_exists(db, user_create.name):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=strings.USER_ALREADY_EXISTS,
        )
    user = UsersRepository(**user_create.dict())
    db.add(user)
    await db.commit()
    return UserInResponse(user=user)


@router.get("/{id}", response_model=UserInResponse, name="users:get-user")
async def get_user(
    user: UsersRepository = Depends(get_user_by_id),
) -> UserInResponse:
    return UserInResponse(user=User.from_orm(user))


@router.patch(
    "/{id}",
    response_model=UserInResponse,
    name="users:update-user",
)
async def update_user_by_id(
    user_update: UserInUpdate = Body(..., embed=True, alias="user"),
    user: UsersRepository = Depends(get_user_by_id),
    db: AsyncSession = Depends(get_db),
) -> UserInResponse:
    for key, value in user_update.dict(exclude_unset=True).items():
        setattr(user, key, value)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return UserInResponse(user=user)


@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    name="users:delete-user",
    response_class=Response,
)
async def delete_user_by_slug(
    user: User = Depends(get_user_by_id), db: AsyncSession = Depends(get_db)
) -> None:
    await db.delete(user)
    await db.commit()
