# https://www.acmicpc.net/problem/1325
import sys
from collections import deque
f = sys.stdin.readline

n, m = map(int, f().split())

adjList = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, f().split())
    adjList[b].append(a)


def bfs(v):
    count = 0
    q = deque([v])
    visited = [0] * (n+1)
    visited[v] = 1
    while q:
        a = q.popleft()
        count += 1
        for i in adjList[a]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1
    return count


result_list = []
max_num = 0

for i in range(1, n+1):
    if adjList[i]:
        temp = bfs(i)
        if temp >= max_num:
            if temp > max_num:
                result_list = []
            max_num = temp
            result_list.append(i)

print(*result_list)
