data: list = [1, 4, 7, 2, 90, 356, 76, 0, 8]


def new_list(num: list) -> list:
    num: list = list(filter((lambda x: not x % 2), num)) + list(filter((lambda x: x % 2), num))
    print(num)


new_list(data)
