hith: int = int(input('Введите нужную глубину треугольника:'))
stroka: list = []
for i in range(1, hith + 1):
    stroka.insert(0, 1)
    for j in range(1, len(stroka) - 1):
        stroka[j] += stroka[j+1]
    print(stroka)

