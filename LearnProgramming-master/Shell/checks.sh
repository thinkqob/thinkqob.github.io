#!/bin/sh
echo -e "\n"
echo "------check disk-------"
echo "command: df -h"
df -h
echo -e "\n"


echo "------check CPU, wait 20 seconds-------"
echo "command: sar -u 2 10"
sar -u 2 10|tail -1|awk '{print "CPU used:",100-$8,"%" }'
echo -e "\n"


echo "------check Mem -------"
echo "command: free -m"
free -m|awk '/Mem/ {print "Mem used:",($3-$6-$7)/$2*100,"%" }'
echo -e "\n"


echo "------check network, wait 60 seconds-------"
echo "command: sar -n DEV -u 2 10"
sar -n DEV -u 2 10|grep bond0|tail -1|awk '{print "bond0 tx network util:",$6/131072000*100,"%","bond0 rx network util:",$5/131072000*100,"%"}'
sar -n DEV -u 2 10|grep bond1|tail -1|awk '{print "bond1 tx network util:",$6/131072000*100,"%","bond1 rx network util:",$5/131072000*100,"%"}'
sar -n DEV -u 2 10|grep bond2|tail -1|awk '{print "bond2 tx network util:",$6/131072000*100,"%","bond2 rx network util:",$5/131072000*100,"%"}'
echo -e "\n"


echo "------check I/O, wait 25 seconds----------" 
echo "command: sar -d 5 5"
sar -d 5 5|grep dev104-8|tail -1|awk '{print "I/O used:",$10,"%" }'
echo -e "\n"


echo "------check route --------" 
echo "command: cat /etc/sysconfig/*route*"
cat /etc/sysconfig/*route*
echo "command: netstat -rn"
netstat -rn
echo -e "\n"


echo "------check server log-------"
echo "command: grep error /var/log/messages"
grep error /var/log/messages
echo -e "\n"


echo "------check server date -------"
echo "command: date"
date
echo -e "\n"
