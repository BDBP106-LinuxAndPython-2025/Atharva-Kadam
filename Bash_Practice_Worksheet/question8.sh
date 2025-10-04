#!/bin/bash

echo "a) Current Date and Time" 
date
echo "b) Logged in Users" 
who
echo "c) System uptime" 
uptime
echo "d) Top 5 processes by memory usage." 
ps aux | sort -k 4 -nr | head -n 5
