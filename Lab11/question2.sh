#!/bin/bash

#Using -e
echo "File/Directory Name"
read n
if [ -e "$n" ];then 
	echo "It exists"
else
	echo "It doesn't exist"
fi

#-e in the if statement will search for files , directories in the current directory 

#Using -s 
echo "File Name"
read n
if [ -s "$n" ];then
        echo "It contains some content"
else
        echo "It doesn't contain anything"
fi

#-s will check if the file name we have typed contains something or not if the file contains something it will return the if statement if not then it will print the else statement.

#Using -f
echo "File Name"
read n
if [ -f "$n" ];then
        echo "The file exists"
else
        echo "The file doesnt exist"
fi

#-f will check if the file exists in the current directory or not it only checks for files.

