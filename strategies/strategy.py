from abc import ABC, abstractmethod
from typing import List, Any


class BaseStrategy(ABC):
    @abstractmethod
    def execute(self, tasks: List[Any]) -> None:
        pass
