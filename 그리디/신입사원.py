# https://www.acmicpc.net/problem/1946

import heapq
import sys

t = int(sys.stdin.readline())

answer_list = []
def new_person():
    n = int(sys.stdin.readline())
    candidate = []
    for _ in range(n):
        first, second = list(map(int, sys.stdin.readline().split()))
        candidate.append([first, second])
    candidate.sort()
    standard = []
    now = candidate[0]
    heapq.heappush(standard, now)
    for i in range(1, len(candidate)):
        if candidate[i][1] < now[1]:
            heapq.heappush(standard, candidate[i])
            now = candidate[i]

    return len(standard)

for j in range(t):
    print(new_person())