#!/usr/bin/env python3
from typing import List
""" Task 5 - takes a list of floats and returns the sum
"""


def sum_list(input_list: List[float]) -> float:
    """adds the floats"""
    sum: float = 0
    for i in input_list:
        sum = sum + i

    return sum
