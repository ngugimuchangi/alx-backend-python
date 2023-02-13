#!/usr/bin/env python3
""" Creating asyncio tasks """
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ Function to create asyncio tasks
        Args:
            max_delay: maximum delay time for the returned
                       coroutine
        Return: asyncio.Task
    """
    return asyncio.create_task(wait_random(max_delay))
