#!/usr/bin/env python3
"""FIFO caching"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO caching"""

    def __init__(self):
        """Initialize method"""
        super().__init__()

    def put(self, key, item):
        """assign to the dict the item for the key"""
        if key and item:
            self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            discard = next(iter(self.cache_data))
            print('DISCARD: {}'.format(str(discard)))
            del self.cache_data[next(iter(self.cache_data))]

    def get(self, key):
        """Must return the value in dict linked to a key"""
        if key is None or self.cache_data.get(key) is None:
            return None
        if key in self.cache_data:
            return self.cache_data.get(key)
