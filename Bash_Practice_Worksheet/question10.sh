#!/bin/bash

echo "Enter the .csv file:"
read f
if [[ "$f" != *.csv ]]; then
	echo "Enter a .csv file"
else 
	gawk -F, '{print $1,$3}' "$f"
fi
