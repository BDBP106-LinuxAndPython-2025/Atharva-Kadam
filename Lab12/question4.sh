#!/bin/bash

numbers=()
read -ra numbers < nums.txt
echo ${numbers[*]}
for number in ${numbers[*]} 
do
	y=$[$number*2]
	echo "The doubled output of numbers of the array are:" $y
done
