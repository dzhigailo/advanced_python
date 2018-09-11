import multiprocessing


def print_even_numbers(lock_even, lock_odd):
    for i in range(0, 101, 2):
        lock_odd.acquire()
        print('Even process: ', i)
        lock_even.release()


def print_odd_numbers(lock_even, lock_odd):
    for i in range(1, 100, 2):
        lock_even.acquire()
        print('Odd process:  ', i)
        lock_odd.release()


if __name__ == '__main__':
    lock_even = multiprocessing.Lock()
    lock_even.acquire()
    lock_odd = multiprocessing.Lock()

    p1 = multiprocessing.Process(target=print_even_numbers,
                                 args=(lock_even, lock_odd))
    p2 = multiprocessing.Process(target=print_odd_numbers,
                                 args=(lock_even, lock_odd))

    p1.start()
    p2.start()
