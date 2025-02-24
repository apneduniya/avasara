import typing as t

from aiogram import BaseMiddleware
from aiogram import types

from app.helpers.logs import log_bot_incomming_message, log_bot_outgoing_message


class AutoAnswerMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: t.Callable[[types.TelegramObject, t.Dict[str, t.Any]], t.Awaitable[t.Any]],
        event: types.TelegramObject,
        data: t.Dict[str, t.Any],
    ) -> t.Any:
        message = event.message
        log_bot_incomming_message(message)

        result = await handler(event, data)
        log_bot_outgoing_message(message, result)

        if result is not None:
            if isinstance(result, list):
                for item in result:
                    await message.answer(text=item, disable_web_page_preview=False)
                return
            await message.answer(text=result, disable_web_page_preview=False)
