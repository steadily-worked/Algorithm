# https://www.acmicpc.net/problem/1916
import heapq
import sys
f = sys.stdin.readline
INF = int(1e9)

n = int(f())
m = int(f())
adjList = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for i in range(m):
    a, b, c = map(int, f().split())
    adjList[a].append((b, c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in adjList[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


start, dest = list(map(int, f().split()))
dijkstra(start)
print(distance[dest])
