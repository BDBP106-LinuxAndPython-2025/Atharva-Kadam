#!/bin/bash

echo "Hi i am $1"
echo "Exit code of the last command" $?
echo "The name of shell script" $0 
echo "The number of arguments" $#
echo "All the arguments are" $@ 
