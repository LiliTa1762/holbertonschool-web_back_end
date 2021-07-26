#!/usr/bin/env python3
"""LRU Caching"""


from base_caching import BaseCaching
from collections import deque


class LRUCache(BaseCaching):
    """Least Recently Used caching system"""

    def __init__(self):
        """Initialize method"""
        super().__init__()
        self.__deque = deque()

    def put(self, key, item):
        """Discard the least recently used and print the key discarded"""
        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                lru_key = self.__deque.popleft()
                del self.cache_data[lru_key]
                print('DISCARD: {}'.format(lru_key))
            elif key in self.cache_data:
                self.__deque.remove(key)

            self.__deque.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Must return the value in dict linked to a key"""
        if key in self.cache_data:
            self.__deque.remove(key)
            self.__deque.append(key)
            return self.cache_data[key]
        return None
