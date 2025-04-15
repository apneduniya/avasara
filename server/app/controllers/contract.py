from fastapi import APIRouter, HTTPException, Query
from typing import Optional

from app.service.contract.get_data import SmartContractAPI
from app.types.contract import UserRegistrationStatus
from app.types.base import BackendAPIResponse
from app.core.logging import logger


router = APIRouter()


@router.get("/check-user-registration", response_model=BackendAPIResponse[UserRegistrationStatus])
async def check_user_registration(
    username: str = Query(..., description="Username to check registration status for")
) -> BackendAPIResponse[UserRegistrationStatus]:
    """
    Check if a user is registered in the system based on their username.
    
    Args:
        username (str): The username to check
        
    Returns:
        FrontendAPIResponse[UserRegistrationStatus]: The registration status of the user
        
    Raises:
        HTTPException: If the request is invalid or an error occurs
    """
    try:
        smart_contract_api = SmartContractAPI()
        registration_status = smart_contract_api.check_user_registration(username)
        
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