import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from app.models.base import Base
from app.models.chat import ChatOrm
from app.core.config import config


async def init_db():
    # Create engine
    engine = create_async_engine(
        config.get_async_database_url(),
        pool_pre_ping=True
    )

    # Drop all tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

    # Create all tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    print("Database tables recreated successfully!")

if __name__ == "__main__":
    asyncio.run(init_db()) 