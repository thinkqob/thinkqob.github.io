#!/usr/bin/env python

# Enter a number and name to num_str
num_str = raw_input('Enter a number: ')

# int the num_str
num_num = int(num_str)

# print a list
non_fac_list = range(1, num_num+1)
print "BEFORE:", repr(non_fac_list)

# name i to 0
i = 0

new_list = []
# while loop
while i < len(non_fac_list):

    # %
    if num_num % non_fac_list[i] != 0:
        new_list.append(non_fac_list[i])

    # self add 1
    i += 1

# print
print "AFTER:", repr(new_list)
