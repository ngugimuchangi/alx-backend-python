# 0x01. Python - Async

## About
- Concurrency
- Parallelism
- Async IO paradigm
- `asyncio` module

## Tasks
0. Asynchronous coroutine that takes in an integer argument (`max_delay`, with a default value of 10) named `wait_random` that waits for a random delay between 0 and `max_delay` (included and float value) seconds and eventually returns it.
    * [0-basic_async_syntax.py](0-basic_async_syntax.py)
1. Asynchronous coroutine, `wait_n`, that takes in 2 int arguments (in this order): `n` and `max_delay`. `wait_n` spawns `wait_random` `n` times with the specified `max_delay` and return  list of all the delays (float values) in ascending order.
    * [1-concurrent_coroutines.py](1-concurrent_coroutines.py)
2. Function `measure_time` with integers `n` and `max_delay` as arguments that measures the total execution time for `wait_n(n, max_delay)`, and returns `total_time / n`. Your function should return a fl
    * [2-measure_runtime.py](2-measure_runtime.py)
3. Function `task_wait_random` that takes an integer `max_delay` and returns a `asyncio.Task` based on  coroutine `wait_random`.
    * [3-tasks.py](3-tasks.py)
4. Function `task_wait_n`: an altered form of function `wait_n` that calls function `task_wait_random` instead of `wait_random`
    * [4-tasks.py](4-tasks.py)
