#!/bin/bash
echo "Enter File Name(full path) To Search";
read filename
if [ -f "$filename" ]; 
then
	echo "$filename exists "
	cat $filename
else
	echo "$filename is not present"
fi


