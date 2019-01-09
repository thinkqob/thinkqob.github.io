#!/usr/bin/ python
# billcount v0.2.2 
# input: two files(acr_delete_table_201608, acr_vpn_201608) from db unloaded
# date: 20160823

import sys


def count(acr_ipc, acr_csag):
    call_count = {}
    acr_ipc = open(acr_ipc)
    acr_ipc_lines = acr_ipc.readlines()
    for line in acr_ipc_lines:
        temp_line = line.split('|')
        if temp_line[0] not in call_count.keys():
            # an empty dict include all the numbers,
            # calling times, calling duration, calling innet, calling outnet,
            # called times, called duration, called innet, called outnet
            call_count[temp_line[0]] = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    
        if temp_line[2] == "0":
            # count calling and update dict
            call_count[temp_line[0]][0] += 1
            call_count[temp_line[0]][1] += int(temp_line[10])
            if temp_line[11] == "0":
                call_count[temp_line[0]][2] += 1
            elif temp_line[11] == "1":
                call_count[temp_line[0]][3] += 1
        elif temp_line[2] == "1":
            # count called and update dict
            call_count[temp_line[0]][4] += 1
            call_count[temp_line[0]][5] += int(temp_line[10])
            if temp_line[11] == "0":
                call_count[temp_line[0]][6] += 1
            elif temp_line[11] == "1":
                call_count[temp_line[0]][7] += 1
    acr_ipc.close()

    acr_csag = open(acr_csag)
    acr_csag_lines = acr_csag.readlines()
    for line in acr_csag_lines:
        temp_line = line.split('|')
        if temp_line[0] in call_count.keys():
            call_count[temp_line[0]][8] += 1
    acr_csag.close()

    return call_count


def main(acr_ipc, acr_csag):
    cc = count(acr_ipc, acr_csag)
    keys = cc.keys()
    keys.sort()
    for key in keys:
        print "%11s%5s%5s%5s%5s%5s%5s%5s%5s%5s" % \
        (key ,cc[key][0], cc[key][1]/60, cc[key][2], cc[key][3], cc[key][4], \
            cc[key][5]/60, cc[key][6], cc[key][7], cc[key][8])

if __name__ == '__main__':
    acr_ipc = sys.argv[1]
    acr_csag = sys.argv[2]
    main(acr_ipc, acr_csag)
