def is_prime(number):
    if number == 2 or number == 3:
        return True
    if number < 2 or number % 2 == 0:
        return False
    if number < 9:
        return True
    if number % 3 == 0:
        return False
    r = int(number ** 0.5)
    f = 5
    while f <= r:
        if number % f == 0:
            return False
        if number % (f + 2) == 0:
            return False
        f += 6
    return True
