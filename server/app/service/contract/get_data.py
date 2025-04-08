

from app.service.base.api import BaseAPIService
from app.service.contract.routes import SmartContractAPIRoutes
from app.types.contract import (
    ContractInfoResponse,
    UsersBySkillResponse,
    UsersByLocationResponse,
    RegisteredUsersResponse,
    UserProfileResponse
)


class SmartContractAPI(BaseAPIService):
    def __init__(self):
        super().__init__(
            service_name="Smart Contract API",
            base_url=SmartContractAPIRoutes.BASE,
        )

    def get_contract_info(self) -> ContractInfoResponse:
        """
        Fetches the core information about the smart contract.

        Returns:
            ContractInfoResponse: A response containing:
                - success (bool): Whether the request was successful
                - data (ContractInfoData): Contains:
                    - owner (str): The Ethereum address of the contract owner
                    - registrationFee (str): The fee required for user registration
                - message (Optional[str]): Success message if successful
                - error (Optional[str]): Error message if request failed
        """
        return self.get(SmartContractAPIRoutes.CONTRACT_INFO)

    def get_users_by_skill(self, skill: str) -> UsersBySkillResponse:
        """
        Retrieves users who have registered with a specific skill.

        Args:
            skill (str): The skill name to filter users by.

        Returns:
            UsersBySkillResponse: A response containing:
                - success (bool): Whether the request was successful
                - data (List[UserProfile]): List of user profiles containing:
                    - address (str): User's Ethereum address
                    - name (Optional[str]): User's display name
                    - skills (List[str]): List of user's skills
                    - location (Optional[str]): User's location
                    - registration_date (Optional[str]): User's registration timestamp
                - message (Optional[str]): Success message if successful
                - error (Optional[str]): Error message if request failed
        """
        return self.get(f"{SmartContractAPIRoutes.USERS_BY_SKILL}?skill={skill}")

    def get_users_by_location(self, location: str) -> UsersByLocationResponse:
        """
        Retrieves users who have registered from a specific location.

        Args:
            location (str): The location name to filter users by.

        Returns:
            UsersByLocationResponse: A response containing:
                - success (bool): Whether the request was successful
                - data (List[UserProfile]): List of user profiles containing:
                    - address (str): User's Ethereum address
                    - name (Optional[str]): User's display name
                    - skills (List[str]): List of user's skills
                    - location (Optional[str]): User's location
                    - registration_date (Optional[str]): User's registration timestamp
                - message (Optional[str]): Success message if successful
                - error (Optional[str]): Error message if request failed
        """
        return self.get(f"{SmartContractAPIRoutes.USERS_BY_LOCATION}?location={location}")

    def get_registered_users(self) -> RegisteredUsersResponse:
        """
        Retrieves all users registered in the smart contract.

        Returns:
            RegisteredUsersResponse: A response containing:
                - success (bool): Whether the request was successful
                - data (List[UserProfile]): List of all registered user profiles containing:
                    - address (str): User's Ethereum address
                    - name (Optional[str]): User's display name
                    - skills (List[str]): List of user's skills
                    - location (Optional[str]): User's location
                    - registration_date (Optional[str]): User's registration timestamp
                - message (Optional[str]): Success message if successful
                - error (Optional[str]): Error message if request failed
        """
        return self.get(SmartContractAPIRoutes.REGISTERED_USERS)

    def get_user_profile(self, address: str) -> UserProfileResponse:
        """
        Retrieves the complete profile information for a specific user.

        Args:
            address (str): The Ethereum address of the user to fetch profile for.

        Returns:
            UserProfileResponse: A response containing:
                - success (bool): Whether the request was successful
                - data (UserProfile): User's complete profile containing:
                    - address (str): User's Ethereum address
                    - name (Optional[str]): User's display name
                    - skills (List[str]): List of user's skills
                    - location (Optional[str]): User's location
                    - registration_date (Optional[str]): User's registration timestamp
                - message (Optional[str]): Success message if successful
                - error (Optional[str]): Error message if request failed
        """
        return self.get(f"{SmartContractAPIRoutes.USER_PROFILE}?address={address}")