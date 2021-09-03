# https://www.acmicpc.net/problem/16953
from collections import deque


def bfs(z):
    q = deque([(z, 1)])
    while q:
        x, count = q.popleft()
        if x == b:
            return count
        for i in (x*2, int(str(x)+"1")):
            if 0 <= i <= b:
                q.append((i, count+1))
    return -1


a, b = list(map(int, input().split()))
print(bfs(a))
