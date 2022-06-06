# В заданном списке вещественных чисел найдите разницу между максимальным и
# минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import os
from random import *
os.system("cls")

list = [1.1, 1.2, 3.1, 5, 10.01]  # [uniform(1, 21) for i in range(8)]
print(list, '\n')

result = []
for i in range(len(list)):
    if list[i] - round(list[i]) == 0:
        continue
    else:
        result.append(round(list[i] - round(list[i]), 3))

print(result)
print('\nМаксимальное число: ', max(result))
print('\nМинимальное число: ', min(result))
print('\nРазница: ', max(result) - min(result))