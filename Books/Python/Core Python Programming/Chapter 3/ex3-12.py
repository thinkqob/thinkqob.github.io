#!/usr/bin/env python
"""combine two file to a new file"""

# open the first file
first_file = raw_input('Enter the first filename you wang to combine: ')
second_file = raw_input('Enter the second filename you wang to combine: ')
new_file = raw_input('Enter the new filename you wang to write: ')

first_obj = open(first_file, 'r')
second_obj = open(second_file, 'r')
new_obj = open(new_file, 'w')

for eachLine in first_obj:
    new_obj.write(eachLine)

new_obj.write('\n')

for eachLine in second_obj:
    new_obj.write(eachLine)

first_obj.close()
second_obj.close()
new_obj.close()
