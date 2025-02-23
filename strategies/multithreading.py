from concurrent.futures import ThreadPoolExecutor
from typing import List, Dict, Any

from loguru import logger

from strategies.strategy import BaseStrategy
from utils.config import NUM_TASKS, MAX_WORKERS
from utils.timer import timer


def run_task_instance(task: Any) -> None:
    task.run()


def run_task(task: Any) -> Dict[str, Any]:
    with timer() as elapsed:
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            futures = [
                executor.submit(run_task_instance, task) for _ in range(NUM_TASKS)
            ]
            for future in futures:
                future.result()
    return {"task": task.__class__.__name__, "duration": elapsed()}


class MultithreadingStrategy(BaseStrategy):
    def execute(self, tasks: List[Any]) -> Dict[str, Any]:
        results = []
        for task in tasks:
            logger.info(
                f"Running task {task.__class__.__name__} with {self.__class__.__name__}"
            )
            result = run_task(task)
            results.append(result)
        return {"strategy": self.__class__.__name__, "tasks": results}
