"""(1) Explain the various ways of importing module contents with examples."""
import random
print(f"Random integer from 1 to 10: {random.randint(1,10)}")

import math as m
print(f"The sin value of 3 is : {m.sin(3)}")

from cmath import sqrt
print(f"The square root of an integer in complex form is: {sqrt(4)}")