import typing as t
from app.core.logging import logger
from app.service.core.resource_hub import ResourceHub
from app.service.opportunity.matcher import OpportunityMatcher


async def create_resource_hub_background_job(resource_hub_class: t.Type[ResourceHub]):
    """
    Background job for resource hub schedulers that fetches and processes opportunities
    
    Args:
        resource_hub_class (Type[ResourceHub]): The resource hub class to process
    """
    logger.info(f"Starting background job for {resource_hub_class.__name__}")
    
    try:
        # Initialize services
        hub = resource_hub_class()
        opportunity_matcher = OpportunityMatcher()

        # Fetch and generate opportunities
        hub.fetch()
        opportunities = await hub.generate_opportunity()
        logger.info(f"Generated {len(opportunities)} opportunities")

        # Process each opportunity
        for opportunity in opportunities:
            try:
                # TODO: Add database check for existing opportunities
                # if opportunity exists in database:
                #     continue
                
                # Match opportunity with capable users
                capable_users = opportunity_matcher.match_opportunity_with_users(opportunity)

                print("-"*100)
                print("Opportunity Title: ", opportunity.title)
                print("Opportunity Key Skills: ", opportunity.key_skills)
                print(" - " * 20)
                for user in capable_users:
                    print("Capable User: ", user.telegramUsername)
                    print(" - " * 20)
                print("-"*100)
                
                # TODO: Notify capable users
                
                logger.debug(f"Processed opportunity: {opportunity.title}")
                logger.debug(f"Found {len(capable_users)} capable users")
                
            except Exception as e:
                logger.error(f"Error processing opportunity {opportunity.title}: {e}")
                continue

        logger.info(f"Completed background job for {resource_hub_class.__name__}")
        
    except Exception as e:
        logger.error(f"Error in resource hub background job: {e}")
        raise 