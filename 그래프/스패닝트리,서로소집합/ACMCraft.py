# https://www.acmicpc.net/problem/1005
from collections import deque
import sys
import copy
f = sys.stdin.readline


def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    print(result[int(f())])


n = int(f())
for i in range(n):
    n, k = map(int, f().split())
    indegree = [0] * (n + 1)
    graph = [[] for i in range(n + 1)]
    time = [0] + list(map(int, f().split()))

    for _ in range(k):
        a, b = map(int, f().split())
        indegree[b] += 1
        graph[a].append(b)
    topology_sort()
