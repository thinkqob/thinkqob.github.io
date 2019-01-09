#!/bin/bash

HOME=`pwd`
USER=`whoami`
TPID=`ps -u $USER|grep java|awk '{print $1}'`
OLDLOG=catalina-`date +%Y%m%d-%H%M%S`

echo -e "-------------------- Stop tomcat ------------------------"
ps -u $USER
kill -9 $TPID
sleep 1
ps -u $USER
sleep 1

echo -e "-------------------- Delete work file -------------------"
ls -al $HOME/tomcat/work/
rm -rf $HOME/tomcat/work/*
ls -al $HOME/tomcat/work/
sleep 1

echo -e "-------------------- Backup log file --------------------"
ls -al $HOME/tomcat/logs
mv $HOME/tomcat/logs/catalina.out $HOME/tomcat/logs/$OLDLOG.log
ls -al $HOME/tomcat/logs
sleep 1

echo -e "-------------------- Delete temp file -------------------"
ls -al $HOME/tomcat/temp
rm $HOME/tomcat/temp/*
ls -al $HOME/tomcat/temp
sleep 1

echo -e "-------------------- Start tomcat -----------------------"
cd $HOME/tomcat/bin/
./startup.sh
ps -u $USER
echo -e "-------------------- Done! ------------------------------"
