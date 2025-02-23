from typing import Any, Dict
from loguru import logger

from benchmarks.benchmark_runner import (
    run_cpu_benchmarks,
    run_io_benchmarks,
)
from benchmarks.report import generate_report


def main() -> None:
    benchmark_functions = {
        # "cpu": run_cpu_benchmarks,
        "io": run_io_benchmarks,
    }

    for name, func in benchmark_functions.items():
        results: Dict[str, Any] = func()
        generate_report(results, filename=f"results_{name}")
    logger.info("Benchmarking complete. HTML report generated.")


if __name__ == "__main__":
    main()
