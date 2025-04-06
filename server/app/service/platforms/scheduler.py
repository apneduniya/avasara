import typing as t

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from app.service.platforms.superteam.superteam_bounty_listing import SuperteamBountyListingResourceHub


class ResourceHubScheduler:
    """
    Scheduler for resource hubs
    """

    def __init__(self):
        self.scheduler = AsyncIOScheduler()
        
        self.resource_hubs = [
            SuperteamBountyListingResourceHub
        ]

    def create_schedules(self) -> t.List:
        """
        Create the schedules for the resource hubs
        """
        for resource_hub in self.resource_hubs:
            self.scheduler.add_job(
                resource_hub.fetch,
                'interval',
                seconds=resource_hub.interval_time
            )

        return self.scheduler



