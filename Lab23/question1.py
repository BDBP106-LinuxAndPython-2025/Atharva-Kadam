"""(1) Write a regular expression that accepting a 3-digit integer between 000 and 255. Imple-
ment this in a script and test it for various possibilities"""
import re
a=r"^(1\d{2}|25[0-5]|2[0-4]\d|1\d\d|0\d{2})$"
# 25[0-5]|2[0-4]\d|1\d{2}|0\d{2})
# import random
# p=random.randint
# q=str(p)
q=["000","345","256","34","3422","1","234"]
for i in q:
   print(f"The 3-digit number is {i}: {bool(re.match(a,i))}")