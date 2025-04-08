import typing as t

from app.service.base.resource_hub import ResourceHub
from app.service.contract.get_data import SmartContractAPI


async def create_resource_hub_background_job(resource_hub_class: t.Type[ResourceHub]):
    """
    Logic for background job of resource hub schedulers
    """
    hub = resource_hub_class()
    smart_contract_api = SmartContractAPI()

    # Fetch and generate opportunities
    hub.fetch()
    opportunities = await hub.generate_opportunity()

    for opportunity in opportunities:
        ...

