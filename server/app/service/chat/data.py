import typing as t
import asyncio

from app.models.repository.chat import ChatOrm, ChatSchema
from app.models.core.pageable import PageRequestSchema, PageResponseSchema
from app.repository.chat import ChatRepository


class ChatService:
    """
    Service class for handling chat-related operations in the Avasara application.

    This service provides a comprehensive set of methods for managing chat messages,
    including CRUD operations and paginated retrieval of chat history. It acts as an
    intermediary between the application's controllers and the data layer.

    The service supports:
    - Saving new chat messages
    - Retrieving messages by ID, user ID, or chat ID
    - Updating existing messages
    - Deleting messages
    - Paginated retrieval of chat history by username, chat ID, or all chats

    Attributes:
        chat_repo (ChatRepository): Repository instance for database operations

    Example Usage:
        >>> # Initialize the service
        >>> chat_service = ChatService()

        >>> # Save a new message
        >>> new_chat = ChatOrm(
        ...     chat_id=123,
        ...     user_id=456,
        ...     message_content="Hello, world!",
        ...     chat_type="text"
        ... )
        >>> saved_chat = await chat_service.save_message(new_chat)

        >>> # Get paginated chat history
        >>> pageable = PageRequestSchema(page=1, size=10, sort='timestamp', direction='DESC')
        >>> chats = await chat_service.get_paged_chats_by_username('user123', pageable)
        >>> for chat in chats.data:
        ...     print(f"Message: {chat.message_content}")
    """

    def __init__(self):
        """Initialize the ChatService with a ChatRepository instance."""
        self.chat_repo: ChatRepository = ChatRepository()

    async def save_message(self, chat: ChatOrm) -> ChatSchema:
        """
        Save a new chat message to the database.

        Args:
            chat (ChatOrm): The chat message to be saved, containing:
                - chat_id: Unique identifier for the chat
                - user_id: ID of the user sending the message
                - message_content: The actual message text
                - chat_type: Type of message (e.g., 'text', 'media')
                - media: Optional media content
                - timestamp: Message creation time

        Returns:
            ChatSchema: The saved chat message in schema format

        Example:
            >>> new_chat = ChatOrm(
            ...     chat_id=123,
            ...     user_id=456,
            ...     message_content="Hello!",
            ...     chat_type="text"
            ... )
            >>> saved_chat = await chat_service.save_message(new_chat)
            >>> print(f"Saved message ID: {saved_chat.id}")
        """
        # Save the chat and get all its data while session is active
        saved_chat = await self.chat_repo.save(chat)

        # Convert to schema while session is still active
        return ChatSchema(
            id=saved_chat.id,
            chat_id=saved_chat.chat_id,
            user_id=saved_chat.user_id,
            username=saved_chat.username,
            message_id=saved_chat.message_id,
            message_content=saved_chat.message_content,
            created_at=saved_chat.created_at,
            updated_at=saved_chat.updated_at,
            chat_type=saved_chat.chat_type,
            media=saved_chat.media
        )

    async def get_message(self, chat_id: int) -> ChatOrm:
        """
        Retrieve a specific chat message by its ID.

        Args:
            chat_id (int): The unique identifier of the chat message to retrieve

        Returns:
            ChatOrm: The requested chat message

        Raises:
            NoResultFound: If no message exists with the given ID

        Example:
            >>> message = await chat_service.get_message(123)
            >>> print(f"Message content: {message.message_content}")
        """
        return await self.chat_repo.get_by_id(chat_id)

    async def get_messages_by_user_id(self, user_id: int) -> ChatOrm:
        """
        Retrieve all chat messages for a specific user.

        Args:
            user_id (int): The ID of the user whose messages to retrieve

        Returns:
            ChatOrm: List of chat messages for the specified user

        Example:
            >>> user_messages = await chat_service.get_messages_by_user_id(456)
            >>> for msg in user_messages:
            ...     print(f"Message: {msg.message_content}")
        """
        return await self.chat_repo.get_by_user_id(user_id)

    async def update_chat(self, chat_id: int, updated_chat: ChatOrm) -> ChatOrm:
        """
        Update an existing chat message.

        Args:
            chat_id (int): The ID of the chat message to update
            updated_chat (ChatOrm): The updated chat message data

        Returns:
            ChatOrm: The updated chat message

        Raises:
            NoResultFound: If no message exists with the given ID

        Example:
            >>> updated = ChatOrm(
            ...     message_content="Updated message",
            ...     timestamp=datetime.now()
            ... )
            >>> result = await chat_service.update_chat(123, updated)
            >>> print(f"Updated message: {result.message_content}")
        """
        chat: ChatOrm = await self.chat_repo.get_by_id(chat_id)
        chat.message_content = updated_chat.message_content
        chat.timestamp = updated_chat.timestamp
        return await self.chat_repo.save(chat)

    async def delete_chat(self, chat_id: int) -> None:
        """
        Delete a chat message by its ID.

        Args:
            chat_id (int): The ID of the chat message to delete

        Example:
            >>> await chat_service.delete_chat(123)
            >>> print("Message deleted successfully")
        """
        return await self.chat_repo.delete_by_id(chat_id)

    async def get_paged_chats_by_username(self, telegram_username: str, pageable: PageRequestSchema) -> PageResponseSchema[ChatSchema]:
        """
        Get paginated chats for a specific Telegram username.

        Args:
            telegram_username (str): The Telegram username to filter chats by
            pageable (PageRequestSchema): Pagination parameters

        Returns:
            PageResponseSchema[ChatSchema]: Paginated response with chat messages
        """
        data, total_count = await self.chat_repo.get_paged_items(pageable, {'username': telegram_username})
        total_pages = (total_count + pageable.size - 1) // pageable.size

        return PageResponseSchema(
            data=[ChatSchema.model_validate(chat) for chat in data],
            total_count=total_count,
            page_size=pageable.size,
            total_pages=total_pages
        )

    async def get_paged_chats_by_chat_id(self, chat_id: int, pageable: PageRequestSchema) -> PageResponseSchema[ChatSchema]:
        """
        Get paginated chats for a specific chat ID.

        Args:
            chat_id (int): The chat ID to filter messages by
            pageable (PageRequestSchema): Pagination parameters

        Returns:
            PageResponseSchema[ChatSchema]: Paginated response with chat messages

        Example:
            >>> pageable = PageRequestSchema(page=1, size=10)
            >>> chats = await chat_service.get_paged_chats_by_chat_id(123, pageable)
            >>> for chat in chats.data:
            ...     print(f"Message: {chat.message_content}")
        """
        data, total_count = await self.chat_repo.get_paged_items(pageable, {'chat_id': chat_id})
        total_pages = (total_count + pageable.size - 1) // pageable.size
        return PageResponseSchema(
            data=[ChatSchema.model_validate(chat) for chat in data],
            total_count=total_count,
            page_size=pageable.size,
            total_pages=total_pages
        )

    async def get_paged_chats(self, pageable: PageRequestSchema) -> PageResponseSchema[ChatSchema]:
        """
        Get all paginated chats.

        Args:
            pageable (PageRequestSchema): Pagination parameters

        Returns:
            PageResponseSchema[ChatSchema]: Paginated response with all chat messages

        Example:
            >>> pageable = PageRequestSchema(page=1, size=20)
            >>> all_chats = await chat_service.get_paged_chats(pageable)
            >>> print(f"Total messages: {all_chats.total_count}")
        """
        data, total_count = await self.chat_repo.get_paged_items(pageable, {})
        total_pages = (total_count + pageable.size - 1) // pageable.size
        return PageResponseSchema(
            data=[ChatSchema.model_validate(chat) for chat in data],
            total_count=total_count,
            page_size=pageable.size,
            total_pages=total_pages
        )

    async def get_chat_id_by_username(self, telegram_username: str) -> t.Optional[int]:
        """
        Get the chat ID associated with a Telegram username.

        This method is used to:
        - Retrieve the chat ID for a specific user
        - Support user lookup functionality
        - Enable chat history access
        - Facilitate user-specific operations

        Args:
            telegram_username (str): The Telegram username to look up

        Returns:
            int: The chat ID associated with the username, or None if not found

        Example:
            >>> chat_id = await chat_service.get_chat_id_by_username('john_doe')
            >>> if chat_id:
            ...     print(f"Found chat ID: {chat_id}")
            ... else:
            ...     print("User not found")
        """
        try:
            chat = await self.chat_repo.get_by_telegram_username(telegram_username)
            if chat is None:
                return None
            return chat.chat_id
        except Exception as e:
            # Log the error and return None to handle the case where multiple rows are found
            from app.core.logging import logger
            logger.error(f"Error getting chat ID for username {telegram_username}: {str(e)}")
            return None



