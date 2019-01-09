#!/usr/bin/env python

import string
import keyword

alphas = string.ascii_letters + '_'
nums = string.digits

print 'Welcome to the Identifier Checker v1.1'
print 'Tests must be at least 1 chars long'
myInput = raw_input('Identifier to test? ')

if myInput > 0:
    if myInput[0] not in alphas:
        print '''invalid: first symbol must be alphabetic'''
    elif myInput in keyword.kwlist:
        print '''invalid: symbol must not be keyword'''
    else:
        for otherChar in myInput[1:]:
            if otherChar not in alphas + nums:
                print '''invalid: remaining symbols must be alphabetic'''
                break
        else:
            print "okay as an identifier"
