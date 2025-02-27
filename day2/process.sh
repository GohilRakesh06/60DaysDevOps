#!/bin/bash
echo "currently running processes in system:"
ps -aux >  process_list.txt
cat process_list.txt
