from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, Optional
from aio_pika import ExchangeType
from pydantic import BaseModel
from app.core.config import config


@dataclass
class RabbitMQConfig:
    """RabbitMQ configuration"""
    host: str = config.RABBITMQ_HOST
    port: int = config.RABBITMQ_PORT
    username: str = config.RABBITMQ_USERNAME
    password: str = config.RABBITMQ_PASSWORD
    virtual_host: str = config.RABBITMQ_VIRTUAL_HOST
    exchange_name: str = config.RABBITMQ_EXCHANGE_NAME
    exchange_type: ExchangeType = ExchangeType.DIRECT

    def __post_init__(self):
        """Convert exchange_type string to ExchangeType enum"""
        if isinstance(self.exchange_type, str):
            self.exchange_type = ExchangeType[self.exchange_type.upper()]


@dataclass
class RabbitMQMessage:
    """RabbitMQ message structure"""
    body: Any
    routing_key: str
    headers: Optional[Dict[str, Any]] = None
    timestamp: datetime = datetime.utcnow() 


class OpportunityNotification(BaseModel):
    """Opportunity notification data"""
    username: str
    message: str
    timestamp: datetime = datetime.utcnow().isoformat()