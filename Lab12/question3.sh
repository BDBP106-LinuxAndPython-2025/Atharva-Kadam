#!/bin/bash

read n
x=1
until [ $x -gt 15 ]
do 
	y=$[n*x]
	echo "$n x $x ="$y
	x=$[x+1]
done

