# Find the maximum of five numbers

s = [1,55,67,12,-10]

max = -99999999
for i in s:
    if i > max:
        max = i

print(f"Maximum number is {max}")