# Find the distance between two points in space

import random
from math import sqrt

a, b = [], []
for i in range(2):
    a.append(random.randint(-50, 50))
    b.append(random.randint(-50, 50))
print(f"Points generated {a[0],a[1]} and {b[0],b[1]}")

s = sqrt((a[0]-a[1])**2+(b[0]-b[1])**2)
print(f"Distance between points {round(s,2)}")