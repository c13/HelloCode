# Display numbers from -N to N

n = int(input("Enter positive number:"))

print(f"All numbers from {-n} to {n}")
for i in range(-n,n+1):
    print(i, end=' ')