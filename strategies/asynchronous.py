import asyncio
from typing import List, Dict, Any

from loguru import logger

from strategies.strategy import BaseStrategy
from utils.config import NUM_TASKS
from utils.timer import timer


class AsyncStrategy(BaseStrategy):
    async def execute_async(self, task: Any) -> List[Any]:
        coroutines = [task.run_async() for _ in range(NUM_TASKS)]
        results = await asyncio.gather(*coroutines)
        return results

    def execute(self, tasks: List[Any]) -> Dict[str, Any]:
        results = []
        for task in tasks:
            logger.info(
                f"Running task {task.__class__.__name__} with {self.__class__.__name__}"
            )
            with timer() as elapsed:
                asyncio.run(self.execute_async(task))
                duration = elapsed()
            results.append(
                {
                    "duration": duration,
                    "task": task.__class__.__name__,
                }
            )
        return {"strategy": self.__class__.__name__, "tasks": results}
