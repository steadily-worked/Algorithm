# https://www.acmicpc.net/problem/17219
import sys
f = sys.stdin.readline

a, b = map(int, f().split())
dicta = {}
for i in range(a):
    x, y = list(map(str, f().split()))
    dicta[x] = y

for i in range(b):
    print(dicta[f().rstrip()])
