import asyncio
from util import async_timed, delay

async def main():
    result = await asyncio.gather(delay(3), delay(1))
    print(result)

asyncio.run(main())
