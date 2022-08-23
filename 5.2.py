number_first: int = int(input('Введите первое число:'))
ryx: str = input('Введите нужное математическое действие:')
number_second: int = int(input('Введите второе число: '))
if ryx == '+':
    rez = number_first + number_second
elif ryx == '-':
    rez = number_first - number_second
elif ryx == '/':
    rez = number_first / number_second
elif ryx == '*':
    rez = number_first * number_second
else:
    rez = False

if rez:
    print(f'{number_first} {ryx} {number_second} = {rez}')
else:
    print('Введите корректное математическое действие!')


