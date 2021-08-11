# https://www.acmicpc.net/problem/1753
import sys
import heapq
f = sys.stdin.readline
INF = int(1e9)

n, m = map(int, f().split())
start = int(f())
adjList = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for i in range(m):
    u, v, w = map(int, f().split())
    adjList[u].append((v, w))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in adjList[now]:
            min_num_first = adjList[now][0][0]
            min_num = adjList[now][0][1]
            if i[0] == min_num_first:
                if min_num > i[1]:
                    cost = dist + i[1]
                else:
                    cost = dist + min_num
            else:
                cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
