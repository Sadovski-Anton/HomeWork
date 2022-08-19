number = int(input('Введите число: '))
result = dict((i, {'name': input('Введите имя: '), 'email': input('Введите почту: ')}) for i in range(number + 1))

print(result)
