# программа выводит делители числа #
print("Введите число:")
a = int(input())
print(1)
for i in range(2,a):
 if(a % i == 0):
  print(i)
print(a)

