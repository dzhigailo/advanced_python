from threading import Event
from threading import Thread


def print_even_numbers(even_ev, odd_ev):
    for i in range(0, 101, 2):
        odd_ev.wait()
        odd_ev.clear()
        print('Even thread: ', i)
        even_ev.set()


def print_odd_numbers(even_ev, odd_ev):
    for i in range(1, 100, 2):
        even_ev.wait()
        even_ev.clear()
        print('Odd thread:  ', i)
        odd_ev.set()


if __name__ == '__main__':
    even_ev = Event()
    odd_ev = Event()

    t1 = Thread(target=print_even_numbers, args=(even_ev, odd_ev))
    t2 = Thread(target=print_odd_numbers, args=(even_ev, odd_ev))

    t1.start()
    t2.start()
    odd_ev.set()
