def int_to_ip():
    nums = raw_input("Enter you IP num: ")
    nums_list = []
    for i in range(0, 12, 3):
        nums_list.append(nums[i:i + 3])
    print ".".join(nums_list)

int_to_ip()


def ip_to_int():
    ip = raw_input("Enter you IP num: ").split('.')
    print "".join(ip)

ip_to_int()
