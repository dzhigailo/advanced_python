from threading import Condition
from threading import Thread


def print_even_numbers(even_cond, odd_cond):
    for i in range(0, 101, 2):
        with odd_cond:
            odd_cond.wait()
            print('Even thread: ', i)
        with even_cond:
            even_cond.notify_all()


def print_odd_numbers(even_cond, odd_cond):
    for i in range(1, 100, 2):
        with even_cond:
            even_cond.wait()
            print('Odd thread:  ', i)
        with odd_cond:
            odd_cond.notify_all()


if __name__ == '__main__':
    even_cond = Condition()
    odd_cond = Condition()

    t1 = Thread(target=print_even_numbers, args=(even_cond, odd_cond))
    t2 = Thread(target=print_odd_numbers, args=(even_cond, odd_cond))

    t1.start()
    t2.start()

    with odd_cond:
        odd_cond.notify_all()
