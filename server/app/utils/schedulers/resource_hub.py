import typing as t

from app.service.base.resource_hub import ResourceHub
from app.service.contract.get_data import SmartContractAPI
from app.static.key_skills import AVAILABLE_KEY_SKILLS
from app.types.contract import UserProfile

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
        # TODO: Check if the opportunity is already in the database or not and handle it
        # if the opportunity is already in the database, skip it
        # if the opportunity is not in the database, add it to the database

        # Check if the key skills are available valid
        if opportunity.key_skills not in AVAILABLE_KEY_SKILLS:
            opportunity.key_skills = "other"

        for key_skill in opportunity.key_skills:
            capable_users = smart_contract_api.get_users_by_skill(key_skill)
            for user in capable_users:
                user_profile = UserProfile(**user)
                print("Opportunity: ", opportunity.title)
                print("Key Skill: ", key_skill)
                print("Capable Users: ", user_profile)

