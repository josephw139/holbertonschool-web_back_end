#!/usr/bin/env python3
import random
import asyncio
""" Task 0 - takes a number and waits a random amount before returning it
"""


async def wait_random(max_delay=10):
    """ Waits random amount """
    wait = random.uniform(0, max_delay)
    await asyncio.sleep(wait)
    return wait
