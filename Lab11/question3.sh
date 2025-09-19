#!/bin/bash

#using -n
echo "Insert the string:"
read n
if [ -n "$n" ]; then
	echo "String is not empty."
else
	echo "String is empty."
fi
#So -n will check if the string is full if we pass some string it will pass the "if" statement 

#using -z
echo "What is your string?"
read h
if [ -z "$h" ]; then
        echo "String is empty."
else
        echo "String is not  empty."
fi
#-z will check if the string is empty only if the string is empty it will pass the "if" statement 
