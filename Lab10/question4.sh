#!/bin/bash

#giving exit code

echo "Enter file name:"
read n
if [ -f "$n"  ]; then
	echo "File exists"
	exit 200
else
	echo "File does not exist"
	exit 201
fi

#to check if the correct exit code is generated after executing the script give the command "echo $?"

#part (ii)
echo "File name:"
read n
if [ -f "$n" ]; then
	echo $?
        echo "File exists"
        exit 200	
else
        echo "File does not exist"
	exit 201
fi
#after using echo $? after if statement it doesnt give the exit code because the echo $? command has to be run in the terminal out of the script and only after the script is executed will the exit code be shown

#part (iii)
echo "file"
read n
if [ -f "$n" ]; then
        echo "File exists"
	exit 200
	echo $?

else
        echo "File does not exist"
	exit 201
	echo $?
fi
#no after the exit 200 and exit 201 the echo $? command doesnt work because first the script has to be executed only then will the echo $? command work 
