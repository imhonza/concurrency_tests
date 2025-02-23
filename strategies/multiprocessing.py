from multiprocessing import Pool
from typing import List, Dict, Any

from strategies.strategy import BaseStrategy
from utils.config import NUM_TASKS, MAX_WORKERS
from utils.timer import timer


def run_task_instance(task: Any) -> None:
    task.run()


def run_task(task: Any) -> Dict[str, Any]:
    with timer() as elapsed:
        with Pool(processes=MAX_WORKERS) as pool:
            pool.map(run_task_instance, [task] * NUM_TASKS)
    return {"task": task.__class__.__name__, "duration": elapsed()}


class MultiprocessingStrategy(BaseStrategy):
    def execute(self, tasks: List[Any]) -> Dict[str, Any]:
        results = []
        for task in tasks:
            results.append(run_task(task))
        return {"strategy": self.__class__.__name__, "tasks": results}
