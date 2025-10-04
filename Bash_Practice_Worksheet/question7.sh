#!/bin/bash

threshold=80

disk_usage=$(df -h | tail -n 1 | gawk '{print $5}' | sed 's/%//' )
if [ $disk_usage -ge $threshold ]; then
	echo "Warning the disk has been used above threshold"
else
	echo "Disk used is below threshold"
fi
