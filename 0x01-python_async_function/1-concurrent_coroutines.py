#!/usr/bin/env python3
""" Task 1 - Multiple coroutines executed together
"""


wait_random = __import__('0-basic_async_syntax').wait_random
import asyncio


async def wait_n(n, max_delay):
    i = 0
    delays = []
    finished = []
    while i < n:
        delays.append(asyncio.create_task(wait_random(max_delay)))

    for task in asyncio.as_completed(delays):
        done = await task
        finished.append(done)

    return finished
