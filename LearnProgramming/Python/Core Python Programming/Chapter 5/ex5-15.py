def gcd(num1, num2):
    if num2 == 0:
        return num1
    else:
        return gcd(num2, num1 % num2)


def lcm(num1, num2):
    return num1 * num2 / gcd(num1, num2)


print gcd(8, 4)
print lcm(8, 4)
