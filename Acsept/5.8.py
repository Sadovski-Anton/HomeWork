def vernama()-> list:
    text: str = input('Введите текст, который нужно зашифровать:')
    key: str = input('Введите ключ, одинаковой длинны с текстом шифрования:')

    if len(text) != len(key):
        print('Текст и ключ введены разной длинны!!')
        return vernama()

    def binar(word: list):
        global bin_word
        bin_word = []
        for i in word:
            a = bin(ord(i))[2:]
            a = "0" * (8 - len(a)) + a
            bin_word.append(a)

    binar(text)
    text_list: list = bin_word.copy()

    binar(key)
    key_list: list = bin_word.copy()

    shifr: list = []
    for i in range(len(text_list)):
        rez: list = []
        for j in range(len(text_list[i])):
            if text_list[i][j] == '0' and key_list[i][j] == '0':
                rez.append('0')
            elif text_list[i][j] != '0' and key_list[i][j] != '0':
                rez.append('0')
            else:
                rez.append('1')
        shifr.insert(i, "".join(rez))
    print(shifr)


vernama()
