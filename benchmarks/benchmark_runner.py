from typing import List, Dict, Any
from loguru import logger

from strategies.sequential import SequentialStrategy
from strategies.multithreading import MultithreadingStrategy
from strategies.multiprocessing import MultiprocessingStrategy
from strategies.asynchronous import AsyncStrategy

from tasks.cpu_intensive import (
    FibonacciRecursiveTask,
    FibonacciMemoizationTask,
    QuicksortTask,
    MergesortTask,
    MonteCarloSimulationTask,
)
from tasks.io_intensive import (
    SleepTask,
)


def run_cpu_benchmarks() -> List[Dict[str, Any]]:
    tasks_list: List[Any] = [
        FibonacciMemoizationTask(n=300),
        FibonacciRecursiveTask(n=30),
        QuicksortTask(n=10**5),
        MergesortTask(n=10**5),
        MonteCarloSimulationTask(num_samples=10**6),
    ]

    strategies: List[Any] = [
        SequentialStrategy(),
        AsyncStrategy(),
        MultithreadingStrategy(),
        MultiprocessingStrategy(),
    ]

    benchmark_results: List[Dict[str, Any]] = []

    for strat in strategies:
        logger.info(f"Running benchmark with {strat.__class__.__name__}...")
        result: Dict[str, Any] = strat.execute(tasks_list)
        benchmark_results.append(result)

    return benchmark_results

def run_io_benchmarks() -> List[Dict[str, Any]]:
    tasks_list: List[Any] = [
        SleepTask(duration=0.2),
    ]

    strategies: List[Any] = [
        SequentialStrategy(),
        AsyncStrategy(),
        MultithreadingStrategy(),
        MultiprocessingStrategy(),
    ]

    benchmark_results: List[Dict[str, Any]] = []

    for strat in strategies:
        logger.info(f"Running benchmark with {strat.__class__.__name__}...")
        result: Dict[str, Any] = strat.execute(tasks_list)
        benchmark_results.append(result)

    return benchmark_results
