#!/bin/bash
echo "Enter Full path of log file to find errors "
read filename
log_file=$filename
output_file="errors.log"

echo "Extracting error messages from $log_file..."

awk '/error|ERROR|Error/ {print}' "$log_file" > "$output_file"



