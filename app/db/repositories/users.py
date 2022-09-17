from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import func
from app.models.schemas.users import UserInCreate, User
from . import Base
from sqlalchemy import Column, Integer, String, DateTime

class UsersRepository(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    email = Column(String, nullable=False)

    __mapper_args__ = {"eager_defaults": True}
