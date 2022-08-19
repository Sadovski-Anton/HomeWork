text = input('Введите текст: ')
number_counter = dict((i, text.count(i)) for i in text)

print(number_counter)
