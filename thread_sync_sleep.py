from threading import Thread
import time

TIME_SLEEP = 0.05


def print_even_numbers():
    for i in range(0, 101, 2):
        print('Even thread: ', i)
        time.sleep(TIME_SLEEP)


def print_odd_numbers():
    for i in range(1, 100, 2):
        print('Odd thread:  ', i)
        time.sleep(TIME_SLEEP)


if __name__ == '__main__':
    t1 = Thread(target=print_even_numbers)
    t2 = Thread(target=print_odd_numbers)

    t1.start()
    t2.start()
