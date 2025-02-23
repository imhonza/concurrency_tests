import asyncio
import os
import time

from tasks.task import BaseTask

class SleepTask(BaseTask):
    def __init__(self, duration: float) -> None:
        self.duration = duration

    def run(self) -> None:
        time.sleep(self.duration)

    async def run_async(self) -> None:
        await asyncio.sleep(self.duration)
