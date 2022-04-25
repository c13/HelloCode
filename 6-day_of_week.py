# Given a number representing the day of the week. Display its name and indicate whether it is a holiday.

import random
a = random.randint(1,7)

days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

print(f"Number {a} is {days[a-1]}")