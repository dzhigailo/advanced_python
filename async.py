import concurrent.futures
from tools import is_prime


def executor_func(start, end):
    input_range = range(start, end)

    with concurrent.futures.ProcessPoolExecutor() as executor:
        result = 0
        for number, prime in zip(input_range,
                                 executor.map(is_prime, input_range)):
            if prime:
                result += number

    print(result)


def main():
    executor_func(20, 9999)


if __name__ == '__main__':
    main()
