#!/usr/bin/env python3
""" Task 4 - modified wait_n function
"""


task_wait_random = __import__('3-tasks').task_wait_random
import asyncio
from typing import List


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    i = 0
    delays = []
    finished: List[float] = []
    while i < n:
        delays.append(asyncio.create_task(task_wait_random(max_delay)))

    for task in asyncio.as_completed(delays):
        done = await task
        finished.append(done)

    return finished