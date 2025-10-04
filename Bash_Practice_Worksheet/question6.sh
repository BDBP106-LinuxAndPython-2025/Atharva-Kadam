#!/bin/bash

echo "Enter the number:"
read n
if [ "$n" -gt 0 ]; then
	for i in {1..20}
	do
		result=$[ $n*$i ]
		echo ""$n" x "$i" ="$result
	done
else 
	echo "Enter a number greater than 0"
fi
