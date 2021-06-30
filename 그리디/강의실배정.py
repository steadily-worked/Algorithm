# https://www.acmicpc.net/problem/11000

import heapq
import sys

n = int(sys.stdin.readline())
total_list = []
for i in range(n):
    start, end = map(int, sys.stdin.readline().split())
    total_list.append([start, end])

total_list.sort()
classroom = []
heapq.heappush(classroom, total_list[0][1])
for i in range(1, len(total_list)):
    if total_list[i][0] < classroom[0]:
        heapq.heappush(classroom, total_list[i][1])
    else:
        heapq.heappop(classroom)
        heapq.heappush(classroom, total_list[i][1])

print(len(classroom))
