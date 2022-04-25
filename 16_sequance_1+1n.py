# set a list of n numbers in the sequence (1+〖1/n)〗^n and display their sum

import random

n = random.randint(6, 16)
print(f"Massive length generated {n}")

massive = []

for i in range(1, n+1):
    massive.append(1+(1/i)**i)
print(f'Massive sum is {sum(massive):.2f}')
