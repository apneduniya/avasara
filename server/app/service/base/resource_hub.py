import typing as t
from abc import ABC, abstractmethod


class ResourceHub(ABC):
    @abstractmethod
    def fetch(self) -> t.List[t.Dict]:
        """
        Get opportunities from the platform
        """
        pass


