#!/bin/bash

function divide {
echo $1 $2
	if [ $2 -eq 0 ]; then
		echo "Divisor cannot be zero."
	else
	local quotient=$(echo "scale=2; $1/$2" | bc)
	local remainder=$[ $1%$2 ]

	echo "The quotient is" $quotient
	echo "The remainder is" $remainder
	fi
}
div=$(divide $1 $2)
echo $div
