import functools
import requests
import asyncio
from concurrent.futures import ThreadPoolExecutor
from threading import Lock
from util import async_timed

counter_lock = Lock()
counter: int = 0


def get_status_code(url: str) -> int:
    global counter
    response = requests.get(url)
    with counter_lock:
        counter = counter + 1
    return response.status_code


async def reporter(request_count: int):
    while counter < request_count:
        print(f'Finished {counter}/{request_count} requests')
        await asyncio.sleep(.5)


@async_timed()
async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        request_count = 200
        urls = ['https://www.example.com' for _ in range(request_count)]
        reporter_task = asyncio.create_task(reporter(request_count))
        tasks = [loop.run_in_executor(pool, functools.partial(get_status_code, url)) for url in urls]
        results = await asyncio.gather(*tasks)
        await reporter_task
        print(results)

    """
    Важно помнить, что процессы не разделяют память и нужно было создавать и правильно инициализировать специальные объекты разделяемой памяти.
    Но потоки видят памамять создавшего их процесса. Это упрощает дело, но мы теперь не сможем использовать Value, потому что там встроенные 
    блокировки. Придется создать их самих, для этого есть Lock из модуля threading, отличающиеся от реализации в модуле multiprocessing. Нужно
    лишь окружить кретические секции с поимощью Lock, используя его методы acquire и release, либо использовать контекстный менеджер на этот блок. 
    """

asyncio.run(main())
