import os

from app.core.logging import logger
from app.static.core.llm import LLMModelEnum


class OpenAIModel(LLMModelEnum):
    GPT_4O = "gpt-4o"
    GPT_4O_MINI = "gpt-4o-mini"

    @property
    def env_var(self) -> str:
        return "OPENAI_API_KEY"
    



