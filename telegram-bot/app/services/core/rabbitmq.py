import json
from typing import Any, Callable, Optional
from aio_pika import connect_robust, Message, Exchange, Channel, Connection
from aio_pika.pool import Pool

from app.core.logging import logger
from app.models.rabbitmq import RabbitMQConfig, RabbitMQMessage


class RabbitMQService:
    """RabbitMQ service for handling message queue operations.

    This service provides a robust interface for interacting with RabbitMQ, including:
    - Connection pooling for efficient resource management
    - Channel pooling for concurrent operations
    - Exchange declaration and management
    - Message publishing and consumption

    Use Cases:
    1. Asynchronous message publishing:
        ```python
        service = RabbitMQService()
        await service.publish_message("queue_name", {"data": "value"})
        ```

    2. Message consumption with callback:
        ```python
        async def handle_message(message: dict):
            print(f"Received: {message}")

        service = RabbitMQService()
        await service.consume_messages("queue_name", handle_message)
        ```

    3. Batch message processing:
        ```python
        service = RabbitMQService()
        messages = [{"id": i} for i in range(10)]
        await service.publish_batch("queue_name", messages)
        ```
    """

    def __init__(self, config: Optional[RabbitMQConfig] = None):
        """Initialize RabbitMQ service"""
        self.config = config or RabbitMQConfig()
        self.connection_pool: Optional[Pool[Connection]] = None
        self.channel_pool: Optional[Pool[Channel]] = None
        self.exchange: Optional[Exchange] = None

    async def _get_connection(self) -> Connection:
        """Get a connection from the pool"""
        if not self.connection_pool:
            self.connection_pool = Pool(
                self._create_connection,
                max_size=5
            )
        async with self.connection_pool.acquire() as connection:
            return connection

    async def _get_channel(self) -> Channel:
        """Get a channel from the pool"""
        if not self.channel_pool:
            self.channel_pool = Pool(
                self._create_channel,
                max_size=5
            )
        async with self.channel_pool.acquire() as channel:
            return channel

    async def _create_connection(self) -> Connection:
        """Create a new RabbitMQ connection"""
        return await connect_robust(
            host=self.config.host,
            port=self.config.port,
            login=self.config.username,
            password=self.config.password,
            virtualhost=self.config.virtual_host
        )

    async def _create_channel(self) -> Channel:
        """Create a new channel"""
        connection = await self._get_connection()
        return await connection.channel()

    async def _get_exchange(self) -> Exchange:
        """Get or create the exchange"""
        if not self.exchange:
            channel = await self._get_channel()
            self.exchange = await channel.declare_exchange(
                self.config.exchange_name,
                self.config.exchange_type,
                durable=True
            )
        return self.exchange

    async def publish(self, message: RabbitMQMessage) -> None:
        """
        Publish a message to RabbitMQ exchange.

        Args:
            message (RabbitMQMessage): Message to publish containing:
                - body: Message content to be JSON serialized
                - headers: Optional message headers
                - routing_key: Routing key for message delivery

        Example:
            message = RabbitMQMessage(
                body={"event": "user_created", "user_id": 123},
                headers={"priority": "high"},
                routing_key="user.events"
            )
            await rabbitmq.publish(message)
        """
        try:
            exchange = await self._get_exchange()
            await exchange.publish(
                Message(
                    body=json.dumps(message.body).encode(),
                    headers=message.headers or {}
                ),
                routing_key=message.routing_key
            )
            logger.debug(f"Published message: {message.body}")
        except Exception as e:
            logger.error(f"Error publishing message: {str(e)}")
            raise

    async def consume(self, queue_name: str, callback: Callable[[Any], None]) -> None:
        """
        Consume messages from a RabbitMQ queue and process them with callback.

        Args:
            queue_name (str): Name of the queue to consume from
            callback (Callable[[Any], None]): Async function to process messages

        Example:
            async def process_message(message):
                print(f"Received: {message}")

            await rabbitmq.consume("user_events", process_message)

        Note:
            - Queue is declared as durable
            - Messages are automatically acknowledged after callback completes
            - Exceptions in callback will be logged and re-raised
        """
        try:
            channel = await self._get_channel()
            exchange = await self._get_exchange()

            # Declare queue
            queue = await channel.declare_queue(queue_name, durable=True)
            await queue.bind(exchange, queue_name)

            logger.info(f"Started consuming from queue: {queue_name}")

            async with queue.iterator() as queue_iter:
                async for message in queue_iter:
                    async with message.process():
                        try:
                            body = json.loads(message.body.decode())
                            await callback(body)
                        except Exception as e:
                            logger.error(f"Error processing message: {str(e)}")
                            raise
        except Exception as e:
            logger.error(f"Error consuming messages: {str(e)}")
            raise

    async def close(self) -> None:
        """Close all connections and channels"""
        try:
            if self.channel_pool:
                await self.channel_pool.close()
            if self.connection_pool:
                await self.connection_pool.close()
            logger.info("Closed all RabbitMQ connections")
        except Exception as e:
            logger.error(f"Error closing connections: {str(e)}")
            raise

