#!/bin/bash

#checking if a file exists

echo "Enter file name:"
read n
if [ -f "$n"  ]; then 
	echo "File exists"
else
	echo "File doesnt exist"
fi

if [ -x "$n" ]; then 
	echo "File is executable"
else
	echo "File is not executable"
fi
