
def divisors(n, low, high):
    """Return True if n has a divisor in the range from low to high, Otherwisr return false."""
    if low > high:
        return False
    elif n % low == 0:
        return True
    else:
        return divisors(n, low + 1, high)


print divisors(5, 2, 4)


def isprime(n):
    """ for any greater than or equal to 2 , return True if n is prime. False if not """
    if divisors(n, 2, n-1):
        return False
    else:
        return True

print isprime(5)


def listprime(n, limit):
    if n == limit:
        return []
    elif isprime(n):
        return [n] + listprime(n + 1, limit)
    else:
        return listprime(n + 1, limit)

print listprime(2, 8)


def incrementlist(numberlist):
    """Take a list of numbers as an argument and returns a new list with each number incremented by one"""

    if numberlist == []:
        return []
    else:
        newfirst = numberlist[0] + 1
        incrementedlist = incrementlist(numberlist[1:])
        return [newfirst] + incrementedlist

print(incrementlist(range(0, 3)))


