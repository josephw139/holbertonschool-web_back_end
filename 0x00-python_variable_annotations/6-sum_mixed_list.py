#!/usr/bin/env python3
from typing import Union, List
""" Task 6 - adds lists of ints and floats
"""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """adds floats and ints"""
    sum: float = 0
    for i in mxd_lst:
        sum = sum + i

    return sum
