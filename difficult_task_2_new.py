#программа определяющая является ли число простым

print("Введите число:")
a = int(input())

status = 1

for i in range(2,a):
 if(a % i == 0):
  status = 0
  break

if(status == 0):
 print('Число сложное')
else:
 print('Число простое')
