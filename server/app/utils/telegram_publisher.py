import asyncio

from app.service.core.rabbitmq import RabbitMQService, RabbitMQMessage
from app.core.logging import logger
from app.models.rabbitmq import OpportunityNotification


class TelegramPublisher:
    """Publisher for sending Telegram notifications via RabbitMQ"""
    
    def __init__(self):
        self.rabbitmq = RabbitMQService()
        self.queue_name = "opportunity_notifications"

    async def send_notification(self, username: str, message: str) -> None:
        """Send a notification to Telegram via RabbitMQ
        
        Args:
            username (str): Telegram username to send the message to
            message (str): The message content to send
        """
        try:
            data = OpportunityNotification(
                username=username,
                message=message
            )
            notification = RabbitMQMessage(
                body=data.model_dump(),
                routing_key=self.queue_name,
                headers={
                    "type": "telegram_notification",
                    "priority": "high"
                }
            )
            
            await self.rabbitmq.publish(notification)
            logger.info(f"Published Telegram notification for username: {username}")
            
        except Exception as e:
            logger.error(f"Error publishing Telegram notification: {str(e)}")
            raise

    async def close(self) -> None:
        """Close RabbitMQ connections"""
        await self.rabbitmq.close()


# Example usage
async def main():
    publisher = TelegramPublisher()
    try:
        await publisher.send_notification(
            chat_id="123456789",
            message="<b>Hello!</b> This is a test notification.",
            parse_mode="HTML"
        )
    finally:
        await publisher.close()

if __name__ == "__main__":
    asyncio.run(main()) 