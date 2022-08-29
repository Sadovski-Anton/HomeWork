data: list = [1, 2, 3, 4, 5]
def reversedata(data):
    a: int = 1
    c = data.pop(0)
    data.append(c)
    while a != len(data):
        c = data.pop(0)
        data.insert(-a, c)
        a += 1
    print(data)


reversedata(data)
