#!/usr/bin/env python3
import asyncio
from typing import List
""" Task 4 - modified wait_n function
"""


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ modified wait_n function """
    delays = []
    finished: List[float] = []
    for i in range(n):
        task = task_wait_random(max_delay)
        delays.append(task)

    for task in asyncio.as_completed(delays):
        done: float = await task
        finished.append(done)

    return finished
