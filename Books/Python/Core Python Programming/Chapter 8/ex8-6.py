import math

def is_prime(num):
    count = int(math.sqrt(num))
    while count > 1:
        if num % count == 0:
            return False
        count -= 1
    else:
        return True


def get_factors(num):
    return [i for i in range(1, num + 1) if num % i == 0]

def prime_factor(num):
    print [ i for i in get_factors(num) if is_prime(i)]


prime_factor(120)
