from enum import Enum

from app.core.config import config


class TelegramAPIRoutes(Enum):
    """
    Enum for telegram API routes
    """

    BASE = f"https://api.telegram.org/bot{config.BOT_TOKEN}"

    SEND_MESSAGE = "/sendMessage"
    GET_ME = "/getMe"
    GET_UPDATES = "/getUpdates"


class UserAPIRoutes(Enum):
    """
    Enum for user API routes
    """

    BASE = config.API_URL

    GET_CHAT_ID_BY_USERNAME = "/users/get-chat-id-by-username"
