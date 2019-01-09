import math

def is_prime(num):
    count = int(math.sqrt(num))
    while count > 1:
        if num % count == 0:
            return False
        count -= 1
    else:
        return True

print is_prime(9)
print is_prime(3)
print is_prime(17)
