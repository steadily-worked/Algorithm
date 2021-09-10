# https://www.acmicpc.net/problem/15654
from itertools import permutations

n, m = map(int, input().split())
items = list(map(int, input().split()))
result_list = []

for i in permutations(items, m):
    result_list.append((i))

result_list = sorted(result_list)

for i in result_list:
    print(*i)
