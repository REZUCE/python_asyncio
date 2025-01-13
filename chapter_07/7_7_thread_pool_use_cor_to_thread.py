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
    urls = ['https://www.example.com' for _ in range(1000)]
    tasks = [loop.run_in_executor(None, functools.partial(get_status_code, url)) for url in urls]
    results = await asyncio.gather(*tasks)
    print(results)
    """
    Здесь мы используем исполнитель по умолчанию, так еще и избавляемся от использования из functools.partial, которая делает функцию без аргументов,
    чтобы можно бы пропихнуть в loop.run_in_executor. А также здесь уходим от get_running_loop()(потому что to_thread и так знает, как обращаться к 
    циклу событий) и run_in_exectur(). 
    """


asyncio.run(main())
