#!/usr/bin/env python3
"""return values with the appropriate types"""

from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """values with the appropriate types"""
    return [(i, len(i)) for i in lst]
