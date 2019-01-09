#!/usr/bin/ python
# billcount v0.1.2
# input: multi file from smp/cdr
# date：20160823

import os, sys


def count(all_file):
    call_count = {}
    for filename in all_file:
        f = open(filename)
        lines = f.readlines()
        lines.remove(lines[0])
        lines.remove(lines[-1])
        for line in lines:
            temp_line = line.split('|')
            if temp_line[0] not in call_count.keys():
                # an empty dict include all the numbers,
                # calling times, calling duration, calling innet, calling outnet,
                # called times, called duration, called innet, called outnet
                call_count[temp_line[0]] = [0, 0, 0, 0, 0, 0, 0, 0]
    
            if temp_line[2] == "0":
                # count calling and update dict
                call_count[temp_line[0]][0] += 1
                call_count[temp_line[0]][1] += int(temp_line[10])
                if temp_line[12] == "0":
                    call_count[temp_line[0]][2] += 1
                elif temp_line[12] == "1":
                    call_count[temp_line[0]][3] += 1
            elif temp_line[2] == "1":
                # count called and update dict
                call_count[temp_line[0]][4] += 1
                call_count[temp_line[0]][5] += int(temp_line[10])
                if temp_line[12] == "0":
                    call_count[temp_line[0]][6] += 1
                elif temp_line[12] == "1":
                    call_count[temp_line[0]][7] += 1
    f.close()
    return call_count


def main(argv):
    path = os.path.join(os.getcwd(), argv)
    os.chdir(path)
    all_file = os.listdir(path)
    cc = count(all_file)
    keys = cc.keys()
    keys.sort()
    for key in keys:
        print "%11s%5s%5s%5s%5s%5s%5s%5s%5s" % \
        (key ,cc[key][0], cc[key][1]/60, cc[key][2], cc[key][3], \
            cc[key][4], cc[key][5]/60, cc[key][6], cc[key][7])

if __name__ == '__main__':
    argv = sys.argv[1]
    main(argv)
