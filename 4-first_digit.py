# Show the first digit of the fractional part of a number

a = float(input("Enter a fractional number with dot:"))

n = round(a*10)%10

print(f"First digit of the fractional part is {n}")