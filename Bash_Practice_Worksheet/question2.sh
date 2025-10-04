#!/bin/bash

echo "Enter file name"
read n
if [ -f "$n" ]; then
	echo "File exists."
	if [ -r "$n" ]; then
		echo "File is readable."
	else 
		echo "File is not readable."
	fi
	if [ -w "$n" ]; then
                echo "File is writable."
        else
                echo "File is not writable."
        fi
else 
	echo "The file doesn't exist"
fi
