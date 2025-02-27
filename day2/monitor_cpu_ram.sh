#!/bin/bash
log_file="system_log.log"
while true; do
	echo "CPU Usage:" >> "$log_file"
    	top -bn1 | grep "Cpu(s)" | awk '{print "User: " $2 "%, System: " $4 "%, Idle: " $8 "%"}' >> "$log_file"
    
    	echo "RAM Usage:" >> "$log_file"
    	free -h | awk 'NR==2{print "Used: " $3 ", Free: " $4 ", Total: " $2}' >> "$log_file"
	sleep 5;
done
