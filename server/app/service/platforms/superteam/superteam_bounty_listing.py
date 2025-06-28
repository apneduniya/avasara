import typing as t
import asyncio
import datetime

from app.core.logging import logger

from app.service.core.api import APIService
from app.service.core.resource_hub import ResourceHub
from app.service.platforms.superteam.routes import SuperteamAPIRoutes
from app.repository.opportunity import OpportunityRepository


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
        self.opportunity_repository = OpportunityRepository()
        self.platform_name = "superteam"

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

    async def remove_existing_opportunities(self) -> t.List[t.Dict]:
        """
        Check and remove existing opportunities (which has already been fetched and saved in the database before) from the list.
        """
        count = 0
        
        for item in self.raw_resource_data:
            opportunity = await self.opportunity_repository.get_by_platform_name_and_platform_id(self.platform_name, item["id"])
            if opportunity:
                logger.debug(f"Removing existing opportunity: {item['title']}")
                self.raw_resource_data.remove(item)
                count += 1
        logger.info(f"Removed {count} existing opportunities from the list")
        return self.raw_resource_data

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
                # Add extra metadata
                item["bounty_link"] = f"https://earn.superteam.fun/listing/{item['slug']}"
                item["platform_name"] = self.platform_name
                item["fetched_at"] = datetime.datetime.now(datetime.UTC) # Just for helping LLM to understand the data better
                
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
    from dotenv import load_dotenv

    from app.service.opportunity.data import OpportunityService
    from app.helpers.json import pretty_json

    load_dotenv()

    async def main():
        try:
            opportunity_service = OpportunityService()
            superteam_bounty_listing = SuperteamBountyListingResourceHub()

            superteam_bounty_listing.fetch()
            await superteam_bounty_listing.remove_existing_opportunities()
            
            # Generate opportunities
            opportunities = await superteam_bounty_listing.generate_opportunity()
            if opportunities is None:
                print("\nNo opportunities found\n")
                return
            
            for opportunity in opportunities:
                await opportunity_service.save(opportunity)
                print(f"\nSaved opportunity: {opportunity.title}")

            opportunities_dict = [opp.model_dump() for opp in opportunities] 
            print(f"\n\nFetched {len(opportunities)} opportunities:")
            print(pretty_json(opportunities_dict), "\n\n")
            
        except Exception as e:
            logger.error(f"Error in main execution: {e}")
            raise

    # Run the async main function
    asyncio.run(main())
