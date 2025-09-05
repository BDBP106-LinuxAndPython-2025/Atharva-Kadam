
#to sort according to height which is 2nd column
sort -t "," -k 2 -hr SOCR-HeightWeight.csv -o SOC.txt
#no the tallest person does not weigh the most 
#the tallest person weighs-75.1528inches amd weighs 146.9701(pounds)

#whereas the heaviest person weighs-170.924pounds and is 70.71295inches tall
sort -t "," -k 3 -hr SOCR-HeightWeight.csv -o SOC2.txt
