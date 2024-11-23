import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "postgres")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "postgres")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "fastapi_db")
    TEST_POSTGRES_DB: str = os.getenv("TEST_POSTGRES_DB", "fastapi_test_db")

    SECRET_KEY: str = os.getenv("SECRET_KEY", "default-secret-key")

    # Debug mode
    DEBUG: bool = os.getenv("DEBUG", "False").lower() in (
        "true",
        "1",
    )  # Debug mode (True for development)

    @property
    def DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@localhost:5432/{self.POSTGRES_DB}"

    @property
    def TEST_DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@localhost:5433/{self.TEST_POSTGRES_DB}"


# Create an instance of settings to be used across the application
settings = Settings()
