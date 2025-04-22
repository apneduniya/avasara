from typing import Optional
from datetime import datetime
from fastapi import APIRouter, HTTPException, Query, Depends
from fastapi_restful.cbv import cbv

from app.core.logging import logger
from app.models.core.pageable import PageRequestSchema
from app.models.repository.chat import ChatSchema
from app.service.chat.data import ChatService
from app.config.settings import config
from app.static.llm import OpenAIModel, GeminiModel
from app.service.core.llm import LLM
from app.types.base import BackendAPIResponse
from app.models.agent.chat import RequestAgentAskQuestion
from app.helpers.chat.llm_message import generate_llm_message
from app.static.prompts.ask_question import SYSTEM_PROMPT


agent_router = APIRouter()


@cbv(agent_router)
class AgentController:
    def __init__(self):
        self.chat_service = ChatService()
        self.llm = LLM(OpenAIModel.GPT_4O)
        self.pageable = PageRequestSchema(page=1, size=10, sort='created_at', direction='DESC')

    @agent_router.post("/ask-question", response_model=BackendAPIResponse[str])
    async def ask_question(self, request: RequestAgentAskQuestion):
        """
        Ask a question to the agent.
        """
        try:
            # Get chat history
            chat_history = await self.chat_service.get_paged_chats_by_chat_id(request.chat_id, self.pageable)
            messages = generate_llm_message(chat_history.data)

            # Add system prompt to the messages
            prompt = SYSTEM_PROMPT.format(current_date_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            messages.insert(0, {"role": "system", "content": prompt})

            # Add user question to the messages
            question = request.question
            messages.append({"role": "user", "content": question})

            # Get response from the LLM
            response = await self.llm.chat_completion(messages)

            # Save the response to the database
            chat = ChatSchema(
                chat_id=request.chat_id,
                user_id=config.BOT_ID,
                username=config.BOT_USERNAME,
                message_id=int(chat_history.data[-1].message_id)+1,
                message_content=response.content,
                chat_type=chat_history.data[-1].chat_type,
                media=None
            )
            await self.chat_service.save_message(chat.to_orm())
            return BackendAPIResponse(success=True, message="Question asked successfully", data=response.content)
        except Exception as e:
            logger.error(f"Error asking question: {e}")
            raise HTTPException(status_code=500, detail=str(e))
