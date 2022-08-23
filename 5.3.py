number_finish: int = int(input('Введите конечное число:'))
rez = ''
j = 0
for i in range(number_finish+1):
    if not i%2:
        rez += ' ' + str(i)
        j += 1
    if j == 5:
        print(rez)
        rez = ''
        j = 0
    elif i == number_finish:
        print(rez)

