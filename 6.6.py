data: list = [1, 4, 7, 2, 90, 356, 76, 0, 8]
data: list = list(filter((lambda x: not x % 2), data)) + list(filter((lambda x: x % 2), data))
print(data)
