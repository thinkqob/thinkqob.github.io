for i in range(21):
    if i % 2 == 0:
        print i,

print "\n"

for j in range(20):
    if j % 2 != 0:
        print j,

print "\n"


def div_test():
    num = raw_input("Can the first num divide by second: ").split()
    if int(num[0]) % int(num[1]) == 0:
        print "True"
    else:
        print "False"

div_test()
