def factorial(num):
    result = 1
    while num >= 1:
        result *= num
        num -= 1
    return result


print factorial(9)
