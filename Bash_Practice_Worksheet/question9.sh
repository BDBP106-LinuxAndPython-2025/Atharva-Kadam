#!/bin/bash

A=(12 23 223 2367 37278 22)
max=${A[0]}
for i in "${A[@]}"
do
	if [ "$max" -lt "$i" ]; then
		max=$i
	fi
done
echo "The maximum number is:" $max

min=${A[0]}
for i in "${A[@]}"
do
	if [ "$min" -gt "$i" ]; then
		min=$i
	fi
done
echo "The minimum number is:" $min

sum=0
for i in ${A[@]}
do
	sum=$[ $sum+$i ]
done
echo "The sum of numbers is:" $sum

