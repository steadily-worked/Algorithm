# 목표: 1번 도시에서 출발해서 K번 도시를 방문하고 X번 회사로 가는 것
import sys
f = sys.stdin.readline

INF = int(1e9)
n, m = map(int, f().split())

adjList = [[INF]*(n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            adjList[a][b] = 0

for _ in range(m):
    # A에서 B로 가는 비용은 C라고 설정
    a, b = map(int, f().split())
    adjList[a][b] = 1
    adjList[b][a] = 1
x, k = map(int, f().split())

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            adjList[a][b] = min(adjList[a][b], adjList[a][k] + adjList[k][b])

result = adjList[1][k] + adjList[k][x]
if result == INF:
    print(-1)
else:
    print(result)
# for a in range(1, n+1):
#     for b in range(1, n+1):
#         if adjList[a][b] == INF:
#             print(-1)
#             break
#         else:
#             print(adjList[a][b], end=' ')
