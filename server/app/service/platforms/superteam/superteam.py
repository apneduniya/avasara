import typing as t

from app.helpers.json import pretty_json

from app.service.base.api import BaseAPIService
from app.service.base.resource_hub import ResourceHub
from app.service.platforms.superteam.routes import SuperteamAPIRoutes


class SuperteamBountyListingResourceHub(BaseAPIService, ResourceHub):
    def __init__(self):
        super().__init__("superteam bounty listing", SuperteamAPIRoutes.BASE)

    def _bounty_listings(self):
        return self.get(SuperteamAPIRoutes.SUPERTEAM_BOUNTY_LISTINGS)

    def fetch(self) -> t.List[t.Dict]:
        return self._bounty_listings()
    


superteam_bounty_listing = SuperteamBountyListingResourceHub()
print(pretty_json(superteam_bounty_listing.fetch()))




