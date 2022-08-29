#!/usr/bin/env python3
from typing import Iterable, Sequence, List, Tuple
""" Task 9 - annotate and return values of appropriate types
"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ annotations """
    return [(i, len(i)) for i in lst]
