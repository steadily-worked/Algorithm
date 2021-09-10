# https://www.acmicpc.net/problem/15652
from itertools import combinations_with_replacement

n, m = map(int, input().split())
items = []
for i in range(1, n+1):
    items.append(i)

for i in combinations_with_replacement(items, m):
    print(*i, sep=' ')
