# n개의 숫자가 순서대로 하나씩 주어졌을 때, 숫자가 하나씩 주어질 때마다 지금까지 주어진 숫자들 중 가장 작은 숫자 3개의 곱을 출력하는 프로그램을 작성해보세요.

import heapq

n = int(input())
arr = list(map(int, input().split()))
q = []

for i in arr:
    heapq.heappush(q, i)
    if len(q) < 3:
        print(-1)
    else:
        a = heapq.heappop(q)
        b = heapq.heappop(q)
        c = heapq.heappop(q)
        print(a*b*c)
        heapq.heappush(q, a)
        heapq.heappush(q, b)
        heapq.heappush(q, c)