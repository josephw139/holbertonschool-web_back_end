#!/usr/bin/env python3
from typing import Callable
""" Task 8 - float multiplier
"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function with the given float"""
    def func(num: float) -> float:
        """returns the function"""
        return num * multiplier
    return func
