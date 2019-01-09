def order():
    num_list = raw_input('Enter some numbers: ').split()
    num_list.sort()
    new_list = sorted(num_list, reverse=True)
    print num_list, new_list

order()
