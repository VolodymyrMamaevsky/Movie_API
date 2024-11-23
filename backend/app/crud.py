from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
import models
import schemas


# Retrieve a movie by ID
async def get_movie_by_id(db: AsyncSession, movie_id: int):
    result = await db.execute(select(models.Movie).filter(models.Movie.id == movie_id))
    return result.scalars().first()


# Create a new movie
async def create_movie(db: AsyncSession, movie: schemas.MovieCreate):
    db_movie = models.Movie(**movie.dict())
    db.add(db_movie)
    await db.commit()
    await db.refresh(db_movie)
    return db_movie


# Update a movie by ID
async def update_movie(db: AsyncSession, movie_id: int, movie: schemas.MovieUpdate):
    result = await db.execute(select(models.Movie).filter(models.Movie.id == movie_id))
    db_movie = result.scalars().first()
    if not db_movie:
        return None
    for key, value in movie.dict(exclude_unset=True).items():
        setattr(db_movie, key, value)
    await db.commit()
    await db.refresh(db_movie)
    return db_movie


# Delete a movie by ID
async def delete_movie(db: AsyncSession, movie_id: int):
    result = await db.execute(select(models.Movie).filter(models.Movie.id == movie_id))
    db_movie = result.scalars().first()
    if not db_movie:
        return False
    await db.delete(db_movie)
    await db.commit()
    return True


# Retrieve all movies with pagination
async def get_movies(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(models.Movie).offset(skip).limit(limit))
    return result.scalars().all()
