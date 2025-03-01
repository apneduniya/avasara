import typing as t
import datetime

from sqlalchemy import (
    Column,
    String,
    Float,
    Integer,
    DateTime,
    Text,
)
from app.models.base import BaseOrm, BaseSchema


class ChatOrm(BaseOrm):
    __tablename__ = "chats"

    chat_id = Column(Integer, primary_key=True, unique=True, nullable=False)
    user_id = Column(Integer, nullable=False)
    username = Column(String, nullable=True)
    message_id = Column(Integer, nullable=False)
    message_content = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=lambda: datetime.datetime.now(datetime.timezone.utc), nullable=False)
    chat_type = Column(String, nullable=False)
    media = Column(Text, nullable=True)


class ChatSchema(BaseSchema):
    __orm__ = ChatOrm

    chat_id: int
    user_id: int
    username: t.Optional[str] = None
    message_id: int
    message_content: str
    chat_type: str
    media: t.Optional[str] = None
