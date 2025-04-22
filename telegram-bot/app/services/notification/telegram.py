import typing as t
import json

from app.core.logging import logger
from app.types.base import BackendAPIResponse

from app.services.core.notification import BaseNotificationService
from app.services.core.api import APIService
from app.services.notification.routes import TelegramAPIRoutes, UserAPIRoutes

from app.provider.bot_controller import get_bot_controller
from app.provider.bot import get_bot


class TelegramNotificationService(BaseNotificationService):
    """Telegram notification service for sending messages to users via Telegram.

    This service handles sending notifications to specific Telegram users by their username.
    It manages the bot controller lifecycle and provides methods for sending formatted messages.

    Attributes:
        username (str): The Telegram username to send notifications to
        chat_id (Optional[int]): The chat ID associated with the username, initialized during service setup
    """

    def __init__(self, username: str):
        """Initialize the Telegram notification service.

        Args:
            username (str): The Telegram username to send notifications to
        """
        self._bot_controller = get_bot_controller()
        self._bot = get_bot()
        
        self.username: str = username
        self.chat_id: t.Optional[int] = None
        self.telegram_api: APIService[TelegramAPIRoutes] = None
        self.user_api: APIService[UserAPIRoutes] = None

    async def initialize(self) -> None:
        """Initialize the service by getting the chat ID for the username.

        This method:
        1. Temporarily stops the bot controller to prevent message conflicts
        2. Attempts to find the chat ID for the given username
        3. Raises an error if the chat ID cannot be found

        Raises:
            ValueError: If the chat ID cannot be found for the given username
        """
        await self._bot_controller.close()

        self.telegram_api = APIService[TelegramAPIRoutes](
            service_name="telegram",
            base_url=TelegramAPIRoutes.BASE
        )
        self.user_api = APIService[UserAPIRoutes](
            service_name="user",
            base_url=UserAPIRoutes.BASE
        )

        self.chat_id = await self._get_chat_id_from_username(self.username)
        if self.chat_id is None:
            logger.error(f"Chat ID not found for username: {self.username}. Might be the user has not started the bot yet.")
            raise ValueError(f"Chat ID not found for username: {self.username}. Might be the user has not started the bot yet.")

    async def send_notification(self, message: str) -> None:
        """Send a notification message to the user.

        Args:
            message (str): The message to send, supports Markdown formatting
        """
        await self._bot.send_message(
            chat_id=self.chat_id,
            text=message,
            parse_mode="Markdown"
        )
        logger.info(f"Sent notification to {self.username}: {message}")

    async def _get_updates(self) -> t.List[t.Any]:
        """Get updates from the Telegram bot.

        Returns:
            List[t.Any]: A list of updates from the bot
        """
        return self.telegram_api.get(TelegramAPIRoutes.GET_UPDATES)
    
    async def _get_chat_id_from_username(self, username: str) -> t.Optional[int]:
        """Get the chat ID for a given Telegram username.

        Args:
            username (str): The Telegram username to find the chat ID for

        Returns:
            Optional[int]: The chat ID if found, None otherwise
        """
        try:
            chat_id: BackendAPIResponse[int] = self.user_api.get(UserAPIRoutes.GET_CHAT_ID_BY_USERNAME, params={"telegram_username": username})
            return chat_id["data"]
        except Exception as e:
            logger.error(f"Error getting chat ID for username: {username}. Error: {e}")
            return None
    
    async def end(self) -> None:
        """End the service by restarting the bot controller.

        This method restarts the bot controller to resume normal bot operation
        after sending notifications.
        """
        await self._bot_controller.start()


if __name__ == "__main__":
    import asyncio
    
    async def main():
        notification_service = TelegramNotificationService(username="thatsmeadarsh")
        await notification_service.initialize()  # Initialize before use
        await notification_service.send_notification("Hello world! *bold* _italic_ [link](https://www.google.com)")
        print("Notification sent!")

    asyncio.run(main())


