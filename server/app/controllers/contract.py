from typing import Optional

from fastapi import APIRouter, HTTPException, Query, Depends
from fastapi_restful.cbv import cbv

from app.service.contract.get_data import SmartContractAPI
from app.types.contract import UserRegistrationStatus
from app.types.base import BackendAPIResponse
from app.core.logging import logger


contract_router = APIRouter()


@cbv(contract_router)
class ContractController:
    def __init__(self):
        self.smart_contract_service = SmartContractAPI()

    @contract_router.get("/check-user-registration", response_model=BackendAPIResponse[UserRegistrationStatus])
    async def check_user_registration(
        self,
        username: str = Query(..., description="Username to check registration status for"),
    ) -> BackendAPIResponse[UserRegistrationStatus]:
        """
        Check if a user is registered in the system based on their username.
        """
        
        try:
            registration_status = self.smart_contract_service.check_user_registration(username)
            
            return BackendAPIResponse(
                success=True,
                message="User registration status retrieved successfully",
                data=registration_status
            )
            
        except ValueError as e:
            logger.error(f"Validation error checking user registration: {str(e)}")
            raise HTTPException(
                status_code=400,
                detail=str(e)
            )
        except Exception as e:
            logger.error(f"Error checking user registration: {str(e)}")
            raise HTTPException(
                status_code=500,
                detail="An error occurred while checking user registration"
            ) 