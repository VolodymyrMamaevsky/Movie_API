import os
import asyncio
import aiohttp  # Асинхронная библиотека для HTTP-запросов
from sqlalchemy.ext.asyncio import AsyncSession
import crud, schemas
from database import AsyncSessionLocal

# Load the TMDB API key from the environment
API_KEY = os.getenv("TMDB_API_KEY", "default_key")
BASE_URL = "https://api.themoviedb.org/3/movie/popular"


# Fetch movies from TMDB API
async def fetch_movies():
    async with aiohttp.ClientSession() as session:
        async with session.get(
            BASE_URL, params={"api_key": API_KEY, "language": "en-US", "page": 1}
        ) as response:
            if response.status == 200:
                return await response.json()
            else:
                print(f"Error fetching data: {response.status}")
                return {"results": []}


# Save movies to the database
async def save_movies_to_db():
    async with AsyncSessionLocal() as db:
        movies_data = await fetch_movies()
        movies = movies_data.get("results", [])

        for movie in movies:
            try:
                movie_data = schemas.MovieCreate(
                    title=movie["title"],
                    description=movie.get("overview", ""),
                    release_year=(
                        int(movie["release_date"].split("-")[0])
                        if "release_date" in movie
                        else 0
                    ),
                    rating=movie.get("vote_average", 0.0),
                )
                await crud.create_movie(db, movie_data)
                print(f"Movie added: {movie['title']}")
            except Exception as e:
                print(f"Error adding movie {movie['title']}: {e}")
        await db.commit()


if __name__ == "__main__":
    asyncio.run(save_movies_to_db())
