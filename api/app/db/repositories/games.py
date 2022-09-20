from . import Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy import func


class GamesRepository(Base):
    __tablename__ = "games"
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    age_rating = Column(Integer, nullable=False)
    publisher = Column(String, nullable=False)
    logo_url = Column(String)

    __mapper_args__ = {"eager_defaults": True}

    # TODO: add fetching of actual image
    @property
    async def thumbnail(self) -> str:
        return self.logo_url
