name = input('Ввведите имя: ')
age = input('Ввведите возраст: ')
city = input('Ввведите город: ')

print('Приветствуем тебя,', name, age, 'лет', 'из', city)
print(f'Приветствуем тебя, {name} {age} лет из {city}')
print('Приветствуем тебя, {} {} лет из {}'.format(name, age, city))
