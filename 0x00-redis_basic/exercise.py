#!/usr/bin/env python3
"""
exercise
"""
from curses import wrapper
import redis
from uuid import uuid4
from typing import Callable, Union
from functools import wraps


def call_history(method: Callable) -> Callable:
    """call history"""

    @wraps(method)
    def wrap(self, *args) -> Union[int, str]:
        """wrapper"""
        key = method.__qualname__
        self._redis.rpush(f"{key}:inputs", str(args))
        output = method(self, *args)
        self._redis.rpush(f"{key}:outputs", output)
        return output

    return wrap


def count_calls(method: Callable) -> Callable:
    """count how many times Cache is called"""
    key = method.__qualname__

    @wraps(method)
    def wrap(self, *args) -> Union[int, str]:
        """counter func"""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args)

    return wrap


def replay(method: Callable) -> None:
    """display history of calls from a function"""
    r = redis.Redis()
    q = method.__qualname__
    input = r.lrange(f"{q}:inputs", 0, -1)
    output = r.lrange(f"{q}:outputs", 0, -1)
    print(f"{q} was called {len(input)} times:")

    for inp, out in zip(input, output):
        print(f"{q}(*{(inp).decode('utf-8')}) -> {(out).decode('utf-8')}")


class Cache():
    """Cache class"""

    def __init__(self):
        """init method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """stores a random key"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None):
        """gets a key"""
        if fn:
            return fn(self._redis.get(key))
        return self._redis.get(key)

    def get_str(self, key: str) -> str:
        """converts string"""
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """converts int"""
        return self.get(key, int)
