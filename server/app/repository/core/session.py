from contextlib import asynccontextmanager

from sqlalchemy import AsyncAdaptedQueuePool
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession

from app.config.settings import config


async_url = config.get_async_database_url()
engine = create_async_engine(
    async_url,
    pool_pre_ping=True,
    poolclass=AsyncAdaptedQueuePool,
    pool_size=5,
    max_overflow=10
)
sessionmaker = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False
)


@asynccontextmanager
async def get_db_session() -> AsyncSession:  # type: ignore
    session = sessionmaker()
    try:
        yield session
        await session.commit()
    except Exception:
        await session.rollback()
        raise
    finally:
        await session.close()


async def shutdown() -> None:
    if engine is not None:
        await engine.dispose()
