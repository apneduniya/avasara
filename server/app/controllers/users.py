from fastapi import APIRouter, HTTPException, Query
from fastapi_restful.cbv import cbv

from app.core.logging import logger
from app.models.core.pageable import PageRequestSchema
from app.service.chat.data import ChatService
from app.types.base import BackendAPIResponse


users_router = APIRouter()


@cbv(users_router)
class UsersController:
    def __init__(self):
        self.chat_service = ChatService()
        self.pageable = PageRequestSchema(page=1, size=10, sort='created_at', direction='DESC')

    @users_router.get("/get-chat-id-by-username", response_model=BackendAPIResponse[int])
    async def get_chat_id_by_username(self, telegram_username: str = Query(..., description="Telegram username")):
        """
        Get chat ID by username.
        """
        try:
            # Get chat id
            chat_id = await self.chat_service.get_chat_id_by_username(telegram_username)
            if chat_id is None:
                raise HTTPException(status_code=404, detail="User not found")
            
            return BackendAPIResponse(
                success=True, 
                message="Chat ID fetched successfully", 
                data=chat_id
            )
        except Exception as e:
            logger.error(f"Error fetching chat ID: {e}")
            raise HTTPException(status_code=500, detail=str(e))
