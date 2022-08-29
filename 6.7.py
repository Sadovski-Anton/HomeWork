data: list = [1, 5, 7, 9, 3, 5, 4, 6]

def sum_number(n: int):
    if n == len(data)-1:
        rez = data[n-1] + data[0]
    else:
        rez = data[n-1] + data[n+1]
    return rez

result: list = list(map(lambda x: sum_number(data.index(x)), data))
print(result)
