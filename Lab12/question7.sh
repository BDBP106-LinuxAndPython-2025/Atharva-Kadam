#!/bin/bash

function directory {
	local n=$1
	if [ -d "$n" ]; then
		echo "The directory exists" 
	ls	
	else
		echo "The directory  doesnt exist"
		mkdir $n
	fi
}
directory "$1"
