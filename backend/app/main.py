from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app import models, schemas, crud
from app.database import Base, engine, get_db
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="Movie API",
    description="Test task for company Indeo Solutions",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_root():
    return {"message": "Welcome to the Movie API!"}


@app.get("/movies/", response_model=List[schemas.Movie])
async def get_movies(
    skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)
):
    """Retrieve a list of movies with optional pagination."""
    return await crud.get_movies(db, skip=skip, limit=limit)


@app.get("/movies/{movie_id}", response_model=schemas.Movie)
async def get_movie(movie_id: int, db: AsyncSession = Depends(get_db)):
    """Retrieve a movie by its ID."""
    movie = await crud.get_movie_by_id(db, movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie


@app.post("/movies/", response_model=schemas.Movie)
async def create_movie(movie: schemas.MovieCreate, db: AsyncSession = Depends(get_db)):
    """Create a new movie."""
    return await crud.create_movie(db, movie)


@app.put("/movies/{movie_id}", response_model=schemas.Movie)
async def update_movie(
    movie_id: int, movie: schemas.MovieUpdate, db: AsyncSession = Depends(get_db)
):
    """Update an existing movie."""
    updated_movie = await crud.update_movie(db, movie_id, movie)
    if not updated_movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return updated_movie


@app.delete("/movies/{movie_id}")
async def delete_movie(movie_id: int, db: AsyncSession = Depends(get_db)):
    """Delete a movie by its ID."""
    success = await crud.delete_movie(db, movie_id)
    if not success:
        raise HTTPException(status_code=404, detail="Movie not found")
    return {"detail": "Movie deleted successfully"}


# Database initialization
@app.on_event("startup")
async def startup():
    """Event fired when the application starts."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.on_event("shutdown")
async def shutdown():
    """Event fired when the application shuts down."""
    await engine.dispose()
