from threading import RLock, Thread
from typing import List

list_lock = RLock()


def sum_list(int_list: List[int]) -> int:
    print('Waiting to acquire lock...')
    with list_lock:
        print('Acquired lock.')
        if len(int_list) == 0:
            print('Finished summing.')
            return 0
        else:
            head, *tail = int_list
            print('Summing rest of list.')
            return head + sum_list(tail)

    """
    Здесь используется Реентерабельная блокировка, которая позволяет одному потоку захватить то, что уже захватил ранее.
    """

thread = Thread(target=sum_list, args=([1, 2, 3, 4],))
thread.start()
thread.join()
