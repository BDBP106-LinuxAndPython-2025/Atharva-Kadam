#!/bin/bash

echo "Enter the file name."
read n
if [ -f "$n" ]; then
	wc "$n"
else 
	echo "File doesnt exist"
fi

echo "Enter the file name."
read m
if [ -f "$m" ]; then
        echo "The number of words are `wc -w "$n"`"
	 echo "The number of lines are `wc -l "$n"`"
	  echo "The number of characters are `wc -m "$n"`"
else
        echo "File doesnt exist"
fi
