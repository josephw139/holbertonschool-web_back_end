#!/usr/bin/env python3
""" Task 1 - fifo cache """


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ fifo cache """

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()

    def put(self, key, item):
        """ caches items """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            first_key = list(self.cache_data.keys())[0]
            self.cache_data.pop(first_key)
            print("DISCARD: {}".format(first_key))

    def get(self, key):
        """ retrieves values """
        if key is None:
            return None
        if key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
