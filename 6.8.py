data: dict = {
    'Belarus': ['Минск', 'Гомель'],
    'Italy': ['Милан', 'Турин']
}


def sity_name() -> str:
    name: str = input('Введите название города:')
    for i in data.keys():
        if name in data.get(i):
            print(i)


sity_name()
