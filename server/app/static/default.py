

from app.types.llm import LLMModelType
from app.static.llm import OpenAIModel


# Default LLM Model
DEFAULT_LLM_MODEL: LLMModelType = OpenAIModel.GPT_4O


# Default Embedding Configuration
DEFAULT_EMBEDDING_MODEL: str = "text-embedding-3-small"
DEFAULT_EMBEDDING_CHUNK_SIZE: int = 300
DEFAULT_EMBEDDING_TOP_K: int = 5


