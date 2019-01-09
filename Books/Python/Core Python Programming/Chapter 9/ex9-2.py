def file_seek(filename, line):
    f = open(filename, 'r')
    c = f.readlines()
    for i in xrange(line):
        print c[i],
    print len(c)
    f.close()

file_seek('test.txt', 6)
