import os
from abc import ABC, ABCMeta, abstractmethod

from enum import Enum, EnumMeta

from app.core.logging import logger


class ABCEnumMeta(ABCMeta, EnumMeta):
    """
    Merge of ABCMeta and EnumMeta
    """
    pass


class BaseLLMModelEnum(Enum, metaclass=ABCEnumMeta):
    """
    Base class for all LLM models
    """
    @property
    @abstractmethod
    def env_var(self) -> str:
        ...
        

class LLMModelEnum(BaseLLMModelEnum):
    """
    Generic LLM model enum
    """
    @classmethod
    def _validate_env_var(cls) -> None:
        # Get the first enum member to access the env_var property
        first_member = next(iter(cls))
        if not os.getenv(first_member.env_var):
            logger.debug(f"Environment variable for {cls.__name__} not found")
            raise ValueError(f"Environment variable for {cls.__name__} not found")
