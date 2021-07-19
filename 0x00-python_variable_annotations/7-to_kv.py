#!/usr/bin/env python3
"""Takes an argument and return a tuple"""


from typing import Union, List, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """return a tuple, v and should be annotated as a float"""
    return (k, v * v)
