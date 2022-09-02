select_posishion: str = 'email'
data: dict = {
    3: {'name': 'Fedor3', 'soname': 'Petrov3', 'telefon': 1234567893, 'email': ''},
    1: {'name': 'Fedor', 'soname': 'Petrov', 'telefon': 123456789, 'email': 'info@gmail.com'},
    2: {'name': 'Fedor2', 'soname': 'Petrov2', 'telefon': 1234567892},
    4: {'name': 'Fedor4', 'soname': 'Petrov4', 'telefon': 1234567894, '123123': 'info@gmail.com'}
}
def proverka(number: str) -> str:
    for i in data.keys():
        a = data.get(i)
        if number not in a or a[number] == '':
            print(a['name'])


proverka(select_posishion)
