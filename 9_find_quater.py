# Specifying the number of a quarter of a rectangular coordinate system, show the valid coordinate values for the points of this quarter

import sys
a = int(input("Enter quadrant number of the rectangular coordinate system:"))

if a == 1:
    print(f"Limits for point coordinats is {sys.maxsize,sys.maxsize}")
elif a == 2:
    print(f"Limits for point coordinats is {sys.maxsize,-sys.maxsize}")
elif a == 3:
    print(f"Limits for point coordinats is {-sys.maxsize,-sys.maxsize}")
elif a == 4:
    print(f"Limits for point coordinats is {-sys.maxsize,sys.maxsize}")
else:
    print(f"Quadrant numbers is only 1, 2, 3 or 4")