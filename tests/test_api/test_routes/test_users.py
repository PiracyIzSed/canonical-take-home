from ast import List
import pytest
from fastapi import FastAPI
from httpx import AsyncClient, HTTPStatusError
from starlette import status
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.repositories.users import UsersRepository
from app.models.schemas.users import UserInResponse, User, ListOfUsersInResponse

pytestmark = pytest.mark.asyncio

async def test_user_can_not_create_users_with_same_username(
    app: FastAPI,
    client: AsyncClient,
    test_user: User,
) -> None:
    user_dict = {
        "name": test_user.name,
        "age": 16,
        "email": "jhon.doe@email.com",
    }
    response = await client.post(
        app.url_path_for("users:create-user"),
        json={ "user": user_dict }
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST

async def test_users_can_be_created(
    app: FastAPI, client: AsyncClient, 
) -> None:
    user_data = {
        "name": "game-master-1",
        "age": 16,
        "email": "game.master123@email.com"
    }
    try:
        response = await client.post(
            app.url_path_for("users:create-user"), json={"user": user_data}
        )
        response.raise_for_status()
    except HTTPStatusError as e:
        pytest.fail(f"Could not create game: {e.response.content}")
    user = UserInResponse(**response.json())
    assert user.user.name == user_data["name"]
    assert user.user.age == user_data["age"]


@pytest.mark.parametrize(
    "api_method, route_name",
    (("GET", "users:get-user"), ("PATCH", "users:update-user")),
)
async def test_cannot_fetch_or_update_non_existent_user(
    app: FastAPI,
    client: AsyncClient,
    api_method: str,
    route_name: str,
) -> None:
    response = await client.request(
        api_method, app.url_path_for(route_name, id=11111)
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND

@pytest.mark.parametrize(
    "update_field, update_value",
    (
        ("email", "new_email@email.com"),
        ("age", 14),
    ),
)
async def test_can_update_user_profile(
    app: FastAPI,
    client: AsyncClient,
    test_user: User,
    update_value: str,
    update_field: str,
) -> None:
    response = await client.patch(
        app.url_path_for("users:update-user", id=test_user.id),
        json={"user": {update_field: update_value}},
    )
    assert response.status_code == status.HTTP_200_OK

    user_profile = UserInResponse(**response.json())
    assert user_profile.user.dict()[update_field] == update_value


async def test_can_delete_a_user(
    app: FastAPI,
    client: AsyncClient,
    test_user: User,
    session: AsyncSession,
) -> None:
    await client.delete(
        app.url_path_for("users:delete-user", id=test_user.id)
    )
    user = await session.get(UsersRepository, test_user.id)
    assert not user, f"Found the user after deleltion {user.name}"

async def test_can_retrieve_user_by_id(
    app: FastAPI, client: AsyncClient, test_user: User
) -> None:
    response = await client.get(
        app.url_path_for("users:get-user", id=test_user.id)
    )
    user = UserInResponse(**response.json())
    assert user.user.id == test_user.id
    assert user.user.name == test_user.name

@pytest.mark.parametrize(
    "age, result", ((24, 1), (17, 2))
)
async def test_filtering_by_age(
    app: FastAPI,
    client: AsyncClient,
    age: int,
    result: int,
    session: AsyncSession,
) -> None:
    session.add(UsersRepository(
            name="user-42", email="user-42@email.com", age=24
        ))
    for i in range(2, 4):
        session.add(UsersRepository(
            name=f"user-{i}", email=f"user-{i}@email.com", age=17
        ))
    await session.commit()
    
    response = await client.get(
        app.url_path_for("users:list-users"), params={"age": age}
    )

    users = ListOfUsersInResponse(**response.json())
    assert users.count == result

async def test_list_users_with_limit_and_offset(
    app: FastAPI,
    client: AsyncClient,
    session: AsyncSession,
) -> None:

    for i in range(5):
        user = UsersRepository(
            name=f"user-{i}", email=f"user-{i}@email.com", age=i
        )
        session.add(user)
    await session.commit()
    full_response = await client.get(
        app.url_path_for("users:list-users")
    )
    all_users = ListOfUsersInResponse(**full_response.json())

    response = await client.get(
        app.url_path_for("users:list-users"),
        params={"limit": 2, "offset": 3},
    )

    filtered_users = ListOfUsersInResponse(**response.json())
    assert all_users.users[3:] == filtered_users.users
