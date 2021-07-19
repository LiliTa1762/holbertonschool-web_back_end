#!/usr/bin/env python3
"""type-annotated function sum_mixed_list"""


from typing import Union, List

nums = Union[int, float]


def sum_mixed_list(mxd_lst: List[nums]) -> float:
    """Using Union to mxd list, return a float"""
    return sum(mxd_lst)
