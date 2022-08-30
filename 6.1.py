def is_dvoika()-> int:
    number_10: int = int(input('Введите число для конвертации:'))
    number_2: str = ''
    while number_10 > 0:
        number_2 = str(number_10 % 2) + number_2
        number_10 = number_10 // 2
    print(number_2)


is_dvoika()
