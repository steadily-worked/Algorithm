# https://www.acmicpc.net/problem/5430
import sys
from collections import deque
f = sys.stdin.readline

t = int(f())

errorFlag = False
for i in range(t):
    p = f()
    n = int(f())
    candidate = f()[1:-2].split(',')
    if candidate[0] != '':
        q = deque(candidate)
    else:
        q = deque()

    flag = True
    for i in p:
        if i == 'R':
            if flag:
                flag = False
            elif not flag:
                flag = True
        elif i == 'D':
            if len(q) == 0:
                print("error")
                errorFlag = True
                break

            if flag:
                q.popleft()
            else:
                q.pop()

    if p.count('R') % 2 != 0:
        q.reverse()

    if not errorFlag:
        print('[', end='')
        for i in range(len(q)):
            print(q[i], end='')
            if i != len(q)-1:
                print(',', end='')
        print(']')
    errorFlag = False
