# https://www.acmicpc.net/problem/2252
from collections import deque
import sys
f = sys.stdin.readline

n, m = map(int, f().split())
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, f().split())
    indegree[b] += 1  # 더 큰 3에 대한 진입차수 1 증가하기
    graph[a].append(b)


def topology_sort():
    result = []
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=' ')


topology_sort()
