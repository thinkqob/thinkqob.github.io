dollar = float(raw_input("Give me some change:"))

quarter = int(dollar // 0.25)
ten = int((dollar - (quarter * 0.25)) // 0.10)
five = int((dollar - (quarter * 0.25) - (ten * 0.10)) // 0.05)
one = int((dollar - (quarter * 0.25) - (ten * 0.10) - (five * 0.05)) // 0.01)

print "You have %s quarter, %s ten, %s five, and %s one," % (quarter, ten, five, one),
print "total have %s coins." % (quarter + ten + five + one)

"""
def get_cent_count(num):
    cent_count_arr = []
    cents = [25, 10, 5, 1]

    left = num
    i = 0
    while left != 0:
        cent_count_arr.append(left // cents[i])
        left = left % cents[i]
        i += 1

    return cent_count_arr

print get_cent_count(76)
print get_cent_count(123)
print get_cent_count(88)
"""