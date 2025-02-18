import asyncio

from app.core.config import config
from app.core.logging import logger
from app.bot_controller import BotController


async def main() -> None:
    bot_controller = BotController(config.BOT_TOKEN)
    await bot_controller.start()


if __name__ == "__main__":
    logger.info("Starting bot...")
    asyncio.run(main())