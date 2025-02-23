from typing import List, Dict, Any

from strategies.strategy import BaseStrategy
from utils.config import NUM_TASKS
from utils.timer import timer


class SequentialStrategy(BaseStrategy):
    def execute(self, tasks: List[Any]) -> Dict[str, Any]:
        results = []
        for task in tasks:
            with timer() as elapsed:
                for _ in range(NUM_TASKS):
                    task.run()
            results.append({"task": task.__class__.__name__, "duration": elapsed()})
        return {"strategy": self.__class__.__name__, "tasks": results}
