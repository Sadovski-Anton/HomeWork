data: dict = {
    '0': 0,
    '1': 1,
    '2': 2,
}


def is_dvoika()-> int:
    number_10: str = (input('Введите число для конвертации:'))
    num_10: int = 0
    x: int = 1

    for i in number_10:
        num_10 += data[i] * 10**(len(number_10) - x)
        x += 1

    number_2: str = ''

    while num_10 > 0:
        number_2 = str(num_10 % 2) + number_2
        num_10 = num_10 // 2
    print(number_2)


is_dvoika()
