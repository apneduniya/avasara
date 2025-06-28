import typing as t
import asyncio

from app.models.repository.opportunity import OpportunityOrm
from app.models.opportunity import Opportunity as OpportunitySchema
from app.models.core.pageable import PageRequestSchema, PageResponseSchema
from app.repository.opportunity import OpportunityRepository


class OpportunityService:
    """
    Service class for managing opportunity data.
    """

    def __init__(self):
        self.opportunity_repository = OpportunityRepository()

    async def save(self, opportunity: OpportunitySchema):
        """
        Save an opportunity to the database.

        Args:
            opportunity (OpportunitySchema): The opportunity to save.

        Returns:
            OpportunitySchema: The saved opportunity.
        """
        await self.opportunity_repository.save(opportunity.to_orm())
    
    async def get_paged_opportunities(self, pageable: PageRequestSchema) -> PageResponseSchema[OpportunitySchema]:
        """
        Get a paginated list of opportunities.
        """
        opportunities, total_count = await self.opportunity_repository.get_paged_items(pageable, {})
        opportunities_schema_list = []
        for opportunity in opportunities:
            schema = OpportunitySchema(
                id=opportunity.id,
                title=opportunity.title,
                description=opportunity.description,
                platform_name=opportunity.platform_name,
                deadline=opportunity.deadline,
                key_skills=opportunity.key_skills.split(","),
                opportunity_type=opportunity.opportunity_type,
                location=opportunity.location,
                compensation=opportunity.compensation,
                know_more_link=opportunity.know_more_link,
                platform_id=opportunity.platform_id,
                created_at=opportunity.created_at,
                updated_at=opportunity.updated_at
            )
            opportunities_schema_list.append(schema)

        total_pages = (total_count + pageable.size - 1) // pageable.size
        return PageResponseSchema[OpportunitySchema](
            data=opportunities_schema_list,
            total_count=total_count,
            page_size=pageable.size,
            total_pages=total_pages
        )