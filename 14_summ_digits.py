# Calculate the sum of digits in a real number.
import random


# задаем случайное вещественное число из диапазона
a = random.uniform(1, 1001)
print('Задано число:', a)

a = str(a).replace('.', '')     # переводим в строковый тип, убираем точку
print(a)
summa = sum(map(int, a))        # переводим в числовой тип, считаем сумму
print('Сумма цифр данного числа равна:', summa, '\n')
