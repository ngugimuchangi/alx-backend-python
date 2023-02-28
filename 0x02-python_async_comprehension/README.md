# 0x02. Python - Async Comprehension
## About
- Asynchronous generator and comprehensions
## Tasks
0. Coroutine `async_generator` that loops 10 times, each time asynchronously waiting 1 second, then yields a random number between 0 and 10
    * [0-async_generator.py](0-async_generator.py)
1. Coroutine `async_comprehension` that collects 10 random numbers using async comprehension over `async_generator` (from task 0), then return the 10 random numbers
    * [1-async_comprehension.py](1-async_comprehension.py)
2. Coroutine `measure_runtime` that executes `async_comprehension` coroutine (from task 2)four times concurrently, then returns the total execution time for all four coroutines.
    * [2-measure_runtime.py](2-measure_runtime.py)
