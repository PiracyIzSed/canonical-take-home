from os import environ
import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.db.repositories.games import GamesRepository
from app.db.repositories.users import UsersRepository
from app.db.repositories import Base
from app.models.domain.games import Game
from app.models.domain.users import User
from app.core.settings.app import AppSettings

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
async def session(settings: AppSettings):
    engine = create_async_engine(
        settings.database_url,
        echo=True,
    )
    async with engine.begin() as async_engine:
        await async_engine.run_sync(Base.metadata.drop_all)
        await async_engine.run_sync(Base.metadata.create_all)
    
    
    
    async_session = sessionmaker(
        engine, expire_on_commit=False, class_=AsyncSession
    )()
    async with async_session.begin():
        yield async_session

@pytest.fixture
async def client(app: FastAPI) -> AsyncClient:
    async with AsyncClient(
        app=app,
        base_url="http://testserver",
        headers={"Content-Type": "application/json"},
    ) as client:
        yield client