if __name__ == "__main__":
    async def main():
        """
        Example usage of the ChatService.

        This demonstrates how to:
        1. Initialize the service
        2. Get paginated chats for a specific username
        3. Process and display the results
        """
        chat_service = ChatService()

        # Save a new message
        # new_chat = ChatSchema(
        #     chat_id=123,
        #     user_id=456,
        #     username="thatsmeadarsh",
        #     message_id=123,
        #     message_content="Hello!",
        #     chat_type="text",
        #     media="None"
        # )

        # saved_chat = await chat_service.save_message(new_chat.to_orm())
        # message_id = saved_chat.id
        # print(f"Saved message ID: {message_id}")

        def divider():
            print("-" * 50)

        def print_chat_data(chat: ChatSchema):
            print(f"ID: {chat.id}")
            print(f"Chat ID: {chat.chat_id}")
            print(f"User ID: {chat.user_id}")
            print(f"Username: {chat.username}")
            print(f"Message ID: {chat.message_id}")
            print(f"Message Content: {chat.message_content}")
            print(f"Created At: {chat.created_at}")
            print(f"Chat Type: {chat.chat_type}")
            print(f"Media: {chat.media}")
            divider()
        
        pageable = PageRequestSchema(page=1, size=10, sort='created_at', direction='DESC')

        # # Get paginated chats for a specific username
        # chats = await chat_service.get_paged_chats_by_username('thatsmeadarsh', pageable)
        

        # divider()
        # for chat in chats.data:
        #     print_chat_data(chat)

        # # Get paginated chats for avasara_bot
        # chats = await chat_service.get_paged_chats_by_username('avasara_bot', pageable)

        # divider()
        # for chat in chats.data:
        #     print_chat_data(chat)

        # Get paginated chats for a specific chat ID
        chat_id = 5611375328
        chats = await chat_service.get_paged_chats_by_chat_id(chat_id, pageable)

        divider()
        for chat in chats.data:
            print_chat_data(chat)

    asyncio.run(main())
