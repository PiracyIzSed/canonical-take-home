from datetime import timezone
from os import environ
import pytest
from fastapi import FastAPI
from asgi_lifespan import LifespanManager
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.db.repositories import Base
from app.db.repositories.games import GamesRepository
from app.db.repositories.users import UsersRepository
from app.models.domain.users import User
from app.models.domain.games import Game
from app.core.settings.app import AppSettings
from app.models.schemas.games import GameInResponse

environ["APP_ENV"] = "dev"

@pytest.fixture
def settings() -> AppSettings:
    from app.core.config import get_app_settings
    return get_app_settings()

@pytest.fixture
def app(settings: AppSettings) -> FastAPI:
    from app import get_application  # local import for testing purpose
    return get_application(settings)

@pytest.fixture
async def initialized_app(app: FastAPI, settings: AppSettings) -> FastAPI:
    async with LifespanManager(app):
        engine = create_async_engine(
            settings.database_url,
            echo=True
        )
        async with engine.begin() as async_engine:
            await async_engine.run_sync(Base.metadata.drop_all)
            await async_engine.run_sync(Base.metadata.create_all)
        app.state.engine = engine
        yield app

@pytest.fixture
async def session(initialized_app: FastAPI):
    engine = initialized_app.state.engine
    async_session = sessionmaker(
        engine, expire_on_commit=False, class_=AsyncSession,
    )
    async with async_session() as session:
        yield session

@pytest.fixture
async def client(initialized_app: FastAPI) -> AsyncClient:
    async with AsyncClient(
        app=initialized_app,
        base_url="http://testserver",
        headers={"Content-Type": "application/json"},
    ) as client:
        yield client

@pytest.fixture
async def test_user(session) -> User:
    user = UsersRepository(
        name="john",
        age=16,
        email="john.doe@gmail.com"
    )
    session.add(user)
    await session.commit()
    return User.from_orm(user)


@pytest.fixture
async def test_game(session) -> Game:
    game = GamesRepository(
        title="Test Game",
        description="Slug for tests",
        age_rating=17,
        publisher="Rockstar Studios",
        logo_url="https://mysite.com/test_logo.png"
    )
    session.add(game)
    await session.commit()
    game_obj = Game.from_orm(game)
    # FIXME: a hack to insert timezone information into the db object because the db object is missing it even though the timezone is UTC
    game_obj.created_at = game_obj.created_at.replace(tzinfo=timezone.utc)
    return game_obj