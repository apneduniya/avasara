from enum import Enum

from app.config.settings import config


class SmartContractAPIRoutes(Enum):
    """
    Enum for smart contract API routes
    """

    BASE = config.FRONTEND_URL

    # Contract Info Routes
    CONTRACT_INFO = "/api/contract/info"
    
    # User-related Routes
    USERS_BY_SKILL = "/api/contract/users-by-skill"
    USERS_BY_LOCATION = "/api/contract/users-by-location"
    REGISTERED_USERS = "/api/contract/registered-users"
    USER_PROFILE = "/api/contract/user-profile"





