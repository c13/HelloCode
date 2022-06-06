# Implement list shuffling algorithm

import time


def random_number(n):
    '''
    this function uses time.perf_counter to get some random digit /int every time to get as
    random as possible from given list.

    '''
    digit = int(str(time.perf_counter()).split('.')[-1][-1])
    new_digit = round(digit / len(n))
    if digit <= len(n):
        return n[digit - 1]
    elif new_digit <= len(n):
        return n[new_digit - 1]
    return n[0]


n = 10
spisok = [i for i in range(n)]
print(f"List of elements: {spisok}")

mixed = []
while len(spisok) > 0:
    i = random_number(spisok)
    mixed.append(i)
    spisok.remove(i)

print(f"Mixed list of elements: {mixed}")
