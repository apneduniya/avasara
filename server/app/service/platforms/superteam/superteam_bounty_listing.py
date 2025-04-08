import typing as t
import asyncio
from datetime import datetime

from app.helpers.json import pretty_json
from app.core.logging import logger

from app.service.core.api import APIService
from app.service.core.resource_hub import ResourceHub
from app.service.platforms.superteam.routes import SuperteamAPIRoutes


class SuperteamBountyListingResourceHub(ResourceHub):
    """
    Resource hub for superteam bounty listings.
    Fetches and processes bounty listings from Superteam's API.
    """
    
    def __init__(self):
        """
        Initialize the resource hub with API service and default values
        """
        self.api = APIService[SuperteamAPIRoutes](
            service_name="superteam_bounty_listing",
            base_url=SuperteamAPIRoutes.BASE
        )
        self.raw_resource_data = []
        logger.info("Initialized SuperteamBountyListingResourceHub")

    @property
    def interval_time(self) -> int:
        """Get the interval time for fetching resources (in seconds)"""
        return 60 * 60 * 24  # 24 hours

    def fetch(self) -> t.List[t.Dict]:
        """
        Fetch bounty listings from Superteam API
        
        Returns:
            List[Dict]: Raw bounty listing data
            
        Raises:
            ApiError: If the API request fails
        """
        try:
            logger.info("Fetching Superteam bounty listings")
            data = self.api.get(SuperteamAPIRoutes.SUPERTEAM_BOUNTY_LISTINGS)
            if not isinstance(data, list):
                logger.error(f"Unexpected response format: {type(data)}")
                return []
                
            self.raw_resource_data = data
            logger.info(f"Successfully fetched {len(data)} bounty listings")
            return data
        except Exception as e:
            logger.error(f"Error fetching Superteam bounty listings: {e}")
            raise

    @property
    def resource_data(self) -> t.List[t.Dict]:
        """
        Get processed bounty listing data with additional metadata
        
        Returns:
            List[Dict]: Processed bounty listing data
        """
        if not self.raw_resource_data:
            logger.warning("No raw data available for processing")
            return []

        try:
            # Create a deep copy to prevent accidental modifications
            data = [item.copy() for item in self.raw_resource_data]
            
            logger.debug("Processing bounty listings data")
            for item in data:
                # Add metadata
                item["bounty_link"] = f"https://earn.superteam.fun/listing/{item['slug']}"
                item["platform_name"] = "superteam"
                item["fetched_at"] = datetime.utcnow().isoformat()
                
                # Remove unnecessary fields
                item.pop("slug", None)
                
                # Ensure required fields exist
                item.setdefault("title", "Untitled Bounty")
                item.setdefault("description", "")
                item.setdefault("reward", 0)
                item.setdefault("status", "active")
                
                # Clean up description
                if "description" in item:
                    item["description"] = item["description"].strip()

            logger.debug(f"Processed {len(data)} bounty listings")
            return data
        except Exception as e:
            logger.error(f"Error processing bounty listings: {e}")
            return []


if __name__ == "__main__":
    async def main():
        try:
            # Initialize and fetch data
            superteam_bounty_listing = SuperteamBountyListingResourceHub()
            superteam_bounty_listing.fetch()
            
            # Generate opportunities
            opportunities = await superteam_bounty_listing.generate_opportunity()
            
            # Convert to dictionaries for JSON serialization
            opportunity_dicts = [opp.model_dump() for opp in opportunities]
            
            # Log results
            logger.info("Opportunity data:")
            logger.info(pretty_json(opportunity_dicts))
            
        except Exception as e:
            logger.error(f"Error in main execution: {e}")
            raise

    # Run the async main function
    asyncio.run(main())
