import asyncio
import os
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text
from app.models.core.base import BaseOrm
from app.config.settings import config
from app.core.logging import logger


async def clean_db():
    """
    Clears all data from database tables while preserving table structure.
    
    This function performs the following operations:
    1. Verifies the environment is development
    2. Creates an async database engine
    3. Temporarily disables foreign key constraints
    4. Retrieves all table names
    5. Truncates each table to remove all data
    6. Re-enables foreign key constraints
    
    Use Cases:
    - Resetting test data between test runs
    - Clearing development environment for fresh start
    - Preparing database for new data migration
    - Debugging data-related issues
    
    Safety Features:
    - Only runs in development environment
    - Preserves table structure and relationships
    - Handles foreign key constraints properly
    
    Example:
        >>> asyncio.run(clean_db())
        INFO: Cleared data from table: users
        INFO: Cleared data from table: chats
        INFO: All database tables cleared successfully!
        
    Note: This function should only be used in development environments
    as it will delete all data from all tables.
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

    # Get all table names and clear data
    async with engine.begin() as conn:
        # Get all table names
        result = await conn.execute(text("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public'
        """))
        tables = [row[0] for row in result]
        
        # Clear each table
        for table in tables:
            # Disable triggers temporarily for this table
            await conn.execute(text(f"ALTER TABLE {table} DISABLE TRIGGER ALL"))
            # Truncate the table
            await conn.execute(text(f"TRUNCATE TABLE {table} CASCADE"))
            # Re-enable triggers
            await conn.execute(text(f"ALTER TABLE {table} ENABLE TRIGGER ALL"))
            logger.info(f"Cleared data from table: {table}")

    logger.info("All database tables cleared successfully!")

if __name__ == "__main__":
    asyncio.run(clean_db())
