#!/usr/bin/env python3
"""
Task 1 - simple pagination
"""


import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ gets the selection from the csv file """
        assert type(page) == int
        assert type(page_size) == int
        assert page > 0
        assert page_size > 0
        self.dataset()
        selection = index_range(page, page_size)
        datarows = self.__dataset[selection[0]:selection[1]]
        return datarows

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ calls get_page, returns dict dataset """
        datarows = self.get_page(page, page_size)
        prev = None if page == 1 else page - 1
        total = math.ceil(len(self.__dataset) / page_size)
        next = None if page >= total else page + 1

        newdict = {'page_size': page_size, 'page': page, 'data': datarows,
                   'next_page': next, 'prev_page': prev, 'total_pages': total}
        return newdict


def index_range(page, page_size):
    """ returns tuple containing a start index and an end index """
    start = page * page_size - page_size
    end = page * page_size
    return (start, end)
