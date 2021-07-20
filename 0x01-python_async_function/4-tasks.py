#!/usr/bin/env python3
"""wait_n and task_wait_random"""


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """wait_n and task_wait_random being called"""
    delay_list: List()[float] = []
    total_delays: List[float] = []

    for i in range(n):
        delay_list.append(task_wait_random(max_delay))

    for delay_list in asyncio.as_completed(delay_list):
        order = await delay_list
        total_delays.append(order)

    return total_delays
