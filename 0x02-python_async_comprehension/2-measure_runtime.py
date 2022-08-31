#!/usr/bin/env python3
""" Task 2 - measure runtimes
"""


import asyncio
from time import time
async_c = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ measure runtime """
    start: float = time()
    await asyncio.gather(async_c(), async_c(), async_c(), async_c())
    end: float = time()

    return end - start
