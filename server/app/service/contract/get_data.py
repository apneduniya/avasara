import typing as t
from datetime import datetime

from app.core.logging import logger
from app.service.core.api import APIService
from app.service.contract.routes import SmartContractAPIRoutes
from app.types.base import FrontendAPIResponse
from app.types.contract import (
    ContractInfoData,
    UserProfile,
    ContractInfoResponse,
    UsersBySkillResponse,
    UsersByLocationResponse,
    RegisteredUsersResponse,
    UserProfileResponse
)


class SmartContractAPI:
    """
    API client for interacting with the smart contract.
    Provides methods to fetch various types of contract data with robust error handling and validation.
    """
    
    def __init__(self):
        """
        Initialize the smart contract API client.
        """
        self.api = APIService[SmartContractAPIRoutes](
            service_name="Smart Contract API",
            base_url=SmartContractAPIRoutes.BASE
        )
        logger.info("Initialized SmartContractAPI")

    def get_contract_info(self) -> ContractInfoData:
        """
        Fetches the core information about the smart contract.

        Returns:
            ContractInfoData: Contract information containing owner and registration fee

        Raises:
            ApiError: If the API request fails
            ValidationError: If the response data is invalid
        """
        try:
            logger.info("Fetching contract info")
            response: FrontendAPIResponse[ContractInfoData] = self.api.get(SmartContractAPIRoutes.CONTRACT_INFO)
            logger.info("Successfully fetched contract info")
            return response["data"]
        except Exception as e:
            logger.error(f"Error fetching contract info: {e}")
            raise

    def get_users_by_skill(self, skill: str) -> UsersBySkillResponse:
        """
        Retrieves users who have registered with a specific skill.

        Args:
            skill (str): The skill name to filter users by.

        Returns:
            List[UserProfile]: List of user profiles matching the skill

        Raises:
            ApiError: If the API request fails
            ValueError: If skill is empty or invalid
            ValidationError: If the response data is invalid
        """
        if not skill or not isinstance(skill, str):
            raise ValueError("Skill must be a non-empty string")
            
        if len(skill.strip()) < 2:
            raise ValueError("Skill must be at least 2 characters long")

        try:
            logger.info(f"Fetching users with skill: {skill}")
            response: FrontendAPIResponse[UsersBySkillResponse] = self.api.get(
                SmartContractAPIRoutes.USERS_BY_SKILL,
                params={"skill": skill.strip()}
            )
            users = [UserProfile(**user) for user in response["data"]]
            logger.info(f"Successfully fetched {len(users)} users with skill {skill}")
            return users
        except Exception as e:
            logger.error(f"Error fetching users by skill {skill}: {e}")
            raise

    def get_users_by_location(self, location: str) -> UsersByLocationResponse:
        """
        Retrieves users who have registered from a specific location.

        Args:
            location (str): The location name to filter users by.

        Returns:
            List[UserProfile]: List of user profiles from the location

        Raises:
            ApiError: If the API request fails
            ValueError: If location is empty or invalid
            ValidationError: If the response data is invalid
        """
        if not location or not isinstance(location, str):
            raise ValueError("Location must be a non-empty string")
            
        if len(location.strip()) < 2:
            raise ValueError("Location must be at least 2 characters long")

        try:
            logger.info(f"Fetching users from location: {location}")
            response: FrontendAPIResponse[UsersByLocationResponse] = self.api.get(
                SmartContractAPIRoutes.USERS_BY_LOCATION,
                params={"location": location.strip()}
            )
            users = [UserProfile(**user) for user in response["data"]]
            logger.info(f"Successfully fetched {len(users)} users from {location}")
            return users
        except Exception as e:
            logger.error(f"Error fetching users by location {location}: {e}")
            raise

    def get_registered_users(self) -> RegisteredUsersResponse:
        """
        Retrieves all users registered in the smart contract.

        Returns:
            List[UserProfile]: List of all registered user profiles

        Raises:
            ApiError: If the API request fails
            ValidationError: If the response data is invalid
        """
        try:
            logger.info("Fetching all registered users")
            response: FrontendAPIResponse[RegisteredUsersResponse] = self.api.get(SmartContractAPIRoutes.REGISTERED_USERS)
            users = [UserProfile(**user) for user in response["data"]]
            logger.info(f"Successfully fetched {len(users)} registered users")
            return users
        except Exception as e:
            logger.error(f"Error fetching registered users: {e}")
            raise

    def get_user_profile(self, address: str) -> UserProfileResponse:
        """
        Retrieves the complete profile information for a specific user.

        Args:
            address (str): The Ethereum address of the user to fetch profile for.

        Returns:
            UserProfile: The user's complete profile information

        Raises:
            ApiError: If the API request fails
            ValueError: If address is empty or invalid
            ValidationError: If the response data is invalid
        """
        if not address or not isinstance(address, str):
            raise ValueError("Address must be a non-empty string")

        try:
            logger.info(f"Fetching profile for user: {address}")
            response: FrontendAPIResponse[UserProfileResponse] = self.api.get(
                SmartContractAPIRoutes.USER_PROFILE,
                params={"address": address.lower()}  # Normalize address to lowercase
            )
            profile = UserProfile(**response["data"])
            logger.info(f"Successfully fetched profile for user {address}")
            return profile
        except Exception as e:
            logger.error(f"Error fetching profile for user {address}: {e}")
            raise