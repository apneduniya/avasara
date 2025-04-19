import asyncio
import os

from app.utils.rabbitmq import RabbitMQService


async def process_message(message):
    """Callback function to process received messages"""
    print("\n📨 Received message:")
    print(f"Body: {message}")
    print("-" * 50)

async def test_consume_messages():
    """Test consuming messages from RabbitMQ using CloudAMQP"""
    try:
        # Initialize RabbitMQ service
        rabbitmq = RabbitMQService()
        
        print("👂 Listening for messages on 'test_queue'...")
        print("Press Ctrl+C to stop")
        
        # Start consuming messages
        await rabbitmq.consume("test_queue", process_message)
        
    except KeyboardInterrupt:
        print("\n👋 Stopping consumer...")
    except Exception as e:
        print(f"❌ Error consuming messages: {str(e)}")
    finally:
        # Clean up
        await rabbitmq.close()

if __name__ == "__main__":
    asyncio.run(test_consume_messages()) 