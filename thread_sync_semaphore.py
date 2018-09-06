from threading import Semaphore
from threading import Thread


def print_even_numbers(sem_even, sem_odd):
    for i in range(0, 101, 2):
        sem_even.acquire()
        print('Even thread: ', i)
        sem_odd.release()


def print_odd_numbers(sem_even, sem_odd):
    for i in range(1, 100, 2):
        sem_odd.acquire()
        print('Odd thread:  ', i)
        sem_even.release()


if __name__ == '__main__':
    sem_even = Semaphore(1)
    sem_odd = Semaphore(0)

    even_thread = Thread(target=print_even_numbers, args=(sem_even, sem_odd))
    odd_thread = Thread(target=print_odd_numbers, args=(sem_even, sem_odd))

    even_thread.start()
    odd_thread.start()
