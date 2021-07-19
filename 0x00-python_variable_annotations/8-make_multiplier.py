#!/usr/bin/env python3
"""type-annotated function make_multiplier"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return another function"""
    def mult(num: float):
        """multiplies a float by multiplier"""
        return num * multiplier
    return mult
