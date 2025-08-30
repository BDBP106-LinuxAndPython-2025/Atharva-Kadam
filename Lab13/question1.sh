#!/bin/bash

#(i)
sed -n -f q1sed textfile
echo""

#(ii) 
sed s'/language/lang/g' textfile
echo""

#(iii)
sed '/is/d' textfile
echo""

#(iv)
sed '=' textfile | sed 'N;s/\n//'
#
echo""

#(v)
sed '1,2d' textfile
echo""

#(vi)
sed -n 'p;n' textfile
echo""
#-n doesnt give output for each command but waits for print command suppresses automatic printing
#p will print the current line
#n after p skips the next line

#(vii)
sed '0,/Python/s/Python/python/;0,/language/s/language/lang/' textfile
#we are defining from 0,/Python that replace only from 0 to Python and then stop replacing and same in languages 
