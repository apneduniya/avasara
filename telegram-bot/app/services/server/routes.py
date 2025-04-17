from enum import Enum

from app.core.config import config


class ContractAPIRoutes(Enum):
    BASE: str = config.API_URL

    USER_EXISTS: str = "/contract/check-user-registration"


class ChatAPIRoutes(Enum):
    BASE: str = config.API_URL

    SAVE_MESSAGE: str = "/chat/save-message"


class AgentAPIRoutes(Enum):
    BASE: str = config.API_URL

    ASK_QUESTION: str = "/agent/ask-question"

