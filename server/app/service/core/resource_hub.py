import typing as t
from abc import ABC, abstractmethod

from app.core.logging import logger
from app.models.opportunity import Opportunity
from app.service.agent.opportunity import process_opportunity_by_chunk


class BaseResourceHub(ABC):
    """
    Abstract base class for resource hubs
    """
    
    @abstractmethod
    def fetch(self) -> t.List[t.Dict]:
        """
        Fetch opportunities from the platform
        
        Returns:
            List[Dict]: Raw opportunity data
        """
        pass

    @abstractmethod
    async def remove_existing_opportunities(self) -> t.List[t.Dict]:
        """
        Check and remove existing opportunities (which has already been fetched and saved in the database before) from the list.
        """
        pass

    @property
    @abstractmethod
    def resource_data(self) -> t.List:
        """
        Get the processed resource data
        
        Returns:
            List: Processed resource data
        """
        pass

    @property
    @abstractmethod
    def interval_time(self) -> int:
        """
        Get the interval time for fetching resources (in seconds)
        
        Returns:
            int: Interval time in seconds
        """
        pass


class ResourceHub(BaseResourceHub):
    """
    Concrete implementation of resource hub with common functionality
    """
    
    @t.final
    async def generate_opportunity(self) -> t.Optional[t.List[Opportunity]]:
        """
        Convert fetched data into Opportunity objects
        
        Returns:
            List[Opportunity]: Processed opportunities
        """
        if not self.resource_data:
            logger.warning("No resource data available to generate opportunities")
            return None
        
        try:
            logger.info(f"Generating opportunities from {len(self.resource_data)} resources")
            opportunity_data = await process_opportunity_by_chunk(self.resource_data)
            if opportunity_data is None:
                logger.warning("No opportunities found after processing all chunks")
                return None
            
            logger.info(f"Successfully generated {len(opportunity_data)} opportunities")
            return opportunity_data
        except Exception as e:
            logger.error(f"Error generating opportunities: {e}")
            raise 