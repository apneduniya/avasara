import typing as t
import datetime

from pydantic import BaseModel
from sqlalchemy import (
    Column,
    String,
    Float,
    BigInteger,
    DateTime,
    Text,
)

from app.models.core.base import BaseOrm, BaseSchema


class ChatOrm(BaseOrm):
    __tablename__ = "chats"

    chat_id = Column(BigInteger, nullable=False)
    user_id = Column(BigInteger, nullable=False)
    username = Column(String, nullable=True)
    message_id = Column(BigInteger, nullable=False)
    message_content = Column(Text, nullable=False)
    timestamp = Column(DateTime(timezone=True), default=lambda: datetime.datetime.now(datetime.timezone.utc), nullable=False)
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



class RequestSaveMessage(BaseModel):
    chat_id: int
    user_id: int
    username: t.Optional[str] = None
    message_id: int
    message_content: str
    chat_type: str
    media: t.Optional[str] = None
    