# https://www.acmicpc.net/problem/15657
from itertools import combinations_with_replacement

n, m = map(int, input().split())
items = list(map(int, input().split()))
items.sort()
result = []
for i in list(combinations_with_replacement(items, m)):
    for j in i:
        print(j, end=' ')
    print()
