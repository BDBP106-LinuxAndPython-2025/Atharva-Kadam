#!/bin/bash

file='data.txt'

while IFS=" " read -r c1 c2 c3 c4
do 
	echo "column1: $c1 column2: $c2 column3: $c3 column4: $c4"
done < "$file"
