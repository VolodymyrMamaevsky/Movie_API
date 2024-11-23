import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "postgres")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "postgres")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "fastapi_db")
    TEST_POSTGRES_DB: str = os.getenv("TEST_POSTGRES_DB", "fastapi_test_db")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "default-secret-key")
    DEBUG: bool = os.getenv("DEBUG", "False").lower() in ("true", "1")

    @property
    def DATABASE_URL(self):
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@localhost:5432/{self.POSTGRES_DB}"

    @property
    def TEST_DATABASE_URL(self):
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@localhost:5433/{self.TEST_POSTGRES_DB}"


settings = Settings()
