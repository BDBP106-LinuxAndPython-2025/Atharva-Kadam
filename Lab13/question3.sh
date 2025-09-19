#!/bin/bash

#(i)
echo "The answer of (i) is"
gawk '$0 !~ /^>/' textfile3
#$0 refers to the entire line.
#!~ means "does not match" the following pattern.
#/^>/ is the pattern that matches lines starting with >.:wq
echo""

#(ii)
echo "The answer of (ii) is"
#The nucleotides are same of DNA and RNA except that RNA does not have Thymine it has Uracil instead of it
sed 's/T/U/g' textfile3
echo""

#(iii)
echo "The answer of (iii) is"
sed 's/^>seq1/human_gene/' textfile3
echo""

