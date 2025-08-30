#!/bin/bash

#(i)
echo "The answer of (i) is"
gawk '{if ($2<25)  print $1}' textfile2
echo""

#(ii)
echo"The answer of (ii) is"
gawk '{if ($3=="Physics") print $1}' textfile2
echo""

#(iii)
echo "The answer of (iii) is"
gawk '{print $1 "," $2 "," $3}' textfile2 > textfile2.csv


