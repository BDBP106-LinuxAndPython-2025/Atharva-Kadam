"""(5) Write a Python script that scans through a given piece of text and extracts all unique
email addresses from it."""
import re
a="[a-z0-9\.\-\%\_]+@[a-z0-9\.\_]+\.[a-z]{2,}"
string1="atharvakadam26@gmail.com poorvatillu1509@gmail.com poorvatillu1509@gmail.com 255hsbd005@ibab.ac.in sohelmulla19@ lalitaphul@gmail.ac.in"
set1=set(re.findall(a,string1))
print(set1)