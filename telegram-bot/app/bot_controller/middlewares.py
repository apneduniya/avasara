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

    async def __call__(
        self,
        handler: t.Callable[[types.TelegramObject, t.Dict[str, t.Any]], t.Awaitable[t.Any]],
        event: types.TelegramObject,
        data: t.Dict[str, t.Any],
    ) -> t.Any:
        message: types.Message = event.message
        log_bot_incomming_message(message)

        print(message.text)
        user_chat = ChatSchema(
            message_content=str(message.text),
            chat_id=int(message.chat.id),
            chat_type=str(message.chat.type),
            username=str(message.chat.username),
            user_id=int(message.from_user.id),
            message_id=int(message.message_id),
        )
        # await ChatService().save_message(user_chat.to_orm()) # convert pydantic to sqlalchemy and save to db
        print(user_chat.model_dump_json())

        result = await handler(event, data)
        log_bot_outgoing_message(message, result)

        # result can be both string or list of strings
        # if it is a list of strings, then we need to send each string as a separate message
        if isinstance(result, list):
            bot_response = "\n".join(result)
        else:
            bot_response = result

        if result is not None:
            bot_chat: ChatSchema = ChatSchema(
                message_content=str(bot_response),
                chat_id=int(message.chat.id),
                chat_type=str(message.chat.type),
                username="avasara_bot",
                user_id=7259245296,
                message_id=int(message.message_id) + 1,
            )
            # await ChatService().save_message(bot_chat.to_orm())
            print(bot_chat.model_dump_json())
            if isinstance(result, list):
                for item in result:
                    await message.answer(text=item, disable_web_page_preview=False)
                return
            await message.answer(text=result, disable_web_page_preview=False)


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
