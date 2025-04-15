import typing as t

from sqlalchemy import or_, select
from sqlalchemy.exc import NoResultFound

from app.models.repository.chat import ChatOrm
from app.models.core.pageable import PageRequestSchema
from app.repository.core.repository import GenericRepository
from app.repository.core.session import get_db_session


class ChatRepository(GenericRepository[ChatOrm]):
    """
    Repository class for managing chat-related database operations.
    
    This repository provides methods to interact with chat data in the database,
    including retrieving chats by various identifiers and paginated queries.
    
    Use Cases:
    - Managing user chat history and interactions
    - Supporting Telegram bot functionality
    - Implementing chat-based features
    - User authentication and verification
    - Chat analytics and monitoring
    """
    def __init__(self):
        super().__init__(ChatOrm)

    async def get_by_telegram_username(self, telegram_username: str) -> ChatOrm:
        """
        Retrieve a chat by Telegram username.

        This method is essential for:
        - User authentication and verification
        - Retrieving user chat history
        - Implementing user-specific features
        - Supporting bot commands and responses
        - User profile management

        Args:
            telegram_username (str): The Telegram username to search for

        Returns:
            ChatOrm: The chat record if found, None otherwise

        Example:
            >>> chat_repo = ChatRepository()
            >>> chat = await chat_repo.get_by_telegram_username('john_doe')
            >>> if chat:
            ...     # Process user's chat history
            ...     print(f"User {chat.username} found with {chat.message_content}")
            ... else:
            ...     # Handle new user registration
            ...     print("New user detected")
        """
        async with get_db_session() as session:
            try:
                query = select(ChatOrm).filter(ChatOrm.username == telegram_username)
                result = await session.execute(query)
                return result.scalar_one_or_none()
            except NoResultFound:
                return None

    async def get_by_chat_id(self, chat_id: int) -> ChatOrm:
        """
        Retrieve a chat by chat ID.

        This method is crucial for:
        - Message threading and context
        - Chat session management
        - Group chat handling
        - Message history retrieval
        - Chat analytics

        Args:
            chat_id (int): The unique identifier of the chat

        Returns:
            ChatOrm: The chat record if found, None otherwise

        Example:
            >>> chat_repo = ChatRepository()
            >>> chat = await chat_repo.get_by_chat_id(123456789)
            >>> if chat:
            ...     # Process chat messages
            ...     print(f"Chat found with {len(chat.messages)} messages")
            ... else:
            ...     # Handle non-existent chat
            ...     print("Chat not found")
        """
        async with get_db_session() as session:
            try:
                query = select(ChatOrm).filter(ChatOrm.chat_id == chat_id)
                result = await session.execute(query)
                return result.scalar_one_or_none()
            except NoResultFound:
                return None

    async def get_paged_items(self, pageable: PageRequestSchema, filters: dict) -> tuple[list[ChatOrm], int]:
        """
        Get paginated chat items with optional filters.

        This method supports:
        - Chat history browsing
        - Message search functionality
        - Chat analytics
        - User activity monitoring
        - Data export capabilities

        Args:
            pageable (PageRequestSchema): Pagination parameters (page, size, sort)
            filters (dict): Filter criteria for the query

        Returns:
            tuple[list[ChatOrm], int]: A tuple containing:
                - List of chat records matching the criteria
                - Total count of matching records

        Example:
            >>> chat_repo = ChatRepository()
            >>> pageable = PageRequestSchema(page=1, size=10)
            >>> filters = {"chat_type": "private"}
            >>> chats, total = await chat_repo.get_paged_items(pageable, filters)
            >>> print(f"Found {total} chats, showing page {pageable.page}")
        """
        return await super().get_paged_items(pageable, filters)
