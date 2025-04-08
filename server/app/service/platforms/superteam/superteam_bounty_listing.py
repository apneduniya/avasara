import typing as t

from app.helpers.json import pretty_json

from app.service.base.api import BaseAPIService
from app.service.base.resource_hub import ResourceHub
from app.service.platforms.superteam.routes import SuperteamAPIRoutes


class SuperteamBountyListingResourceHub(BaseAPIService, ResourceHub):
    """
    Resource hub for superteam bounty listings
    """
    interval_time = 60 * 60 * 24  # 24 hours

    def __init__(self):
        super().__init__("superteam bounty listing", SuperteamAPIRoutes.BASE)
        self.raw_resource_data = []

    def fetch(self) -> t.List[t.Dict]:
        data = self.get(SuperteamAPIRoutes.SUPERTEAM_BOUNTY_LISTINGS)
        self.raw_resource_data = data
        return data

    @property
    def resource_data(self) -> t.List:
        # Deep copy to prevent accidental modifications
        # Otherwise, getting KeyError for 'unwanted fields' (those I am deleting afterwards as they have no use like 'slug') before removing them
        data = [item.copy() for item in self.raw_resource_data]
        
        # Add some information to the data
        for item in data:
            # Add a complete link to the opportunity using slug before removing it
            item["bounty_link"] = f"https://earn.superteam.fun/listing/{item['slug']}"

            # Add platform name as "superteam"
            item["platform_name"] = "superteam"

            # Remove 'unwanted fields'
            item.pop("slug")

        return data


if __name__ == "__main__":
    import asyncio

    superteam_bounty_listing = SuperteamBountyListingResourceHub()
    superteam_bounty_listing.fetch()
    opportunities = asyncio.run(
        superteam_bounty_listing.generate_opportunity())

    # Convert Opportunity objects to dictionaries for JSON serialization
    opportunity_dicts = [opp.model_dump() for opp in opportunities]
    print("Opportunity data:\n", pretty_json(opportunity_dicts), "\n\n")
