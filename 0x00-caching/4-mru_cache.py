#!/usr/bin/env python3
""" Task 4 - mru cache """


BaseCaching = __import__('base_caching').BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """ mru cache """

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ adds item """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        self.cache_data.move_to_end(key)
        length = len(self.cache_data)
        if length > self.MAX_ITEMS:
            keys = list(self.cache_data.keys())
            self.cache_data.pop(keys[length - 2])
            print("DISCARD: {}".format(keys[length - 2]))

    def get(self, key):
        """ retrieves values """
        if key is None:
            return None
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        else:
            return None
