#!/bin/bash

echo "Enter the word to be searched."
read w
echo "Enter the name of file."
read f
if [ -f "$f" ]; then
	grep -n "$w" "$f"
else 
	echo "The file doesn't exist"
fi
