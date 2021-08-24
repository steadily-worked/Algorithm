# https://www.acmicpc.net/problem/11279
import heapq
import sys
f = sys.stdin.readline

n = int(f())
q = []
for i in range(n):
    x = int(f())
    if x == 0:
        if len(q) == 0:
            print(0)
        else:
            print(abs(heapq.heappop(q)))
    else:
        heapq.heappush(q, -x)
