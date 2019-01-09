#!/usr/bin/env python
"""readTextFile.py -- read text file"""

# get filename
fname = raw_input('enter filename: ')
print

# attempt to open file for reading
try:
    fobj = open(fname, 'r')
except IOError, e:
    print "*** file open error:", e
else:
    # display context to the screen
    for eachLine in fobj:
        print eachLine,
    fobj.close()
