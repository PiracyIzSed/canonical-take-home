from typing import AsyncGenerator
from fastapi import Depends
from sqlalchemy.orm import sessionmaker
from starlette.requests import Request
from sqlalchemy.ext.asyncio import AsyncSession

async def _get_session(request: Request) -> AsyncGenerator[AsyncSession, None]:
    async_session = sessionmaker(
        request.app.state.engine, expire_on_commit=False, class_=AsyncSession
    )
    async with async_session() as session:
        yield session

async def get_db(session: AsyncSession = Depends(_get_session)) -> AsyncGenerator[AsyncSession, None]:
    yield session