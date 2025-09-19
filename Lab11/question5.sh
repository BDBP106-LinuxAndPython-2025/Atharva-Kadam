#!/bin/bash

#Part (1)
var1="Testing"
var2="testing"
if [ $var1 \> $var2 ];then
	echo "$var1 is greater than $var2"
else
	echo "$var2 is greater than $var1"
fi

#output- testing is greater than Testing , that means in shell "if" command is interpreting that "testing" is greater than "Testing"


#after running the sort command on the teststringfile, it sorts the values as : "testing" and then "Testing" telling us that "testing" < "Testing" while we saw that in the if command, it interprets "testing" > "Testing"

#Thus, "if" command handles upper and lower cases just opposite to the way "sort" command handles upper and lower cases.
