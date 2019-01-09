# a)
def findchar(string, char):
    for i in range(len(string)):
        if char == string[i]:
            print i
        else:
            pass

findchar(string='abcdefg', char='g')


# b)
def rfindchar(string, char):
    for i in range(1, len(string) + 1):
        if char == string[-i]:
            print len(string) + 1 - i
        else:
            pass

rfindchar('abgdefg', 'g')


# c)
def subchr(string, origchar, newchar):
    newstring = ''
    for i in range(len(string)):
        if origchar == string[i]:
            newstring += newchar
        else:
            newstring += string[i]
    print newstring

subchr('abcdefg', 'e', 'z')
