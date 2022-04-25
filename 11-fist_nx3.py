# print first n elements of power of -3

def power(s):
    """
    Function will get power of number -3
    """
    new = (-3) ** s

    return new

n = 20
spisok=[]

for i in range(n):
    spisok.append(power(i))

print(f"List of elements power of -3: {spisok}")