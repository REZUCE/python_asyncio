import asyncio

import aiohttp
from aiohttp import ClientSession
from chapter_04 import fetch_status
from util import async_timed


@async_timed()
async def main():
    # session_timeout = aiohttp.ClientTimeout(total=1, connect=1)
    # async with aiohttp.ClientSession(timeout=session_timeout) as session:
    async with aiohttp.ClientSession() as session:
        urls = ['http://v-lisitsyn.erlyvideo.ru' for _ in range(1000)]
        requests = [fetch_status(session, url) for url in urls]
        status_code = await asyncio.gather(*requests)
        # status_code = [await fetch_status(session, url) for url in urls]
        print(status_code)
        
asyncio.run(main())
