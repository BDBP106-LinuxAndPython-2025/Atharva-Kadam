#!/bin/bash

for i in {1..5}
do
	free_memory=$(free -m | gawk '{print $4}' | tail -n 2 | head -n 1)
	echo "Free Memory available is:"$free_memory"MB"
	if [ "$free_memory" -lt 500 ]; then
		echo "Warning memory svsilsble is less than 500MB."
	fi
sleep 1m
done

