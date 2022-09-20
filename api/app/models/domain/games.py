from typing import Optional, Union

from pydantic import HttpUrl, Field
from app.models.common import DateTimeModelMixin, IDModelMixin
from app.models.domain.rwmodel import RWModel


class Game(IDModelMixin, DateTimeModelMixin, RWModel):
    title: str
    description: str
    age_rating: int
    publisher: str
    logo_url: Optional[HttpUrl]
