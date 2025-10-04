#!/bin/bash

echo "The contents of the directory are:"
echo `ls`
echo "The largest file is" `ls -l | grep "^-"| sort -t " " -k 5 -nr | head -n 1 | gawk '{print ($9)}'`
