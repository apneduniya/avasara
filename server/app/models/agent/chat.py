import typing as t

from pydantic import BaseModel


class RequestAgentAskQuestion(BaseModel):
    chat_id: int
    question: str




