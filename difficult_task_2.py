print("Введите число:")
a = int(input())
b = 0
i = 2
if (a % i == 0):
        b = b+1
if (b <= 0):
    print("Число простое")
else:
    print("Число сложное")