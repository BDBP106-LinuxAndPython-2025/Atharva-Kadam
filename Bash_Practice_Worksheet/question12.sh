#!/bin/bash

for i in {1..6} #since 1 min has 60s seconds and we want to find the time every 10 seconds so only 6 times will the time be showed
do
	date +%T
	sleep 10
done
