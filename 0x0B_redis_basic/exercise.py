#!/usr/bin/env python3
"""Writing strings to Redis"""


from redis.client import Redis
import redis
import uuid
from typing import Callable, Optional, Union


class Cache:
    """String to Redis"""
    def __init__(self):
        """Instantation method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """takes a data argument, returns a string"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable]) -> str:
        """convert the data back to the desired format"""
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self) -> str:
        """conversion to get str"""


    def get_int(self) -> int:
        """conversion to get int"""
