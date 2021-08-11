# C에서 출발
# C에서 보낸 메시지를 받게되는 도시의 개수와 모두 메시지를 받는데까지 걸리는 시간 구하기
import heapq
import sys
f = sys.stdin.readline
INF = int(1e9)

# n: 도시의 개수, m: 통로의 개수, c: 시작점
n, m, c = map(int, f().split())
distance = [INF] * (n+1)
# x에서 y로 가는 시간 z
adjList = [[] for _ in range(n+1)]

for i in range(m):
    x, y, z = list(map(int, f().split()))
    adjList[x].append((y, z))
count = 0


def dijkstra(start):
    global count
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
                count += 1


dijkstra(c)
print(count, end=' ')
distance.remove(INF)
print(max(distance))
