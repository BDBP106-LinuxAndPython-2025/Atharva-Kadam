#!/bin/bash
n=0
while [ $n -le 50 ]
do 
    x=$[ n%2 ]
if [ $x -eq  0 ]; then	
	echo "The even numbers are:"$n
fi
n=$[ $n+1 ] 
done	

#using the for loop
numbers=({0..50})
for num in ${numbers[*]}
do
	if(( $num%2== 0 )); then
		echo "The even numbers using for loop are:" $num
	fi
done
