import asyncio
from util import async_timed, delay

@async_timed()
async def main():
    delay_task = [3, 3, 3]
    [await asyncio.create_task(delay(seconds)) for seconds in delay_task]

asyncio.run(main())
