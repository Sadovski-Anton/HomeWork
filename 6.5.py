data: list = [1, 2, 3, 4, 5]


def reverse_data(num: list)-> list:
    a: int = 1
    c = num.pop(0)
    num.append(c)
    while a != len(num):
        c = num.pop(0)
        num.insert(-a, c)
        a += 1
    print(num)


reverse_data(data)
