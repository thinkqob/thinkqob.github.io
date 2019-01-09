def collatz(n):
    if n % 2 == 0:
        return n / 2
    return 3 * n + 1


print(collatz(9))


def matchfirst(s1, s2):
    if s1[0] == s2[0]:
        return True
    else:
        return False


print(matchfirst('don', 'lee'))


def simpleDistance(s1, s2):
    if len(s1) == 0:
        return 0
    elif s1[0] != s2[0]:
        return 1 + simpleDistance(s1[1:],s2[1:])
    else:
        return simpleDistance(s1[1:],s2[1:])

print(simpleDistance('dofn','d5ee'))



def factorial(n):
    '''Recursive function for computing the factorial of n'''

    if n == 1:
        return 1
    else:
        result = n*factorial(n - 1)
        return result

print (factorial(7))


def subset(capacity, items):
    if capacity <= 0 or items == []:
        return 0
    elif items[0] > capacity:
        return subset(capacity, items[1:])
    else:
        loseIt = subset(capacity, items[1:])
        useIt = items[0] + subset(capacity - items[0], items[1:])
        return max(loseIt, useIt)

print(subset(4, [1, 2, 3, 4]))



