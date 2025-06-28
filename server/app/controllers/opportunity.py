import typing as t

from fastapi import APIRouter, HTTPException, Query, Depends
from fastapi_restful.cbv import cbv

from app.core.logging import logger
from app.models.core.pageable import PageRequestSchema, PageResponseSchema
from app.service.opportunity.data import OpportunityService
from app.types.base import BackendAPIResponse
from app.models.opportunity import Opportunity as OpportunitySchema


opportunity_router = APIRouter()


@cbv(opportunity_router)
class OpportunityController:
    def __init__(self):
        self.opportunity_service = OpportunityService()

    @opportunity_router.get("/", response_model=BackendAPIResponse[PageResponseSchema[OpportunitySchema]])
    async def get_opportunities(self, pageable: PageRequestSchema = Depends(PageRequestSchema)):
        """
        Get a paginated list of opportunities.
        """
        try:
            data = await self.opportunity_service.get_paged_opportunities(pageable)

            return BackendAPIResponse[PageResponseSchema[OpportunitySchema]](
                success=True,
                message="Opportunities fetched successfully",
                data=data
            )
        except Exception as e:
            logger.error(f"Error fetching opportunities: {e}")
            raise HTTPException(
                status_code=500,
                detail=f"Error fetching opportunities: {e}"
            )
    
