# https://www.acmicpc.net/problem/11403
import sys
f = sys.stdin.readline

n = int(f())
a_list = [list(map(int, f().split())) for _ in range(n)]

for k in range(n):
    for a in range(n):
        for b in range(n):
            if a_list[a][k] and a_list[k][b]:
                a_list[a][b] = 1

for i in range(n):
    for j in a_list[i]:
        print(j, end=' ')
    print()
