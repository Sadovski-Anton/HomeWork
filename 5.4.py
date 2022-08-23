text1: str = input('Введите первую строку:')
text2: str = input('Введите вторую строку:')

long: str = min(text1, text2, key=len)
rez: int = 0
for i in range(len(long)):
    if text1[i] == text2[i]:
        rez += 1
print(rez)

