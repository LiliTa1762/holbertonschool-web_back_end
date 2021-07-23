#!/usr/bin/env python3
"""LIFO Caching"""


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """caching system"""

    def __init__(self):
        """Initialize method"""
        super().__init__()
        self.discard_key = ''

    def put(self, key, item):
        """Discard the last item and print the key discarded"""
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                print('DISCARD: {}'.format(self.discard_key))
                self.cache_data.pop(self.discard_key)
            self.discard_key = key

    def get(self, key):
        """Must return the value in dict linked to a key"""
        if key is None or self.cache_data.get(key) is None:
            return None
        if key in self.cache_data:
            return self.cache_data.get(key)
