import asyncio
from asyncio.events import AbstractEventLoop
from concurrent.futures import ProcessPoolExecutor
from functools import partial
from typing import List


def countdown(count_from: int) -> int:
    counter = 0
    while counter < count_from:
        counter = counter + 1
    return counter


async def main():
    with ProcessPoolExecutor() as process_pool: # A 
        loop: AbstractEventLoop = asyncio.get_running_loop() # B, because run_in_executor child class AbstractEventLoop.
        nums = [1, 3, 5, 22, 100000000]
        calls: List[partial[int]] = [partial(countdown, num) for num in nums] # List func pool process. pratical - func without args, but with fixed arguments. Because run_in_executor not accepts func with args.
        
        call_coros = []

        for call in calls:
            call_coros.append(loop.run_in_executor(process_pool, call)) # run_in_executor - принимает выполняемый объект(call) и исполнитель(process_pool). Строим список из объектов, результат которых можно оджидать через await.

        results = await asyncio.gather(*call_coros) # Results after finish all coros. Also may use as_completed, to solve the problem with child process which take longer to complete and they block it result other process .(Также мы можес использовать as_completed, чтобы решить проблему с дочерними процессами которые выполняются долго и блокируют результат других процессов.)
        print(results)

        for result in results:
            print(result)


if __name__ == "__main__":
    asyncio.run(main())
