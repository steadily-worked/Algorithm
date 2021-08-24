# https://www.acmicpc.net/problem/1620
import sys
f = sys.stdin.readline

n, m = map(int, f().split())
dict = {}

for i in range(1, n+1):
    a = f().rstrip()
    dict[a] = i
    dict[i] = a

for _ in range(m):
    a = f().rstrip()
    if a.isdigit():
        print(dict[int(a)])
    else:
        print(dict[a])
