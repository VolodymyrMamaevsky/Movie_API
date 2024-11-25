from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from app.config import settings


class Base(DeclarativeBase):
    pass


# Create the asynchronous engine
engine = create_async_engine(settings.DATABASE_URL, echo=True)

# Create the async session factory
AsyncSessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)


# Dependency to get the database session
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
