#!/usr/bin/env python3
""" Async IO basics """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Coroutine that waits for random number of seconds
        less than max_delay and return the wait period
        Args:
            max_delay: maximum delay time to await
                       coroutine
        Return: delay time for the coroutine
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
