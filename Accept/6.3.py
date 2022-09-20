data: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def sdvig(data: list) -> list:
   n: int = int(input('Введите число смещения чисел:'))
   c: int = 0
   while c < n:
      a: int = data[0]
      del data[0]
      data.append(a)
      c += 1
   print(data)


sdvig(data)
