# Given two numbers, check if one is the square of the second

a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))

if (a**2 == b) or (a == b**2):
     print(f"One of the numbers {a} and {b} is the square of the other")
else:
     print(f"The numbers {a} and {b} are not each other's squares")
