data: list = [1, 5, 7, 9, 3, 5, 4, 6]


def sum_number(n: int)-> list:
    if n == len(data)-1:
        rez: int = data[n-1] + data[0]
    else:
        rez: int = data[n-1] + data[n+1]
    return rez


result: list = list(map(lambda x: sum_number(data.index(x)), data))
print(result)
