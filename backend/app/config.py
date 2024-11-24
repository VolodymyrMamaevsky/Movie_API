from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Database configuration
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "fastapi_db"
    TEST_POSTGRES_DB: str = "fastapi_test_db"

    # Application secrets and keys
    SECRET_KEY: str = "default-secret-key"

    # Debug mode
    DEBUG: bool = False

    # Database URLs
    DATABASE_URL: str
    TEST_DATABASE_URL: str

    class Config:
        # Load environment variables from .env file
        env_file = ".env"
        env_file_encoding = "utf-8"


# Create an instance of settings to be used across the application
settings = Settings()
