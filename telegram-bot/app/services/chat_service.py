from typing import List, Tuple

from app.models.chat import ChatOrm
from app.models.pageable import PageRequestSchema
from app.repository.chat_repository import ChatRepository


class ChatService:
    def __init__(self):
        self.chat_repo: ChatRepository = ChatRepository()

    async def save_message(self, chat: ChatOrm) -> ChatOrm:
        return await self.chat_repo.save(chat)

    async def get_message(self, chat_id: int) -> ChatOrm:
        return await self.chat_repo.get_by_id(chat_id)

    async def get_messages_by_user_id(self, user_id: int) -> ChatOrm:
        return await self.chat_repo.get_by_user_id(user_id)

    async def update_chat(self, chat_id: int, updated_chat: ChatOrm):
        chat: ChatOrm = await self.chat_repo.get_by_id(chat_id)
        chat.message = updated_chat.message
        chat.timestamp = updated_chat.timestamp
        return await self.chat_repo.save(chat)

    async def delete_chat(self, chat_id: int):
        return await self.chat_repo.delete_by_id(chat_id)

    async def get_paged_chats(self, pageable: PageRequestSchema) -> Tuple[List, int]:
        return await self.chat_repo.get_paged_items(pageable, {})

