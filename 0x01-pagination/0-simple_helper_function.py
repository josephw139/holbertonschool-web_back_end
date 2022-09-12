#!/usr/bin/env python3
"""
Task 0 - simple helper function
"""


def index_range(page, page_size):
    """ returns tuple containing a start index and an end index """
    start = page * page_size - page_size
    end = page * page_size
    return (start, end)
