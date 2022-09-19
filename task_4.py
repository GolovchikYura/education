# из рандомных чисел найти сумму и произведение #
import random
print("Введите n:")
n = int(input())
a = ([random.randint(-200, 200) for b in range(n)])
print(a)
summa = 0
for x in a:
    summa += x
print("сумма:",summa)
work=1
for x in a:
    work *= x
print("Произведение:", work)



