def get_factors(num):
    return [i for i in range(1, num) if num % i == 0]


def is_perfect(num):
    if num == sum(get_factors(num)):
        return 1
    else:
        return 0


print [i for i in xrange(10000) if is_perfect(i) == 1]
