import os

from app.core.logging import logger
from app.static.core.llm import LLMModelEnum


class OpenAIModel(LLMModelEnum):
    GPT_4O = "gpt-4o"
    GPT_4O_MINI = "gpt-4o-mini"

    @property
    def env_var(self) -> str:
        return "OPENAI_API_KEY"
    

class GeminiModel(LLMModelEnum):
    GEMINI_1_5_PRO = "gemini-1.5-pro"
    GEMINI_1_5_FLASH = "gemini-1.5-flash"
    GEMINI_2_0_FLASH = "gemini-2.0-flash"

    @property
    def env_var(self) -> str:
        return "GOOGLE_API_KEY"



