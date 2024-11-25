from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, Float


class Base(DeclarativeBase):
    pass


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, index=True)
    description = Column(String, nullable=True)
    release_year = Column(Integer, nullable=False)
    rating = Column(Float, nullable=True)
