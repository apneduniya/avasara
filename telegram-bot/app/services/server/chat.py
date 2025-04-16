import typing as t
import asyncio

from app.core.logging import logger
from app.models.chat import ChatSchema
from app.services.core.api import APIService
from app.services.server.routes import ChatAPIRoutes
from app.types.base import BackendAPIResponse


class ChatService:
    """
    Service for interacting with the chat API.
    """
    
    def __init__(self):
        """
        Initialize the ChatService with a ChatAPI instance.
        """
        self.api = APIService[ChatAPIRoutes](
            service_name="Chat API",
            base_url=ChatAPIRoutes.BASE
        )
        logger.info("Initialized ChatAPI")

    async def save_message(self, chat: ChatSchema) -> ChatSchema:
        """
        Save a message to the chat API.
        """
        try:
            logger.info(f"Saving {chat.username}({chat.user_id}) message of {chat.chat_id}")
            response: BackendAPIResponse[ChatSchema] = self.api.post(ChatAPIRoutes.SAVE_MESSAGE, chat.model_dump())
            return response["data"]
        except Exception as e:
            logger.error(f"Error saving message: {e}")
            raise e


if __name__ == "__main__":
    async def main():
        chat_service = ChatService()

        # Save a new message
        new_chat = ChatSchema(
            chat_id=123,
            user_id=456,
            username="thatsmeadarsh",
            message_id=123,
            message_content="Hello!",
            chat_type="text",
            media="None"
        )

        saved_chat = await chat_service.save_message(new_chat)
        message_id = saved_chat["id"]
        print(f"Saved message ID: {message_id}")

    asyncio.run(main())

