from multiprocessing import Pool
import time


def say_hello2(name: str) -> str:
    time.sleep(10)
    return f'Привет, {name}'

def say_hello(name: str) -> str:
    time.sleep(2)
    return f'Привет, {name}'

if __name__ == "__main__":
    start_time = time.time()
    with Pool() as procces_pool: # Create pool process. As many as cores by machine. multiprocessing cpu_count(), you can also in Pool.
        hi_jeff = procces_pool.apply_async(say_hello, args=('Jeff',)) # Apply say_hello with arg Jeff, in a separate process
        hi_John = procces_pool.apply_async(say_hello2, args=('John',))
        print(hi_jeff.get()) # Get result in async_apply <multiprocessing.pool.ApplyResult object at ....>
        print(hi_John.get()) # But if hi_jeff apply 10s, but hi_john 1 s, then we still need to something similar to as_completed from asyncio or rotate hi_john and hi_jeff 
    end_time = time.time()
    print(f'Время выполнения +- {end_time - start_time}')
