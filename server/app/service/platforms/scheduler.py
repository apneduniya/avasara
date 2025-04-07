import typing as t
from datetime import datetime

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from app.service.platforms.superteam.superteam_bounty_listing import SuperteamBountyListingResourceHub
from app.utils.schedulers.resource_hub import create_resource_hub_background_job
from app.config.settings import config


class ResourceHubScheduler:
    """
    Scheduler for resource hubs
    """

    def __init__(self):
        self.scheduler = AsyncIOScheduler()
        
        self.resource_hubs = [
            SuperteamBountyListingResourceHub
        ]

    def create_schedules(self):
        """
        Create the schedules for the resource hubs
        """
        for resource_hub in self.resource_hubs:
            self.scheduler.add_job(
                func=create_resource_hub_background_job,
                args=[resource_hub],
                trigger='interval',
                seconds=resource_hub.interval_time,
                next_run_time=datetime.now() if config.APSCHEDULER_RUN_ON_STARTUP else None
            )

    def start(self):
        """
        Start the scheduler
        """
        self.scheduler.start()

    def shutdown(self):
        """
        Shutdown the scheduler
        """
        self.scheduler.shutdown()

