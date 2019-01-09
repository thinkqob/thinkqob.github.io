def print_file(filename):
    f = open(filename, 'r')
    for eachLine in f:
        if eachLine[0] != '#':
            print eachLine,


print_file('test.txt')
