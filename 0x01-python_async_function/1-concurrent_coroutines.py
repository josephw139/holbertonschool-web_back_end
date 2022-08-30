#!/usr/bin/env python3
""" Task 1 - Multiple coroutines executed together
"""


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ multiple routines executed together """
    i = 0
    delays = []
    finished: List[float] = []
    while i < n:
        task = asyncio.create_task(wait_random(max_delay))
        delays.append(task)

    for task in asyncio.as_completed(delays):
        done: float = await task
        finished.append(done)

    return finished
