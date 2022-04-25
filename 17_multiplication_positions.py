# Set a list of N elements filled with numbers from [-N, N]. Find the product of the elements at the specified positions. Positions are stored in the file file.txt in one line one number
import random

n = 10
spisok = [random.randint(-12, 12) for _ in range(n)]
print(f"List of elements: {spisok}")

multi = 1
lines, s = [], []
with open('17_positions.txt', 'r') as f:
    lines = f.readlines()

for line in lines:
    line = int(line.strip())
    s.append(spisok[line-1])
    multi *= spisok[line-1]

print()
print(f"Multiplication of elements {s} is {multi}")

