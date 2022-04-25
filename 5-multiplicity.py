# Given a number. Check if it is a multiple of 5 and 10 or 15 but not 30

import random

a = random.randint(10,1000)

if a % 5 == 0 and a % 2 == 0:
    print(f"Number {a} is multiplicity of 5 and 10")
elif a % 15 == 0 and not a % 2 == 0:
    print(f"Number {a} is multiplicity of 15 and not 30")
else:
    print(f"Number {a} not multiplicity of 5, 10 or 30")