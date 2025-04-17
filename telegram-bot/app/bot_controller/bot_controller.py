from asyncio import CancelledError

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiohttp.web_runner import GracefulExit

from app.core.logging import logger
from app.bot_controller import middlewares
from app import handlers


class BotController:
    MIDDLEWARES = [
        # middlewares.SaveChatMiddleware,
        middlewares.AuthorizedMiddleware,
        middlewares.AutoAnswerMiddleware,
    ]

    ROUTERS = [
        handlers.base_router,
        handlers.users_router,
        handlers.question_router,
    ]

    def __init__(self, bot_token: str):
        self._bot = Bot(token=bot_token)
        self._dispatcher = Dispatcher()

        self._register_middlewares()
        self._register_routers()

    async def start(self):
        try:
            await self._dispatcher.start_polling(self._bot)
        except Exception as error:
            logger.exception("Unexpected error: %r", error, exc_info=error)
        except (GracefulExit, KeyboardInterrupt, CancelledError):
            logger.info("Bot graceful shutdown...")

    async def send_message(self, user_external_id: int, answer: str, parse_mode=ParseMode.HTML):
        await self._bot.send_message(user_external_id, answer, parse_mode=parse_mode)

    def _register_middlewares(self):
        for middleware in self.MIDDLEWARES:
            self._dispatcher.update.outer_middleware.register(middleware())

    def _register_routers(self):
        self._dispatcher.include_routers(*self.ROUTERS)