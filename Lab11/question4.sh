#!/bin/bash

val1=Jayashree
val2=Nagesh
if [ $val1 \> $val2 ]; then
echo "$val1 is greater than $val2"
else
echo "$val1 is lesser than $val2"
fi

#after adding "\" before ">" new file is not created and the script is executed correctly.As the "\" acts as an escape character 
