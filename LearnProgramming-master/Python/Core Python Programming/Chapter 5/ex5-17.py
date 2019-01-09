import random
import math


def random_list():
    random_n = random.randint(2, 101)
    list_n = []
    max_n = math.pow(2, 31)
    for i in range(random_n):
        list_n.append(random.randrange(max_n))

    list_n.sort()
    print list_n

random_list()
