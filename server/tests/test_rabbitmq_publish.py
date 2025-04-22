import asyncio
import os
from datetime import datetime

from app.service.core.rabbitmq import RabbitMQService
from app.models.rabbitmq import RabbitMQMessage


async def test_publish_message():
    """Test publishing a message to RabbitMQ using CloudAMQP"""
    try:
        # Initialize RabbitMQ service
        rabbitmq = RabbitMQService()
        
        # Create a test message
        message = RabbitMQMessage(
            body={
                "event": "test_event",
                "data": {
                    "id": 123,
                    "name": "Test Message",
                    "timestamp": datetime.utcnow().isoformat()
                }
            },
            routing_key="test_queue",
            headers={
                "priority": "high",
                "source": "test_publisher"
            }
        )
        
        # Publish the message
        await rabbitmq.publish(message)
        print("✅ Successfully published message to CloudAMQP")
        
    except Exception as e:
        print(f"❌ Error publishing message: {str(e)}")
    finally:
        # Clean up
        await rabbitmq.close()

if __name__ == "__main__":
    asyncio.run(test_publish_message()) 