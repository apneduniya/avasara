from typing import List, Tuple

from app.models.chat import ChatOrm
from app.models.pageable import PageRequestSchema
from app.repository.chat_repository import ChatRepository


class ChatService:
    """
    Service class for handling chat-related operations.
    
    This service provides methods for managing chat messages including saving, retrieving,
    updating, and deleting messages. It also supports pagination for retrieving chat history.
    
    Attributes:
        chat_repo (ChatRepository): Repository instance for database operations
    """
    
    def __init__(self):
        """
        Initialize the ChatService with a ChatRepository instance.
        """
        self.chat_repo: ChatRepository = ChatRepository()

    async def save_message(self, chat: ChatOrm) -> ChatOrm:
        """
        Save a new chat message to the database.
        
        Args:
            chat (ChatOrm): The chat message to be saved
            
        Returns:
            ChatOrm: The saved chat message with any database-generated fields
            
        Example:
            >>> chat = ChatOrm(message="Hello", user_id=1)
            >>> saved_chat = await chat_service.save_message(chat)
        """
        return await self.chat_repo.save(chat)

    async def get_message(self, chat_id: int) -> ChatOrm:
        """
        Retrieve a specific chat message by its ID.
        
        Args:
            chat_id (int): The ID of the chat message to retrieve
            
        Returns:
            ChatOrm: The requested chat message
            
        Example:
            >>> chat = await chat_service.get_message(123)
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
            >>> user_chats = await chat_service.get_messages_by_user_id(1)
        """
        return await self.chat_repo.get_by_user_id(user_id)

    async def update_chat(self, chat_id: int, updated_chat: ChatOrm):
        """
        Update an existing chat message.
        
        Args:
            chat_id (int): The ID of the chat message to update
            updated_chat (ChatOrm): The updated chat message data
            
        Returns:
            ChatOrm: The updated chat message
            
        Example:
            >>> updated = ChatOrm(message="Updated message", timestamp=datetime.now())
            >>> result = await chat_service.update_chat(123, updated)
        """
        chat: ChatOrm = await self.chat_repo.get_by_id(chat_id)
        chat.message = updated_chat.message
        chat.timestamp = updated_chat.timestamp
        return await self.chat_repo.save(chat)

    async def delete_chat(self, chat_id: int):
        """
        Delete a chat message by its ID.
        
        Args:
            chat_id (int): The ID of the chat message to delete
            
        Returns:
            None
            
        Example:
            >>> await chat_service.delete_chat(123)
        """
        return await self.chat_repo.delete_by_id(chat_id)

    async def get_paged_chats(self, pageable: PageRequestSchema) -> Tuple[List, int]:
        """
        Retrieve paginated chat messages.
        
        Args:
            pageable (PageRequestSchema): Pagination parameters including page number and size
            
        Returns:
            Tuple[List, int]: A tuple containing:
                - List of chat messages for the current page
                - Total count of all chat messages
                
        Example:
            >>> page_request = PageRequestSchema(page=1, size=10)
            >>> chats, total = await chat_service.get_paged_chats(page_request)
        """
        return await self.chat_repo.get_paged_items(pageable, {})

