win: str = input('Введите символ на выбор < или >:')
data: list = ['a', 'b', 'c', 'd', 'e', 'f', 'z']
number_start = 0
while True:
    if win == '<':
        if number_start == -len(data):
            number_start = 0
        print(data[number_start - 1])
        number_start -= 1
        win: str = input('Введите символ на выбор < или >:')
    elif win == '>':
        if number_start == len(data)-1:
            number_start = -1
        print(data[number_start + 1])
        number_start += 1
        win: str = input('Введите символ на выбор < или >:')

