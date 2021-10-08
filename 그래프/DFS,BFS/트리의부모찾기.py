# https://www.acmicpc.net/problem/11725
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
adjList = [[] for _ in range(n+1)]
parent = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    adjList[b].append(a)
    adjList[a].append(b)


def bfs(v):
    q = deque([v])
    while q:
        x = q.popleft()
        for i in adjList[x]:
            parent[i].append(x)
            q.append(i)
            adjList[i].remove(x)
    return parent


a = bfs(1)
for i in a:
    for j in i:
        if j != '':
            print(j)
