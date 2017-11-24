age = int(input('Введите свой возраст: '))
if age < 7:
    print('Ты ходишь в детский сад')
elif age >= 7 and age <= 17:
    print('Ты ходишь в школу')
elif age >= 17 and age <= 23:
    print('Ты учишься в университете')
else:
    print('Ты работаешь')