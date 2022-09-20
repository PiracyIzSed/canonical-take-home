from typing import List, Optional

from pydantic import BaseModel, Field, HttpUrl

from app.models.domain.games import Game
from app.models.schemas.rwschema import RWSchema

DEFAULT_GAMES_LIMIT = 20
DEFAULT_GAMES_OFFSET = 0


class GameInResponse(RWSchema):
    game: Game


class GameInCreate(RWSchema):
    title: str
    age_rating: int = Field(..., ge=1)
    publisher: str
    description: str
    logo_url: Optional[HttpUrl] = None


class GameInUpdate(RWSchema):
    title: Optional[str] = None
    description: Optional[str] = None
    publisher: Optional[str] = None
    age_rating: Optional[int] = None


class ListOfGamesInResponse(RWSchema):
    games: List[Game]
    count: int


class GameFilters(BaseModel):
    publisher: Optional[str] = None
    title: Optional[str] = None
    limit: int = Field(DEFAULT_GAMES_LIMIT, ge=1)
    offset: int = Field(DEFAULT_GAMES_OFFSET, ge=0)
