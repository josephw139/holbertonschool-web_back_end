#!/usr/bin/env python3
""" Task 2 - measures elapsed time
"""


wait_n = __import__('1-concurrent_coroutines').wait_n
import asyncio
from time import time


def measure_time(n, max_delay):
    """ measures the time to completion"""
    start = time()
    asyncio.run(wait_n(n, max_delay))
    end = time()

    return (end - start) / n
