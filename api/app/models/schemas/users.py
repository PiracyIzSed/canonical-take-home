from typing import Optional, List

from pydantic import BaseModel, EmailStr, Field

from app.models.domain.users import User
from app.models.schemas.rwschema import RWSchema

DEFAULT_USERS_LIMIT = 20
DEFAULT_USERS_OFFSET = 0


class UserInCreate(RWSchema):
    name: str
    age: int = Field(..., ge=1)
    email: EmailStr


class UserInResponse(RWSchema):
    user: User


class UserInUpdate(BaseModel):
    email: Optional[EmailStr] = None
    age: Optional[int] = None


class ListOfUsersInResponse(RWSchema):
    users: List[User]
    count: int


class UserFilters(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    limit: int = Field(DEFAULT_USERS_LIMIT, ge=1)
    offset: int = Field(DEFAULT_USERS_OFFSET, ge=0)
