from threading import Lock, Thread
import time

lock_a = Lock()
lock_b = Lock()


def a():
    with lock_a: #A
        print('Acquired lock a from method a!')
        time.sleep(1) #B
        with lock_b: #C
            print('Acquired both locks from method a!')


def b():
    with lock_b: #D
        print('Acquired lock b from method b!')
        with lock_a: #E
            print('Acquired both locks from method b!')

    """
    Последовательность возникновения deadlock:

    1. thread_1 (метод A):
    - Получает lock_a
    - Засыпает на 1 секунду (time.sleep(1))

    2. thread_2 (метод B) в это время:
    - Получает lock_b, пока thread_1 спит
    
    3. thread_1 просыпается:
    - Пытается получить lock_b
    - Не может получить, так как lock_b занят thread_2
    - Блокируется в ожидании

    4. thread_2 продолжает:
    - Пытается получить lock_a
    - Не может получить, так как lock_a занят thread_1
    - Блокируется в ожидании

    Результат: Возникает deadlock (взаимоблокировка), так как:
    - thread_1 держит lock_a и ждёт lock_b
    - thread_2 держит lock_b и ждёт lock_a
    """

thread_1 = Thread(target=a)
thread_2 = Thread(target=b)
thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()
