# 시간 복잡도: 최악의 경우에도 O(ElogV)임. V는 노드의 개수, E는 간선의 개수
import heapq
import sys
f = sys.stdin.readline
INF = int(1e9)

# n: 노드의 개수, m: 간선의 개수
n, m = map(int, f().split())
start = int(f())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, f().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    # 시작 노드로 가기위한 최단경로는 0으로 설정하여, 큐에삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 가장 최단거리가 짧은 노드에대한 정보꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리가 된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
