import typing as t

from openai import AsyncOpenAI
from openai.types.chat import ChatCompletion

from app.static.llm import OpenAIModel
from app.core.logging import logger
from app.models.llm import LLMResponse


LLMModelType = t.TypeVar("LLMModelType", bound=t.Union[OpenAIModel])


class LLM(t.Generic[LLMModelType]):
    """
    A generic LLM client that supports different LLM models.
    
    This class provides a unified interface for interacting with different LLM models.
    It uses type hints to ensure type safety when working with different model types.
    
    Usage:
        ```python
        # Initialize with OpenAI model
        llm = LLM(OpenAIModel.GPT_4O)
        
        # Make a chat completion request
        response = await llm.chat_completion([
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": "Hello!"}
        ])
        ```
        
    Args:
        model (LLMModelType): The LLM model to use for completions
        
    Raises:
        ValueError: If the model type is not supported
    """
    def __init__(self, model: LLMModelType):
        self.model = model
        self.client = AsyncOpenAI()

        self.model._validate_env_var()

    async def chat_completion(self, messages: t.List[t.Dict[str, t.Any]], *args, **kwargs) -> LLMResponse:
        """
        Make a chat completion request to the appropriate LLM API based on the model type.
        
        Args:
            messages (List[Dict[str, Any]]): List of message dictionaries with 'role' and 'content' keys
            *args: Additional positional arguments to pass to the underlying API call
            **kwargs: Additional keyword arguments to pass to the underlying API call
            
        Returns:
            LLMResponse: Dictionary containing the API response with at least a 'content' key
            
        Raises:
            ValueError: If the model type is not supported
            Exception: If there is an error in the API call
        """
        match self.model:
            case OpenAIModel.GPT_4O | OpenAIModel.GPT_4O_MINI:
                return await self._openai_chat_completion(messages, *args, **kwargs)
            case _:
                logger.debug(f"Unsupported model: {self.model}")
                raise ValueError(f"Unsupported model: {self.model}")

    async def _openai_chat_completion(self, messages: t.List[t.Dict[str, t.Any]], *args, **kwargs) -> LLMResponse:
        """
        Make a chat completion request to OpenAI API.
        
        Args:
            messages: List of message dictionaries with 'role' and 'content' keys
            *args: Additional positional arguments
            **kwargs: Additional keyword arguments for the API call
            
        Returns:
            LLMResponse: Dictionary containing the API response with at least a 'content' key
        """
        try:
            logger.info("Making OpenAI API request")
            response: ChatCompletion = await self.client.chat.completions.create(
                model=self.model.value,
                messages=messages,
                *args,
                **kwargs
            )
            
            return LLMResponse(content=response.choices[0].message.content)
            
        except Exception as e:
            logger.error(f"Error in OpenAI API call: {str(e)}")
            raise e

