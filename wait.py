# import asyncio
# import aiohttp
# from util import async_timed
# from chapter_04 import fetch_status


# @async_timed()
# async def main():
#     async with aiohttp.ClientSession() as session:
#         fetchers = [
#             asyncio.create_task(fetch_status(session, 'http://v-lisitsyn.erlyvideo.ru')), 
#             asyncio.create_task(fetch_status(session, 'http://v-lisitsyn.erlyvideo.ru'))
#         ]
#         done, pending = await asyncio.wait(fetchers)
#         print(f"Число завершившихся задача: {len(done)}")
#         print(f"Число ожидающих задача: {len(pending)}")

#         for done_task in done:
#             result = await done_task
#             print(result)

# asyncio.run(main())


# Обработка исключений
# import asyncio
# import aiohttp
# from util import async_timed
# import logging
# from chapter_04 import fetch_status


# @async_timed()
# async def main():
#     async with aiohttp.ClientSession() as session:
#         good_request = fetch_status(session, 'https://www.example.com')
#         bad_request = fetch_status(session, 'python://bad')

#         fetchers = [asyncio.create_task(good_request),
#                     asyncio.create_task(bad_request)]

#         done, pending = await asyncio.wait(fetchers)

#         print(f'Done task count: {len(done)}')
#         print(f'Pending task count: {len(pending)}')

#         for done_task in done:
#             # result = await done_task will throw an exception
#             if done_task.exception() is None:
#                 print(done_task.result())
#             else:
#                 logging.error("Request got an exception",
#                               exc_info=done_task.exception())


# asyncio.run(main())


# Если в одном из запросов возникло ислючение и мы хотим снять другие.

# import aiohttp
# import asyncio
# import logging
# from chapter_04 import fetch_status
# from util import async_timed


# @async_timed()
# async def main():
#     async with aiohttp.ClientSession() as session:
#         fetchers = \
#             [asyncio.create_task(fetch_status(session, 'python://bad.com')),
#             asyncio.create_task(fetch_status(session, 'https://www.example.com', delay=3)),
#             asyncio.create_task(fetch_status(session, 'https://www.example.com', delay=3))]

#         done, pending = await asyncio.wait(fetchers, return_when=asyncio.FIRST_EXCEPTION)

#         print(f'Done task count: {len(done)}')
#         print(f'Pending task count: {len(pending)}')

#         for done_task in done:
#             if done_task.exception() is None:
#                 print(done_task.result())
#             else:
#                 logging.error("Request got an exception",
#                               exc_info=done_task.exception())

#         for pending_task in pending:
#             pending_task.cancel()


# asyncio.run(main())





# Обработка всехрезультатов по мере поступления
# Здесь не все успеют выполнится за одну итерацию.
# import asyncio
# import aiohttp
# from util import async_timed
# from chapter_04 import fetch_status


# @async_timed()
# async def main():
#     async with aiohttp.ClientSession() as session:
#         url = 'https://www.example.com'
#         fetchers = [asyncio.create_task(fetch_status(session, url)),
#                     asyncio.create_task(fetch_status(session, url)),
#                     asyncio.create_task(fetch_status(session, url))]

#         done, pending = await asyncio.wait(fetchers, return_when=asyncio.FIRST_COMPLETED)

#         print(f'Done task count: {len(done)}')
#         print(f'Pending task count: {len(pending)}')

#         for done_task in done:
#             print(await done_task)


# asyncio.run(main())


import asyncio

import aiohttp

from chapter_04 import fetch_status
from util import async_timed


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        url = 'https://www.example.com'
        pending = [asyncio.create_task(fetch_status(session, url)),
                   asyncio.create_task(fetch_status(session, url)),
                   asyncio.create_task(fetch_status(session, url))]

        while pending: # выполняется пока количество не выполненых не закончится
            done, pending = await asyncio.wait(pending, return_when=asyncio.FIRST_COMPLETED)

            print(f'Done task count: {len(done)}')
            print(f'Pending task count: {len(pending)}')

            for done_task in done:
                print(await done_task)

asyncio.run(main())
