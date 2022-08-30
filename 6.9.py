data: dict = {
    1: {'name': 'Fedor', 'soname': 'Petrov', 'telefon': 123456789, 'email': 'info@gmail.com'},
    2: {'name': 'Fedor2', 'soname': 'Petrov2', 'telefon': 1234567892},
    3: {'name': 'Fedor3', 'soname': 'Petrov3', 'telefon': 1234567893, 'email': ''},
    4: {'name': 'Fedor4', 'soname': 'Petrov4', 'telefon': 1234567894, '123123': 'info@gmail.com'}
}
select_posishion: str = 'email'


def proverka(number: str) -> str:
    for i in range(1, len(data)+1):
        a = data.get(i)
        if number not in a or a[number] == '':
            print(a['name'])


proverka(select_posishion)
