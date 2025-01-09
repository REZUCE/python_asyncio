import time
import requests
from concurrent.futures import ThreadPoolExecutor

def get_status_code(url: str) -> int:
    response = requests.get(url)
    return response.status_code

start = time.time()

with ThreadPoolExecutor() as thread_pool: # Может быть медленнее чем через aiohttp, потому что ограничение в 32 потока, но можно задать внутри ThreadPoolExecutor(max_workers=1000)- но так все равно медленне, 
    # из-за накладных расходов в OS.
    urls = ['https://vk.com/' for _ in range(1000)]
    results = thread_pool.map(get_status_code, urls)
    for result in results:
        print(result)

end = time.time()

print(f'Выполнение запросов завершено за {end - start:.4f} c')

