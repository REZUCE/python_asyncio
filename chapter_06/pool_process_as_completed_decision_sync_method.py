from multiprocessing import Pool

def say_hello(name: str) -> str:
    return f'Привет, {name}'

if __name__ == "__main__":
    with Pool() as procces_pool: # Create pool process. As many as cores by machine. multiprocessing cpu_count(), you can also in Pool.
        hi_jeff = procces_pool.apply(say_hello, args=('Jeff',)) # Apply say_hello with arg Jeff, in a separate process
        hi_John = procces_pool.apply(say_hello, args=('John',)) # You can return value from apply. apply synchronous method, but there is async_apply.
        print(hi_jeff)
        print(hi_John)
