
from app.services.core.api import APIService
from app.services.server.routes import ContractAPIRoutes
from app.types.base import BackendAPIResponse
from app.core.logging import logger


class ContractService:
    """
    Service for interacting with the smart contract API.
    """

    def __init__(self):
        """
        Initialize the smart contract API client.
        """
        self.api = APIService[ContractAPIRoutes](
            service_name="Contract API",
            base_url=ContractAPIRoutes.BASE
        )
        logger.info("Initialized ContractAPI")

    def is_user_exists(self, telegram_username: str) -> bool:
        """
        Check if a user exists in the smart contract.
        """
        response: BackendAPIResponse = self.api.get(ContractAPIRoutes.USER_EXISTS, params={"username": telegram_username})
        return response["data"]["is_registered"]

