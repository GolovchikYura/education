#Положительные и отрицательные числа#
import random
print("Введите n:")
n = int(input())
a = ([random.randint(-200, 200) for b in range(n)])
print(a)
positive = 0
negative = 0
for x in a:
    if x>0:
        positive+=1
    else:
        negative+=1
print('Положительных:', positive)
print('Отрицательных:', negative)
















