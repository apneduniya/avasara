import typing as t
from datetime import datetime

from aiogram import BaseMiddleware
from aiogram import types

from app.helpers.logs import log_bot_incomming_message, log_bot_outgoing_message
from app.services.chat_service import ChatService
from app.models.chat import ChatSchema


class AutoAnswerMiddleware(BaseMiddleware):
    """
    - This logs the incoming message and the outgoing message.
    - This send the response from the handlers to the user.
    """
    _processed_messages = set()

    async def __call__(
        self,
        handler: t.Callable[[types.TelegramObject, t.Dict[str, t.Any]], t.Awaitable[t.Any]],
        event: types.TelegramObject,
        data: t.Dict[str, t.Any],
    ) -> t.Any:
        message: types.Message = event.message
        
        # Skip if we've already processed this message
        message_key = f"{message.chat.id}_{message.message_id}"
        if message_key in self._processed_messages:
            return None
        self._processed_messages.add(message_key)

        log_bot_incomming_message(message)

        user_chat = ChatSchema(
            message_content=str(message.text),
            chat_id=int(message.chat.id),
            chat_type=str(message.chat.type),
            username=str(message.chat.username),
            user_id=int(message.from_user.id),
            message_id=int(message.message_id),
        )
        await ChatService().save_message(user_chat.to_orm())

        result = await handler(event, data)
        log_bot_outgoing_message(message, result)

        if result is not None:
            bot_response = "\n".join(result) if isinstance(result, list) else result
            
            bot_chat: ChatSchema = ChatSchema(
                message_content=str(bot_response),
                chat_id=int(message.chat.id),
                chat_type=str(message.chat.type),
                username="avasara_bot",
                user_id=7259245296,
                message_id=int(message.message_id) + 1,
            )
            await ChatService().save_message(bot_chat.to_orm())
            
            if isinstance(result, list):
                for item in result:
                    await message.answer(text=item, disable_web_page_preview=False)
            else:
                await message.answer(text=result, disable_web_page_preview=False)
            
            return None


# class SaveChatMiddleware(BaseMiddleware):
#     """
#     - This saves the incoming message to the database.
#     """
#     async def __call__(
#         self,
#         handler: t.Callable[[types.TelegramObject, t.Dict[str, t.Any]], t.Awaitable[t.Any]],
#         event: types.TelegramObject,
#         data: t.Dict[str, t.Any],
#     ) -> t.Any:
#         message: types.Message = event.message
#         user_chat = {}
#         user_chat["message_content"] = message.text
#         user_chat["chat_id"] = message.chat.id
#         user_chat["chat_type"] = message.chat.type
#         user_chat["username"] = message.chat.username
#         user_chat["user_id"] = message.from_user.id
#         user_chat["message_id"] = message.message_id
#         user_chat["timestamp"] = message.date

#         print(user_chat)

#         result = await handler(event, data)

#         if result is not None:
#             bot_chat = {}
#             if isinstance(result, list):
#                 bot_chat["message_content"] = "\n".join(result)
#             else:
#                 bot_chat["message_content"] = result
#             bot_chat["chat_id"] = message.chat.id
#             bot_chat["chat_type"] = message.chat.type
#             bot_chat["username"] = "awasara_bot"
#             bot_chat["user_id"] = "7259245296"
#             bot_chat["message_id"] = int(message.message_id) + 1
#             bot_chat["timestamp"] = datetime.now()

#             print(bot_chat)
