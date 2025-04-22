import asyncio

from app.core.logging import logger
from app.provider.bot_controller import get_bot_controller
from app.utils.server_consumer import ServerConsumer

async def start_bot() -> None:
    bot_controller = get_bot_controller()
    await bot_controller.start()


async def start_server_consumer() -> None:
    server_consumer = ServerConsumer()
    await server_consumer.start_consuming()


async def main() -> None:
    try:
        await asyncio.gather(
            start_bot(),
            start_server_consumer()
        )
    except KeyboardInterrupt:
        logger.info("Shutting down gracefully...")
    except Exception as e:
        logger.error(f"An error occurred: {e}")


if __name__ == "__main__":
    asyncio.run(main())