#!/bin/bash
# Getting the username of the logged-in user
logged_in_user=$(whoami)
# Checking if the user is logged in
if [ -n "$logged_in_user" ]; then 
	echo "The logged-in user is:" $logged_in_user
else
	echo "User is not logged in"
fi

#Syntax changes-
#1. change the curved bracket to square bracket 
#2. fix the typo in the variable loged_in_user to logged_in_user
#3. remove the unnecessary indentation before "then" and shift "then" to the previous line  
#4. fix the typo in the variable from logged-in_USER to logged_in_user
#5. also remove the double quotes after the variable and add them before the variable
