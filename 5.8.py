def vernama()-> list:
    text: str = input('Введите текст, который нужно зашифровать:')
    key: str = input('Введите ключ, который должен быть одинаковой длинны с текстом шифрования:')
    if len(text) != len(key):
        print('Текст и ключ введены разной длинны!!')
        return vernama()
    binar_word: list = []

    def binar(word: list) -> list:
        binar_word: list = []
        for i in word:
            a = bin(ord(i))[2:]
            a = "0" * (8 - len(a)) + a
            binar_word.append(a)
        # return binar_word

    binar(text)
    text_shifr = binar_word
    binar(key)
    key_shifr = binar_word


    print(text_shifr)
    print(key_shifr)


vernama()