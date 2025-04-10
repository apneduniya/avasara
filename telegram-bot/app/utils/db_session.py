from contextlib import asynccontextmanager

from sqlalchemy import AsyncAdaptedQueuePool
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession

from app.core.config import config


async_url = config.get_async_database_url()
engine = create_async_engine(
    async_url,
    pool_pre_ping=True,
    poolclass=AsyncAdaptedQueuePool,
    pool_size=1,
    max_overflow=1
)
sessionmaker = async_sessionmaker(bind=engine, expire_on_commit=False)


@asynccontextmanager
async def get_db_session() -> AsyncSession: # type: ignore
    session = sessionmaker()
    async with session.begin():
        yield session


async def shutdown() -> None:
    if engine is not None:
        await engine.dispose()
