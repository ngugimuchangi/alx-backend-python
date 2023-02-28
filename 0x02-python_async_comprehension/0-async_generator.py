#!/usr/bin/env python3
""" Asynchronous generator module """
import asyncio
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ Asynchronous generator function
        Args: none
        Return: Generator object that yields a random number
                between 0 and 10
    """
    for _ in range(10):
        yield uniform(0, 10)
        await asyncio.sleep(1)
