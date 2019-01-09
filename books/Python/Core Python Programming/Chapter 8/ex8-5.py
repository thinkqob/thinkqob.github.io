def get_factors(num):
    half = int(num / 2)
    i = 1
    l = []
    while i < half:
        if num % i == 0:
            l.append(i)
        i += 1
    print l

get_factors(26)
