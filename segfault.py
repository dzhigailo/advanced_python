import sys


# Checked on Python3.6.2

def segfault(value):
    print(value)

    sys.setrecursionlimit(sys.getrecursionlimit() + 1)

    segfault(value + 1)

if __name__ == '__main__':
    segfault(1)
