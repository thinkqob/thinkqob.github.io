"""
#2-2
s = 1 + 2 * 4
print s


#2-4
name = raw_input("Please enter you login name:")
print "Your login name is %s \n" % name,

num = raw_input("Please enter you phone number:")
print "Your phone number is %s \n" % int(float(num))


#2-5
i = 0
while i <= 10:
    print i,
    i += 1

print "\n"

for i in range(11):
    print i,


#2-6
num = int(raw_input('Enter a Number: '))

if num > 0:
    print "big one"
elif num < 0:
    print "small one"
else:
    print "Zero"


#2-7
s = raw_input('Enter a word: ')
i = 0
slen = len(s)
while i < slen:
    print s[i]
    i += 1

for h in range(len(s)):
    print s[h]


#2-8
num = 0
for i in range(5):
    num += int(raw_input('Enter a num: '))
print num


#2-9
num = 0
for i in range(5):
    num += float(raw_input('Enter a num: '))
print num/5


#2-10
num = raw_input('Enter a number between 1 and 100: ')
if num > 100 or num < 1:
    print "The number is wrong please try again\n"
    num = raw_input('Enter a number between 1 and 100: ')
else:
    print "Good job"


#2-15
a = int(raw_input("Enter a num: "))
b = int(raw_input("Enter a num: "))
c = int(raw_input("Enter a num: "))

if a > b and a > c:
    print a,
    if b > c:
        print b, c,
    else:
        print c, b,
elif b > a and b > c:
    print b,
    if a > c:
        print a, c,
    else:
        print c, a,
else:
    print c,
    if a > b:
        print a, b,
    else:
        print b, a,
"""
