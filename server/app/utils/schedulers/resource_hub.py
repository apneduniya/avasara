import typing as t

from app.service.base.resource_hub import ResourceHub


async def create_resource_hub_background_job(resource_hub_class: t.Type[ResourceHub]):
    """
    Logic for background job of resource hub schedulers
    """
    hub = resource_hub_class()
    hub.fetch()
    opportunities = await hub.generate_opportunity()

    print(opportunities)


