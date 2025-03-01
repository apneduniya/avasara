import logging

from sqlalchemy import or_, select
from sqlalchemy.exc import NoResultFound

from app.models.chat import ChatOrm, ChatSchema
from app.repository.base_repository import BaseRepository
from app.utils.db_session import get_db_session


class ChatRepository(BaseRepository):
    def __init__(self):
        super().__init__(ChatOrm)

