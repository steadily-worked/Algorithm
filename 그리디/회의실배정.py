# https://www.acmicpc.net/problem/1931

import sys

n = int(sys.stdin.readline())
total_list = []
for i in range(n):
    start, end = map(int, sys.stdin.readline().split())
    total_list.append([start, end])

total_list.sort(key=lambda x: (x[1], x[0]))
# 끝나는 시간이 빠른 순서대로
count = 1
now = total_list[0][1]
for i in range(1, len(total_list)):
    if total_list[i][0] >= now:
        count += 1
        now = total_list[i][1]
print(count)
