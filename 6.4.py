data: list = [1, '2', [3, 4], '5fdgdfgfdgdg']
data: list = list(filter(lambda x: isinstance(x, str), data))
print(data)