# https://www.acmicpc.net/problem/14241

import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

a.sort(reverse=True)
i = 0
total_score = 0
while len(a) != 1:
    total_score += a[i] * a[i+1]
    a[i] += a[i+1]
    del(a[i+1])

print(total_score)
