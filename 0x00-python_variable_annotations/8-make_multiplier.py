#!/usr/bin/env python3
"""type-annotated function make_multiplier"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float],float]:
    def mult (num: float):
        return num * multiplier
    return mult
