number_first: int = int(input('Введите сколько чисел хотите отобразить:'))
kratnost: int = int(input('Введите кратность:'))
number_point: int = int(input('Введите число - точку старта:'))

rez: int = number_first * kratnost + number_point
for i in range(number_point + kratnost, rez+1, kratnost):
    print(i)
