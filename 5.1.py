number_first: int = int(input('Введите сколько чисел хотите отобразить:'))
krat: int = int(input('Введите кратность:'))
number_point: int = int(input('Введите число - точку старта:'))

rez: int = number_first * krat + number_point
for i in range(number_point+krat, rez+1, krat):
    print(i)
