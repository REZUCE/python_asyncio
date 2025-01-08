import asyncio

import aiohttp
from aiohttp import ClientSession
from chapter_04 import fetch_status
from util import async_timed


# @async_timed()
# async def main():
#     async with aiohttp.ClientSession() as session:
#         urls = ['http://v-lisitsyn.erlyvideo.ru', 'pidrcom://v-lisitsyn.erlyvideo.ru']
#         requests = [fetch_status(session, url) for url in urls]
#         status_code = await asyncio.gather(*requests, return_exceptions=False)
#         print(status_code)
        
# asyncio.run(main())


# import asyncio

# import aiohttp
# from aiohttp import ClientSession
# from chapter_04 import fetch_status
# from util import async_timed


# @async_timed()
# async def main():
#     async with aiohttp.ClientSession() as session:
#         fetchers = [
#             fetch_status(session, 'http://v-lisitsyn.erlyvideo.ru', 1),
#             fetch_status(session, 'http://v-lisitsyn.erlyvideo.ru', 10),
#             fetch_status(session, 'http://v-lisitsyn.erlyvideo.ru', 10)
#         ]
#         for finished_task in asyncio.as_completed(fetchers):
#             print(await finished_task)

# asyncio.run(main())

@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        fetchers = [
            fetch_status(session, 'http://v-lisitsyn.erlyvideo.ru', 1),
            fetch_status(session, 'http://v-lisitsyn.erlyvideo.ru', 10),
            fetch_status(session, 'http://v-lisitsyn.erlyvideo.ru', 10)
        ]
        for done_task in asyncio.as_completed(fetchers, timeout=2):
            try:
                result = await done_task
                print(result)
            except asyncio.TimeoutError:
                print('Произошел тайм-аут!')
        for task in asyncio.tasks.all_tasks():
            print(task)

asyncio.run(main())
