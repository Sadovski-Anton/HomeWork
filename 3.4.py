first = input('Ввведите первое число: ')
sekond = input('Ввведите второе число: ')
third = input('Ввведите третье число: ')

first_new = first.startswith('-')
sekond_new = sekond.startswith('-')
third_new = third.startswith('-')

result_pol = 3 - first_new - sekond_new - third_new
result_otr = 3 - result_pol

print(f'Пользователь ввел  положительных чисел: {result_pol}')
print(f'Пользователь ввел  отрицательных чисел: {result_otr}')
