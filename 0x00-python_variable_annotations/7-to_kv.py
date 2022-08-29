#!/usr/bin/env python3
from typing import Tuple, Union
""" Task 7 - returns a tuple
"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns the string and square of the number"""
    my_tuple: tuple = (k, (v * v))
    return my_tuple
