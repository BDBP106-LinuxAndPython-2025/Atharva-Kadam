#!/bin/bash

echo "Enter a number."
read n
if [ $n -le 1 ]; then
	echo "It is not a Prime Number."
	exit
fi
	for((i=2;i<=$n/2;i++))
	do
		if [ $((n%i)) -eq 0 ]; then
			echo "It is not Prime."
			exit
		fi
	done
echo "it is prime"
#Method2
: '
echo "Enter a number"
read m
if [ $m -le 1 ]; then
        echo "It is not a Prime Number."
        exit
fi
sqrt=$(echo "sqrt($m)"| bc )
       for((i=2;i<=sqrt;i++))
        do
                if [ $((m%i)) -eq 0 ]; then
                        echo "It is not Prime."
                        exit
                fi
        done
echo "it is prime"
'
