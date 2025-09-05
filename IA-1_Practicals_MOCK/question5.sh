#!/bin/bash

if [ $# -eq 4 ]; then
	echo "The first argument is:" $1
	echo "The second argument is:" $2
	echo "The third argument is:" $3
	echo "The fourth argument is:" $4
else 
	echo "four arguments are required"
	exit 1
fi
