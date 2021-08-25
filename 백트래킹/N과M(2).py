# https://www.acmicpc.net/problem/15650
from itertools import combinations

n, m = map(int, input().split())
items = []
for i in range(1, n+1):
    items.append(i)

for i in combinations(items, m):
    if len(i) == 1:
        print(i[0])
    else:
        print(*i, sep=' ')
