from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.repositories.games import GamesRepository


async def check_game_exists(session: AsyncSession, title: str) -> bool:
    q = select(GamesRepository).where(GamesRepository.title == title)
    results = await session.execute(q)
    game = results.scalars().one_or_none()
    return bool(game)


async def get_games_by_filters(
    session: AsyncSession, filters: dict
) -> list[GamesRepository]:
    limit = filters.pop("limit")
    offset = filters.pop("offset")
    q = select(GamesRepository).filter_by(**filters).limit(limit).offset(offset)
    results = await session.execute(q)
    games = results.scalars().all()
    return games
