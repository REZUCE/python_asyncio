# import asyncio

# import aiohttp
# from aiohttp import ClientSession
# from chapter_04 import fetch_status
# from util import async_timed


# @async_timed()
# async def main():
#     async with aiohttp.ClientSession() as session:
#         urls = ['http://v-lisitsyn.erlyvideo.ru', 'pidrcom://v-lisitsyn.erlyvideo.ru']
#         requests = [fetch_status(session, url) for url in urls]
#         status_code = await asyncio.gather(*requests, return_exceptions=False)
#         print(status_code)
        
# asyncio.run(main())


import asyncio

import aiohttp
from aiohttp import ClientSession
from chapter_04 import fetch_status
from util import async_timed


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        urls = ['http://v-lisitsyn.erlyvideo.ru', 'pidrcom://v-lisitsyn.erlyvideo.ru']
        requests = [fetch_status(session, url) for url in urls]
        status_code = await asyncio.gather(*requests, return_exceptions=True)
        exceptions = [res for res in status_code if isinstance(res, Exception)]
        succes_result = [res for res in status_code if not isinstance(res, Exception)]
        print(f'Все результаты: {status_code}')
        print(f'Результаты с исключением: {exceptions}')
        print(f'Результаты успешные: {exceptions}')
        
asyncio.run(main())
