#!/usr/bin/env python3
"""MRU Caching"""


from base_caching import BaseCaching
from collections import deque


class MRUCache(BaseCaching):
    """Most Recently Used item caching system"""

    def __init__(self):
        """Initialize method"""
        super().__init__()
        self.__stack = deque()

    def put(self, key, item):
        """Discard the most recently used item and print the key discarded"""
        if key and item:
            if key in self.cache_data:
                self.__stack.remove(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                mru_key = self.__stack.popleft()
                del self.cache_data[mru_key]
                print('DISCARD: {}'.format(mru_key))
            self.__stack.appendleft(key)
            self.cache_data[key] = item

    def get(self, key):
        """Must return the value in dict linked to a key"""
        if key in self.cache_data:
            self.__stack.remove(key)
            self.__stack.appendleft(key)
            return self.cache_data[key]
        return None
