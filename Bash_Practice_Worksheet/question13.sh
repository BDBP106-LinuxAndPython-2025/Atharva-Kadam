#!/bin/bash

#(13) Display a menu with options: 1) Show date, 2) Show calendar, 3) show logged-in users,4) Exit. The script should display these options, execute the appropriate command according to the option.

echo "1) Show Date"
echo "2) Show Calender"
echo "3) Show Logged-in Users"
echo "4) Exit"

read  -p "Choose your option (enter only the number of the option):" option
if [ "$option" -eq 1 ]; then
	date
elif [ "$option" -eq 2 ]; then
	cal
elif [ "$option" -eq 3 ]; then
	who
elif [ "$option" -eq 4 ]; then
	echo "Exit"
else 
	echo "Please input the correct option"
fi


