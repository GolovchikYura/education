#дни недели#

print("Введите день недели и я переведу его на английслий:")

a=(input())

days = {
    'пн': 'mn',
    'вт': 'ts',
    'ср': 'wd',
    'чт': 'th',
    'пт': 'fr',
    'сб': 'st',
    'вс': 'sn',
}

print(days[a])