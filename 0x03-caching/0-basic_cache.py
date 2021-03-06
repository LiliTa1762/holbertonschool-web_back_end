#!/usr/bin/env python3
"""Basic dictionary"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """It is a caching system"""

    def put(self, key, item):
        """assign to the dict the item value for the key"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Must return the value in dict linked to a key"""
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
