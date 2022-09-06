#!/usr/bin/env python3
""" Task 2 - lifo cache """


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ lifo cache """

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.last = []

    def put(self, key, item):
        """ adds item """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        self.last.append(key)
        if len(self.cache_data) > self.MAX_ITEMS:
            self.cache_data.pop(self.last[len(self.last) - 2])
            print("DISCARD: {}".format(self.last[len(self.last) - 2]))

    def get(self, key):
        """ retrieves values """
        if key is None:
            return None
        if key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
