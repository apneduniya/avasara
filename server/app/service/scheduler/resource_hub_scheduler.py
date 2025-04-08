import typing as t
from datetime import datetime

from app.core.logging import logger
from app.config.settings import config
from app.service.core.scheduler import BaseScheduler
from app.service.core.resource_hub import ResourceHub
from app.service.scheduler.jobs.resource_hub import create_resource_hub_background_job


class ResourceHubScheduler(BaseScheduler):
    """
    Scheduler specifically for resource hubs
    """
    
    def __init__(self):
        super().__init__()
        self.resource_hubs: t.List[t.Type[ResourceHub]] = []
        logger.info("Initialized ResourceHubScheduler")

    def register_resource_hub(self, resource_hub: t.Type[ResourceHub]) -> None:
        """
        Register a resource hub for scheduling
        
        Args:
            resource_hub (Type[ResourceHub]): Resource hub class to register
        """
        self.resource_hubs.append(resource_hub)
        logger.info(f"Registered resource hub: {resource_hub.__name__}")

    def create_schedules(self) -> None:
        """Create schedules for all registered resource hubs"""
        for resource_hub_class in self.resource_hubs:
            # Create an instance to access the property
            resource_hub = resource_hub_class()
            interval = resource_hub.interval_time
            
            logger.info(f"Creating schedule for {resource_hub_class.__name__} with interval {interval} seconds")
            self.add_job(
                func=create_resource_hub_background_job,
                args=[resource_hub_class],
                trigger='interval',
                seconds=interval,
                next_run_time=datetime.now() if config.APSCHEDULER_RUN_ON_STARTUP else None
            ) 