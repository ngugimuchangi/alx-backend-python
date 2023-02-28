#!/usr/bin/env python3
""" Async comprehension module """
from typing import List


async def async_comprehension() -> List[float]:
    """ Collects 10 random numbers using async comprehension
        over async_generator
    """
    generator = __import__('0-async_generator').async_generator
    return [i async for i in generator()]
