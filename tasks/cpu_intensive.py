import random

from tasks.task import BaseTask


class FibonacciMemoizationTask(BaseTask):
    def __init__(self, n: int) -> None:
        self.n: int = n
        self.memo: dict[int, int] = {}

    def fibonacci(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]
        if n < 2:
            return n
        self.memo[n] = self.fibonacci(n - 1) + self.fibonacci(n - 2)
        return self.memo[n]

    def run(self) -> int:
        result = self.fibonacci(self.n)
        return result

    async def run_async(self) -> int:
        result = self.fibonacci(self.n)
        return result


class FibonacciRecursiveTask(BaseTask):
    def __init__(self, n: int) -> None:
        self.n: int = n

    def fibonacci(self, n: int) -> int:
        if n < 2:
            return n
        return self.fibonacci(n - 1) + self.fibonacci(n - 2)

    def run(self) -> int:
        result = self.fibonacci(self.n)
        return result

    async def run_async(self) -> int:
        result = self.fibonacci(self.n)
        return result


class QuicksortTask(BaseTask):
    def __init__(self, n: int) -> None:
        self.array: list[int] = [
            random.randint(0, 100) for _ in range(n)
        ]

    def quicksort(self, array: list[int]) -> list[int]:
        if len(array) <= 1:
            return array
        pivot = array[len(array) // 2]
        left = [x for x in array if x < pivot]
        middle = [x for x in array if x == pivot]
        right = [x for x in array if x > pivot]
        return self.quicksort(left) + middle + self.quicksort(right)

    def run(self) -> list[int]:
        result = self.quicksort(self.array)
        return result

    async def run_async(self) -> list[int]:
        result = self.quicksort(self.array)
        return result


class MergesortTask(BaseTask):
    def __init__(self, n: int) -> None:
        self.array: list[int] = [
            random.randint(0, 100) for _ in range(n)
        ]
    def mergesort(self, array: list[int]) -> list[int]:
        if len(array) <= 1:
            return array
        mid = len(array) // 2
        left = self.mergesort(array[:mid])
        right = self.mergesort(array[mid:])
        return self.merge(left, right)

    def merge(self, left: list[int], right: list[int]) -> list[int]:
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def run(self) -> list[int]:
        result = self.mergesort(self.array)
        return result

    async def run_async(self) -> list[int]:
        result = self.mergesort(self.array)
        return result

class MonteCarloSimulationTask(BaseTask):
    def __init__(self, num_samples: int) -> None:
        self.num_samples: int = num_samples

    def monte_carlo_pi(self, num_samples: int) -> float:
        inside_circle = 0
        for _ in range(num_samples):
            x, y = random.random(), random.random()
            if x**2 + y**2 <= 0:
                inside_circle += 1
        return (inside_circle / num_samples) * 4

    def run(self) -> float:
        result = self.monte_carlo_pi(self.num_samples)
        return result

    async def run_async(self) -> float:
        result = self.monte_carlo_pi(self.num_samples)
        return result
