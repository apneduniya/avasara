import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from app.models.core.base import BaseOrm
from app.config.settings import config
from app.core.logging import logger


async def init_db():
    """
    Initialize the database by recreating all tables.
    
    This function performs the following operations:
    1. Verifies the environment is development
    2. Creates an async database engine using the configured database URL
    3. Drops all existing tables to ensure a clean slate
    4. Creates all tables defined in the application's models
    5. Logs the progress and completion of the operation
    
    Use Cases:
    - Setting up a new development environment
    - Resetting the database during testing
    - Recreating tables after schema changes
    - Database migration and version control
    
    Note: This function should only be used in development environments
    as it will delete all existing data.
    
    Example:
        >>> asyncio.run(init_db())
        INFO: Dropped all existing tables
        INFO: Created all tables
        INFO: Database tables recreated successfully!
    """
    # Safety check - only allow in development
    if config.ENVIRONMENT != "development":
        logger.error("This script can only be run in development environment!")
        return

    # Create engine with connection pooling and health checks
    engine = create_async_engine(
        config.get_async_database_url(),
        pool_pre_ping=True
    )

    # Drop all existing tables to ensure clean state
    async with engine.begin() as conn:
        await conn.run_sync(BaseOrm.metadata.drop_all)
        logger.info("Dropped all existing tables")

    # Create all tables based on current model definitions
    async with engine.begin() as conn:
        await conn.run_sync(BaseOrm.metadata.create_all)
        logger.info("Created all tables")

    logger.info("Database tables recreated successfully!")

if __name__ == "__main__":
    asyncio.run(init_db()) 