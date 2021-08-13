# https://www.acmicpc.net/problem/1260
from collections import deque
import sys
f = sys.stdin.readline

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in sorted(graph[v]):
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        q = queue.popleft()
        print(q, end=' ')
        for i in sorted(graph[q]):
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 인접 리스트
n, m, v = map(int, f().split())  # n: 정점의 개수, m: 간선의 개수, v: 시작점

visited_DFS = [False] * (n+1)
visited_BFS = [False] * (n+1)

adjList = [[] for _ in range(max(n, m)+1)]

for i in range(m):
    start, dest = map(int, f().split())
    adjList[start].append(dest)
    adjList[dest].append(start)

dfs(adjList, v, visited_DFS)
print()
bfs(adjList, v, visited_BFS)
