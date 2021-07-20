#!/usr/bin/env python3
"""Execute multiple coroutines at the same time with async"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """async routine pawn wait_random n times with the specified max_delay"""
    delay_list: List()[float] = []
    total_delays: List[float] = []

    for i in range(n):
        delay_list.append(wait_random(max_delay))

    for delay_list in asyncio.as_completed(delay_list):
        order = await delay_list
        total_delays.append(order)

    return total_delays
