num: list = [1, 3, 6, 2, 90, -5, 0, 0, 90]
num_sort: list = []
num_sort.append(num[0])
for i in num[1:]:
    if i <= num_sort[0]:
        num_sort.insert(0, i)
    else:
        j = 0
        while j < len(num_sort) and i > num_sort[j]:
            j += 1
        num_sort.insert(j, i)
print(num_sort)

