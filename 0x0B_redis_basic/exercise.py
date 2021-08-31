#!/usr/bin/env python3
"""Writing strings to Redis"""


from redis.client import Redis
import redis
import uuid


class Cache:
    """String to Redis"""
    def __init__(self):
        """Instantation method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: [str, bytes, int, float]) -> str:
        """takes a data argument, returns a string"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
