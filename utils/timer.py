import time
from contextlib import contextmanager
from typing import Generator, Callable


def elapsed_time(start: float) -> float:
    return time.time() - start


@contextmanager
def timer() -> Generator[Callable[[], float], None, None]:
    start = time.time()
    yield lambda: elapsed_time(start)
