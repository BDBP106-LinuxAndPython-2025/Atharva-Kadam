"""(3) Write a Python script to check if a given string contains an email address or not."""
import re
a="^[a-z0-9\.\_\%\-]+@[a-z0-9\.\_]+\.[a-z]{2,}$"
b=["atharvakadam","255hsbd005@ibab.ac.in","atharvakadam26@gmail.com","atharvakadam26@","atharva.com"]
for i in b:
    print(f"The mail id is {i} : {bool(re.match(a,i))}")
