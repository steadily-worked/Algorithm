# https://www.acmicpc.net/problem/11047

import sys

n, k = list(map(int, sys.stdin.readline().split()))

coin_list = []
for _ in range(n):
    coin_list.append(int(sys.stdin.readline()))

coin_list.sort(reverse=True)

count = 0
for i in coin_list:
    count += k // i
    k %= i

print(count)
