import asyncio
from asyncio import CancelledError
from util import delay


async def main():
    task = asyncio.create_task(delay(10))
    
    try:
        result = await asyncio.wait_for(asyncio.shield(task), 5)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print("Задача выполняется более 5 с, скоро она закончится!")
        result = await task
        print(result)

asyncio.run(main())
w
