#!/bin/bash

echo "Enter the directory name."
read n
if [ -d "$n" ]; then
       cd "$n"	
       for f in *.txt
       do
	       if [ -e "$f" ]; then
		       mv "$f" "old_$f"
	       else
		       echo "There are no files ending with .txt"
	       fi
       done
else 
	echo "The directory doesnt exist."
fi
