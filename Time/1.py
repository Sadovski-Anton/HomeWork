a = 'cedewaraaossoqqyt'
b = 'codewars'


def scramble(s1, s2):
    n = sorted(list(s1))
    mm = list(s2)
    m = set(mm)
    for i in m:
        if mm.count(i) > n.count(i):
            print(4545)
            return False
    print(88)
    return True


scramble(a, b)
