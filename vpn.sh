#!/bin/bash
read -p "Enter the time(In seconds) :" t
while true
do
 i=`expr $RANDOM % 49`
 echo "--------CONNECTION--------"
 nordvpn c 
 sleep 1
 echo "--------STATS--------"
 nordvpn status
 echo "--------SLEEP--------"
 echo "Sleeping for $t seconds"
 sleep $t
done 

