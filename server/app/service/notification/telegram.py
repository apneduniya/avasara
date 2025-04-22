import typing as t

from app.core.logging import logger

from app.service.core.api import APIService
from app.service.core.notification import BaseNotificationService
from app.service.notification.routes import TelegramAPIRoutes


class TelegramNotificationService(BaseNotificationService):
    """
    Telegram notification service
    """

    def __init__(self, username: str):
        self.username = username
        self.api = APIService[TelegramAPIRoutes](
            service_name="telegram",
            base_url=TelegramAPIRoutes.BASE
        )
        
        self.chat_id = self._get_chat_id_from_username(username)
        if self.chat_id is None:
            logger.error(f"Chat ID not found for username: {username}. Might be the user has not started the bot yet.")
            raise ValueError(f"Chat ID not found for username: {username}. Might be the user has not started the bot yet.")

    def send_notification(self, message: str) -> None:
        self.api.post(TelegramAPIRoutes.SEND_MESSAGE, data={"chat_id": self.chat_id, "text": message, "parse_mode": "Markdown"})
        logger.info(f"Sent notification to {self.username}: {message}")

    def get_updates(self) -> t.List[t.Dict]:
        return self.api.get(TelegramAPIRoutes.GET_UPDATES)

    def get_me(self) -> t.Dict:
        return self.api.get(TelegramAPIRoutes.GET_ME)
    
    def _get_chat_id_from_username(self, username: str) -> t.Optional[int]:
        response = self.get_updates()
        messages = response["result"]
        for message in messages:
            if message["message"]["from"]["username"] == username:
                return message["message"]["chat"]["id"]
        return None
    


if __name__ == "__main__":
    def main():
        notification_service = TelegramNotificationService(username="thatsmeadarsh")
        notification_service.send_notification("Hello world! *bold* _italic_ [link](https://www.google.com)")

    main()


