# https://www.acmicpc.net/problem/11724
import sys
f = sys.stdin.readline
sys.setrecursionlimit(10**4)

n, m = map(int, f().split())
adjList = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, f().split())
    adjList[a].append(b)
    adjList[b].append(a)

visited = [False] * (n+1)


def dfs(v):
    visited[v] = True
    for i in adjList[v]:
        if not visited[i]:
            dfs(i)


count = 0
for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)
