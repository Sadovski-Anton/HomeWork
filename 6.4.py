data: list = [1, '2', [3, 4], '5g']


def onli_str(data: list) -> list:
    data: list = list(filter(lambda x: isinstance(x, str), data))
    print(data)

onli_str(data)
