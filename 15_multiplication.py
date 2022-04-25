# Write a program that receives a set of products of numbers from 1 to N.
# Example: let N = 4, then
# [ 1, 2, 6, 24 ]

import random
def multy(a):
    if a == 1:
        return 1

    return a * multy(a - 1)


n = random.randint(6,12)

print("Sequence for ")
for i in range(1, n + 1):
    print(multy(i), end=' ')

