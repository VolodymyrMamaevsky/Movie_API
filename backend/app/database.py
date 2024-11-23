from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import settings
import os

DATABASE_URL = (
    settings.TEST_DATABASE_URL
    if os.getenv("USE_TEST_DB", "False").lower() in ("true", "1")
    else settings.DATABASE_URL
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
