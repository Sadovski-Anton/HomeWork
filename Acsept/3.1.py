sentence = input('Введите предложение с пробелами: ')
sentence_1 = sentence[:]
sentence_2 = sentence[:]
print(sentence_1.replace(' ', '-'))
sentence_2_new = '-'.join(sentence_2.split())
print(sentence_2_new)
