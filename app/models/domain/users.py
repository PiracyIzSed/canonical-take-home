from pydantic import EmailStr
from app.models.common import DateTimeModelMixin, IDModelMixin
from app.models.domain.rwmodel import RWModel


class User(IDModelMixin, DateTimeModelMixin, RWModel):
    age: int
    name: str
    email: EmailStr
