def fibonacci(num):
    l = [1, 1]
    i = 0
    while i < num:
        l.append(int(l[i]) + int(l[i + 1]))
        i += 1
    print l[num - 1]

fibonacci(9)
