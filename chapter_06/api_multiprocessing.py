import time
from multiprocessing import Process


def count(count_to: int) -> int:
    start = time.time()
    counter = 0
    while counter < count_to:
        counter = counter + 1
    end = time.time()
    print(f'Finished counting to {count_to} in {end-start}')
    return counter


# This API do, when easy use. But it will not return the values in the order of completion, how as_completed.
# Join does not return value!!!!!
if __name__ == "__main__":
    start_time = time.time()

    to_one_hundred_million = Process(target=count, args=(100000000,)) # Create process
    to_two_hundred_million = Process(target=count, args=(200000000,)) # A

    to_one_hundred_million.start() # Start process
    to_two_hundred_million.start() # B

    to_one_hundred_million.join() # To wait 
    to_two_hundred_million.join() # C

    end_time = time.time()
    print(f'Completed in {end_time-start_time}')
