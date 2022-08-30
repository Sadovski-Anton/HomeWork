data: list = [1, 2, 3, 4, 5]


def reverse_data(data: list)-> list:
    a: int = 1
    c = data.pop(0)
    data.append(c)
    while a != len(data):
        c = data.pop(0)
        data.insert(-a, c)
        a += 1
    print(data)


reverse_data(data)
 
