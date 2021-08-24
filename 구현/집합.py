# https://www.acmicpc.net/problem/11723
import sys

f = sys.stdin.readline
S = set()


def add(param):
    if param not in S:
        S.add(param)


def remove(param):
    if param in S:
        S.remove(param)


def check(param):
    if param in S:
        return 1
    else:
        return 0


def toggle(param):
    if param in S:
        remove(param)
    else:
        add(param)


n = int(f())
for i in range(n):
    a = f().strip().split()
    if len(a) == 1:
        if a[0] == 'all':
            S = set([i for i in range(1, 21)])
        else:
            S = set()
    else:
        x, y = a[0], a[1]
        if x == 'add':
            add(int(y))
        elif x == 'check':
            print(check(int(y)))
        elif x == 'remove':
            remove(int(y))
        elif x == 'toggle':
            toggle(int(y))
