number = int(input('Введите число: '))
list_numbers = list(2**i for i in range(1, number+1))
print(list_numbers)