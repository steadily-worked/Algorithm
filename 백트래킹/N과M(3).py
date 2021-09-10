# https://www.acmicpc.net/problem/15651
from itertools import product

n, m = map(int, input().split())
items = []
for i in range(1, n+1):
    items.append(i)

for i in product(items, repeat=m):
    print(*i, end='\n')
