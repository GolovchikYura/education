# из рандомных чисел найти сумму и произведение #
import random
print("Введите n:")
n = int(input())
a = ([random.randint(-200, 200) for b in range(n)])
print(a)
summa = 0
work=1
for x in a:
    summa += x
    work *= x
print("сумма:",summa)
print("Произведение:", work)

# Учись экономить операции и не делать 2 раза одно и тоже  #

