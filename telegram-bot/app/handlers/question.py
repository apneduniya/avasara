from aiogram import types

from app.bot_controller.router import Router
from app.core.config import config
from app.services.server.agent import AgentService


question_router = Router(name=__name__)
agent_service = AgentService()


# Default handler for all messages
@question_router.register()
async def ask_question(message: types.Message):
    chat_id = message.chat.id
    question = message.text

    answer = agent_service.ask_question(chat_id, question)
    return answer
