from abc import ABC, abstractmethod
from typing import Any


class BaseTask(ABC):
    @abstractmethod
    def run(self) -> Any:
        pass

    @abstractmethod
    async def run_async(self) -> Any:
        pass
