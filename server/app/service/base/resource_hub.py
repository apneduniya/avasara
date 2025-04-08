import typing as t
from abc import ABC, abstractmethod

from app.models.opportunity import Opportunity
from app.service.agent.opportunity import process_opportunity_by_chunk


class ResourceHub(ABC):
    @abstractmethod
    def fetch(self) -> t.List[t.Dict]:
        """
        Get opportunities from the platform

        Args:
            None

        Returns:
            List[Dict]: A list of dictionaries containing opportunity data
        """
        pass

    @t.final
    async def generate_opportunity(self) -> t.List[Opportunity] | t.List:
        """
        Convert the fetched data into a list of opportunities of type Opportunity

        Args:
            None

        Returns:
            List[Opportunity]: A list of Opportunity instances
        """
        # print("Resource data:\n", self.resource_data, "\n\n")
        if not self.resource_data:
            return []
        
        opportunity_data = await process_opportunity_by_chunk(self.resource_data)
        return opportunity_data
    

    @property
    @abstractmethod
    def resource_data(self) -> t.List:
        """
        The fetched data from the platform is stored in this property
        """
        pass

    @property
    @abstractmethod
    def interval_time(self) -> int:
        """
        The interval time (in seconds) for the resource hub
        """
        pass
        
