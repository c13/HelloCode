def subsequence(s):
    """
    Function will get 3n+1
    """
    new = 3*s + 1

    return new

n = 20
spisok=[]

for i in range(n):
    spisok.append(subsequence(i))

print(f"List of elements: {spisok}")