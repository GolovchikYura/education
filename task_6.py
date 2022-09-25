print("Введите число")
a = int(input())
divider=200
result=0
if a%50 != 0:
    print(0)
    exit(0)

numbers = {
    200: 4,
    100: 2,
    50: 1,
   }

while a>0:
    if a-divider>=0:
        result+=numbers[divider]
        a=a-divider
    else:
        divider=int(divider/2)
print(result)












