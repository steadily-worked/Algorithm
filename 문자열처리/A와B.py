# https://www.acmicpc.net/problem/12904
a = input()
b = input()


def BtoA(b):
    if b[-1] == 'A':
        new_b = b[:-1]
        return new_b
    elif b[-1] == 'B':
        if len(b) > 1:
            new_b = list(reversed(b[:-1]))
            return ''.join(new_b)
        else:
            return b


while True:
    b = BtoA(b)
    if a == b:
        print(1)
        break
    elif len(a) >= len(b):
        print(0)
        break
