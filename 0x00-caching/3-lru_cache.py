#!/usr/bin/env python3
""" Task 3 - lru cache """


from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ lru cache """

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
        if len(self.cache_data) > self.MAX_ITEMS:
            popped = self.cache_data.popitem(last=False)
            print("DISCARD: {}".format(popped[0]))

    def get(self, key):
        """ retrieves values """
        if key is None:
            return None
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        else:
            return None
