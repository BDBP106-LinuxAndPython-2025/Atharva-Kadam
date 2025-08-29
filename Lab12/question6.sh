#!/bin/bash

function maximum(){
	local x=$1
	local y=$2
	if [ "$x" -gt "$y" ]; then
	echo "The maximum number is:"$x
else
	echo "The maximum number is:"$y
fi
}
maximum "$1" "$2"
