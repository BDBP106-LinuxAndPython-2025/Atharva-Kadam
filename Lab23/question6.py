"""(6) Write a Python script that reads in a piece of text and prints it out masking out
email addresses. Thus and email address ”helloworld@python.com” should become
”h********d@python.com”."""
import re

sentence="Hello my email id is atharvakadam@gmail.com and my clg id is 255hsbd005@ibab.ac.in"

def mask_email(match):
    email = match.group()
    name, domain = email.split('@')
    if len(name) > 2:
        name = name[0] + '*'*(len(name)-2) + name[-1]
    else:
        name = '*' * len(name)
    return name + '@' + domain

masked_text = re.sub("[a-z0-9\.\_\%\-]+@[a-z0-9\.\_]+\.[a-z]{2,}", mask_email, sentence)
print(masked_text)
