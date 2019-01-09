import os
F = raw_input('pls input a file name:')
n = 0
f = open(F, 'r')
for i in f:
    print i,
    n += 1
    if n == 25:
        n = 0
        os.system('pause')
f.close()

