from pprint import pprint
number = int(input('Введите число: '))
result = dict((i, {'name': input('Введите имя: '), 'email': input('Введите почту: ')}) for i in range(1, number + 1))

pprint(result)

