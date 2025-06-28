import typing as t

from app.static.llm import GeminiModel, OpenAIModel


LLMModelType = t.TypeVar("LLMModelType", bound=t.Union[OpenAIModel, GeminiModel])


