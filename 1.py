def solution(s):
    a = list(s)
    new = []
    n = ''
    for i in a:
        if i.istitle():
            n = n + ''.join(new) + ' '
            new = []
            new.append(i)
        else:
            new.append(i)
    new = ''.join(new)
    n = n + new
    print(n)




solution("breakCamelCase")
