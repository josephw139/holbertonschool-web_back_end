#!/usr/bin/env python3
""" Task 0 - takes a number and waits a random amount before returning it
"""


import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ Waits random amount """
    wait = random.uniform(0, max_delay)
    await asyncio.sleep(wait)
    return wait
