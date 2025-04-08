from enum import Enum

from app.config.settings import config


class TelegramAPIRoutes(Enum):
    """
    Enum for telegram API routes
    """

    BASE = f"https://api.telegram.org/bot{config.TELEGRAM_BOT_TOKEN}"

    SEND_MESSAGE = "/sendMessage"
    GET_ME = "/getMe"
    GET_UPDATES = "/getUpdates"


