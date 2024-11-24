from pydantic import BaseModel
from typing import Optional


# Base schema for movies
class MovieBase(BaseModel):
    """Base schema for common fields of a movie."""

    title: str
    description: Optional[str] = None
    release_year: int
    rating: Optional[float] = None


# Schema for creating a new movie
class MovieCreate(MovieBase):
    """Schema for creating a new movie."""

    pass


# Schema for updating an existing movie
class MovieUpdate(MovieBase):
    """Schema for updating a movie."""

    pass


# Schema for retrieving a movie
class Movie(MovieBase):
    """Schema for retrieving a movie with its ID."""

    id: int  # Unique identifier for the movie

    class Config:
        orm_mode = True  # Enable ORM mode to work with SQLAlchemy models
