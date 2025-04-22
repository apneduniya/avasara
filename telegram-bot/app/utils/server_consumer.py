import asyncio

from app.services.core.rabbitmq import RabbitMQService
from app.services.notification.telegram import TelegramNotificationService
from app.core.logging import logger
from app.core.config import config
from app.models.rabbitmq import OpportunityNotification


class ServerConsumer:
    """Consumer for processing server notifications from RabbitMQ"""
    
    def __init__(self):
        self.rabbitmq = RabbitMQService()
        self.queue_name = "opportunity_notifications"

    async def _process_message(self, message: dict) -> None:
        """Process a single notification message
        
        Args:
            message (dict): Message containing username, message, and timestamp
        """
        try:
            # Convert the message dictionary to an OpportunityNotification object
            data = OpportunityNotification(**message)

            username = data.username
            text = data.message

            telegram_notification_service = TelegramNotificationService(username=username)
            await telegram_notification_service.initialize()
            
            await telegram_notification_service.send_notification(text)
            await telegram_notification_service.end()
            logger.info(f"Successfully sent message to username: {username}")
            
        except Exception as e:
            logger.error(f"Error processing message: {str(e)}")
            raise

    async def start_consuming(self) -> None:
        """Start consuming messages from RabbitMQ"""
        try:
            logger.info("Starting Telegram notification consumer...")
            await self.rabbitmq.consume(self.queue_name, self._process_message)
        except Exception as e:
            logger.error(f"Error in consumer: {str(e)}")
            raise

    async def close(self) -> None:
        """Close RabbitMQ connections"""
        await self.rabbitmq.close()


if __name__ == "__main__":
    async def main():
        consumer = ServerConsumer()
        try:
            await consumer.start_consuming()
        except KeyboardInterrupt:
            logger.info("Stopping consumer...")
        finally:
            await consumer.close()

    asyncio.run(main())