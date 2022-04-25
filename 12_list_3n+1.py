# make dictionary for n elements: element number, 3n+1

n = 10

Dictionary = {i: 3*i+1 for i in range(1, n+1)}
print(f"List of elements 3n+1: {Dictionary}")
