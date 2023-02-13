#!/usr/bin/env python3
""" Measuring time take for parallel execution
    of coroutines
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Function that executes multiple coroutines at
        the same time and measure the time taken to
        complete execution of all coroutines
        Args:
            n: iterations for coroutine
            max_delay: maximum delay time to await
                       coroutine
        Return: time taken to execute all coroutines
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    return (end_time - start_time)/n
