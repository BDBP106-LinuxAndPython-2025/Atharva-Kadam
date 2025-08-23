#!/bin/bash

echo "Input a number: "
read n
if (( "$n" > 100 )); then #here only one square bracket is required or only 2 curved brackets
	echo "The number is greater than 100." #here the indentation is required before echo It can be corrected by adding a tab space
else
	echo "The number is not greater than 100." #here the indentation is required before echo. It can be corrected by adding a tab space
fi

#The last 3 lines were not needed as they were same as 1st if statement 
