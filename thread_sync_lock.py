from threading import Lock
from threading import Thread


def print_even_numbers(lock_even, lock_odd):
    for i in range(0, 101, 2):
        lock_odd.acquire()
        print('Even thread: ', i)
        lock_even.release()


def print_odd_numbers(lock_even, lock_odd):
    for i in range(1, 100, 2):
        lock_even.acquire()
        print('Odd thread:  ', i)
        lock_odd.release()


if __name__ == '__main__':
    lock_even = Lock()
    lock_even.acquire()
    lock_odd = Lock()

    t1 = Thread(target=print_even_numbers, args=(lock_even, lock_odd))
    t2 = Thread(target=print_odd_numbers, args=(lock_even, lock_odd))

    t1.start()
    t2.start()
