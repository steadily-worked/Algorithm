# n개의 숫자가 주어졌을 때 가장 큰 숫자 2개를 뽑아 제거하고 두 숫자의 차이에 해당하는 숫자를 다시 집어넣는 것을 2개 이상의 숫자가 남아 있는 한 계속 반복하려고 합니다.
# 만약 뽑은 가장 큰 숫자 2개가 동일하다면, 이 경우에는 차이가 0이기 때문에 새롭게 집어넣지 않는다고 합니다.
# 이 과정을 진행한 이후 마지막으로 남게되는 숫자를 구하는 프로그램을 작성해보세요.

import heapq

n = int(input())
arr = sorted(list(map(int, input().split())), reverse=True)
q = []

for i in arr:
    heapq.heappush(q, -i)

while len(q) >= 2:
    a = heapq.heappop(q)
    b = heapq.heappop(q)
    if abs(a-b) != 0:
        heapq.heappush(q, -abs(a-b))

if len(q) == 1:
    print(-q[0])
else:
    print(-1)