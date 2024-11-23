import os
import requests
from sqlalchemy.orm import Session
import crud, schemas
from database import SessionLocal

# Load the API key from the .env file
API_KEY = os.getenv("TMDB_API_KEY", "default_key")
BASE_URL = "https://api.themoviedb.org/3/movie/popular"


# Function to fetch movies from the TMDb API
def fetch_movies():
    response = requests.get(
        BASE_URL, params={"api_key": API_KEY, "language": "en-US", "page": 1}
    )
    if response.status_code == 200:
        return response.json().get("results", [])
    else:
        print(f"Error fetching data: {response.status_code}")
        return []


# Function to save movies to the database
def save_movies_to_db():
    db: Session = SessionLocal()
    try:
        movies = fetch_movies()
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
                crud.create_movie(db, movie_data)
                print(f"Movie added: {movie['title']}")
            except Exception as e:
                print(f"Error adding movie {movie['title']}: {e}")
        db.commit()
    finally:
        db.close()


if __name__ == "__main__":
    save_movies_to_db()
