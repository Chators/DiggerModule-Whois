#!/bin/bash

#Programme permettant d'executer Datasploit
#Il permet d analyser un nom de domaine
#Il faut impérativement 1 arguments :
#1. Nom de domaine

[ $# != 1 ] && { echo "Il faut 1 seul arguments !"; exit 1; }

fileLog=$(mktemp reports/datasploitLog.XXXXXXXX);
python domainOsint.py $1 -o json > $fileLog;
fileJsonName=$(cat $fileLog | tail -n1 | cut -d ' ' -f5);
python formatJsonDateDNS.py $fileJsonName $1
cat $fileJsonName;
rm $fileJsonName;
rm $fileLog;
