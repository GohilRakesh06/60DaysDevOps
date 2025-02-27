#!/bin/bash
echo "deleting log files older then 7 days"
find /var/log -type f -mtime +7 -exec rm -f {} \;
echo "old log files are deleted"
