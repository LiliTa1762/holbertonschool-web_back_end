#!/usr/bin/env python3
"""Tasks regular"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random



def task_wait_random(max_delay: int) -> asyncio.Task:
    """returns a asyncio.Task"""
    tasks = asyncio.create_task(wait_random(max_delay))
    return tasks
