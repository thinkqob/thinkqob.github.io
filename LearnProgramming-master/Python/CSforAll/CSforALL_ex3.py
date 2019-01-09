import sys
sys.setrecursionlimit(10000)


def divisors(n, low, high):
    """Return true if n has a divisor in the range from low and high.
        Otherwise return false"""
    if low > high:
        return False
    elif n % low == 0:  # is divisble by low?
        return True
    else:
        return divisors(n, low + 1, high)

print divisors(7, 2, 6)


def isprime(n):
    """For any n greater than or equal to 2,
        Returns True if n is prime. False if not."""
    if divisors(n, 2, n - 1):
        return False
    else:
        return True

print isprime(13)


def listprime(n, limit):
    """Return a list of prime between n and limit."""
    if n == limit:
        return []
    elif isprime(n):
        return [n] + listprime(n + 1, limit)
    else:
        return listprime(n + 1, limit)

print listprime(2, 100)


def isnotdivisbleby2(n):
    """Return True if n is not divisble by 2,
    Else return False"""
    return n % 2 != 0

print isnotdivisbleby2(19)

print filter(isnotdivisbleby2, range(2, 100))


def sift(toremove, numlist):
    """Takes a number, toremove, a list of numbers, numlist.
        Return a list of numbers in numlist that a not multiples of toremove."""
    return filter(lambda x: x % toremove != 0, numlist)


def primesieve(numberlist):
    """Return the list of all primes in numberlist using a prime sieve algorithm."""
    if numberlist == []:
        return []
    else:
        prime = numberlist[0]
        return [prime] + primesieve(sift(prime, numberlist[1:]))


print primesieve(range(2, 9000))




