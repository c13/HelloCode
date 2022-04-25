# Report in which quarter of the coordinate plane or on which axis the point with coordinates X and Y is located

import random
x = random.randint(-50, 50)
y = random.randint(-50, 50)

if x > 0 < y:
    print(f"Point {x,y} positioned in 1 quater")
elif x > 0 > y:
    print(f"Point {x, y} positioned in 2 quater")
elif x < 0 > y:
    print(f"Point {x, y} positioned in 3 quater")
else:
    print(f"Point {x, y} positioned in 4 quater")