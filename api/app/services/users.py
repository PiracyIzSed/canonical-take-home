from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.repositories.users import UsersRepository


async def check_user_exists(session: AsyncSession, name: str) -> bool:
    q = select(UsersRepository).where(UsersRepository.name == name)
    results = await session.execute(q)
    game = results.scalars().one_or_none()
    return bool(game)


async def get_users_by_filters(
    session: AsyncSession, filters: dict
) -> list[UsersRepository]:
    limit = filters.pop("limit")
    offset = filters.pop("offset")
    q = select(UsersRepository).filter_by(**filters).limit(limit).offset(offset)
    results = await session.execute(q)
    games = results.scalars().all()
    return games
