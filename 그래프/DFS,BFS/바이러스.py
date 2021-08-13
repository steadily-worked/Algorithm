# https://www.acmicpc.net/problem/2606
import sys
from collections import deque
f = sys.stdin.readline

c = int(f())
n = int(f())

adjList = [[] for _ in range(max(c, n)+1)]

for i in range(n):
    start, dest = map(int, f().split())
    adjList[start].append(dest)
    adjList[dest].append(start)
# 인접리스트 구현

visited = [False] * (c+1)

q_list = []
count = -1
def bfs(v):
    global count
    queue = deque([v])
    visited[v] = True
    while queue:
        q = queue.popleft()
        count += 1
        q_list.append(q)
        for a in adjList[q]:
            if not visited[a]:
                visited[a] = True
                queue.append(a)
    return count
print(bfs(1))
