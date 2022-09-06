#!/usr/bin/env python3
""" Task 0 - Basic dictionary
"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ Dictionary for caching"""

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()

    def put(self, key, item):
        """ caches values """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ retrieves values """
        if key is None:
            return None
        if key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
