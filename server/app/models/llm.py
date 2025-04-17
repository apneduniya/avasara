import typing as t

from pydantic import BaseModel


class LLMResponse(BaseModel):
    content: str


