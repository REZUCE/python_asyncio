import functools
import requests
import asyncio
from concurrent.futures import ThreadPoolExecutor
from util import async_timed


def get_status_code(url: str) -> int:
    response = requests.get(url)
    return response.status_code


@async_timed()
async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        urls = ['https://www.example.com' for _ in range(1000)]
        tasks = [loop.run_in_executor(pool, functools.partial(get_status_code, url)) for url in urls]
        results = await asyncio.gather(*tasks)
        print(results)
    """
    Этот подход не дает никакого выиграша по сравнению с pool thread без asyncio, но пока ждем await asyncio.gather, то мы можем выполнять другой код. 
    run_in_executor - вызывает метод submit исполнителя пула потоков. Это ставит все задачи в очередь. Затем рабочие потоки в поле могут выбирать задачи из очереди и выполнять их до завершения.
    """


asyncio.run(main())
