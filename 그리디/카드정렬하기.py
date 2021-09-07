# https://www.acmicpc.net/problem/1339
import sys
import heapq
f = sys.stdin.readline

n = int(f())
a = sorted([int(f()) for _ in range(n)])

heapq.heapify(a)
result = 0
while len(a) != 1:
    x = heapq.heappop(a)
    y = heapq.heappop(a)
    heapq.heappush(a, (x+y))
    result += (x+y)
print(result)
