from typing import Optional

from fastapi import APIRouter, HTTPException, Query, Depends
from fastapi_restful.cbv import cbv

from app.core.logging import logger
from app.service.chat.data import ChatService
from app.types.base import BackendAPIResponse
from app.models.repository.chat import ChatSchema, RequestSaveMessage, ChatOrm

chat_router = APIRouter()


@cbv(chat_router)
class ChatController:
    def __init__(self):
        self.chat_service = ChatService()

    @chat_router.post("/save-message", response_model=BackendAPIResponse[ChatSchema])
    async def save_message(self, message: RequestSaveMessage):
        """
        Save a new chat message to the database.
        """
        chat = ChatSchema(
            chat_id=message.chat_id,
            user_id=message.user_id,
            username=message.username,
            message_id=message.message_id,
            message_content=message.message_content,
            chat_type=message.chat_type,
            media=message.media
        )
        chat_orm: ChatOrm = chat.to_orm() # from pydantic to sqlalchemy

        data = await self.chat_service.save_message(chat_orm)
        return BackendAPIResponse(
            success=True,
            message="Message saved successfully",
            data=data
        )
