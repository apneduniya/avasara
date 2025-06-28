import typing as t

from sqlalchemy import or_, select
from sqlalchemy.exc import NoResultFound

from app.models.core.pageable import PageRequestSchema
from app.models.repository.opportunity import OpportunityOrm
from app.repository.core.repository import GenericRepository
from app.repository.core.session import get_db_session


class OpportunityRepository(GenericRepository[OpportunityOrm]):
    """
    Repository class for managing opportunity-related database operations.
    
    This repository provides methods to interact with opportunity data in the database,
    including retrieving opportunities by various identifiers and paginated queries.
    
    Use Cases:
    - Managing opportunity data and metadata
    - Supporting opportunity-related features
    """
    def __init__(self):
        super().__init__(OpportunityOrm)

    async def get_by_platform_name(self, platform_name: str) -> OpportunityOrm:
        """
        Retrieve an opportunity by platform name.
        
        Args:
            platform_name (str): The name of the platform to search for
            
        Returns:
            OpportunityOrm: The opportunity record if found, None otherwise
        """
        async with get_db_session() as session:
            stmt = select(OpportunityOrm).where(OpportunityOrm.platform_name == platform_name)
            result = await session.execute(stmt)
            opportunity = result.scalar_one_or_none()
            return opportunity
        
    async def get_by_platform_name_and_platform_id(self, platform_name: str, platform_id: str) -> OpportunityOrm:
        """
        Retrieve an opportunity by platform name and platform ID.
        
        Args:
            platform_name (str): The name of the platform to search for
            platform_id (str): The ID of the opportunity on the platform
        
        Returns:
            OpportunityOrm: The opportunity record if found, None otherwise
        """
        async with get_db_session() as session:
            stmt = select(OpportunityOrm).where(OpportunityOrm.platform_name == platform_name, OpportunityOrm.platform_id == platform_id)
            result = await session.execute(stmt)
            opportunity = result.scalar_one_or_none()
            return opportunity
