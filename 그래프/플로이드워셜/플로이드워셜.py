# 모든 지점에서 다른 모든 지점까지의 최단경로를 모두 구해야 하는 경우에 사용
# 단계마다 '거쳐가는노드' 를 기준으로 알고리즘을 수행하지만, 매번 방문하지 않는 노드들 중에서 최단거리를 찾는 노드를 찾을 필요가 없다는 점이 다름
# 현재 노드를 거쳐가는 모든 경로를 고려함. 따라서 O(N^3)
# 2차원 리스트에 '최단거리' 정보를 저장함, 점화식에 맞게 2차원 리스트를 갱신함 -> 다이나믹 프로그래밍

# 현재 확인하고있는 노드를 제외하고 N-1개의 노드 중에서 서로 다른 노드 (A, B) 쌍을 선택한다. 이후에 A -> 1번 -> B로 가는 비용을
# 확인한 뒤 최단 거리를 갱신한다.
import sys
f = sys.stdin.readline
INF = int(1e9)

# 노드의 개수 n, 간선의 개수 m
n = int(f())
m = int(f())
# 2차원 리스트(그래프 표현)를 만들고 모든 값을 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아 그 값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용은 C라고 설정
    a, b, c = map(int, f().split())
    graph[a][b] = c

# 점화식에 따라 플로이드워셜 알고리즘을 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        # 도달할 수 없는 경우 무한(INFINITY)이라고 출력
        if graph[a][b] == INF:
            print("INFINITY", end=' ')
        else:
            print(graph[a][b], end=' ')
    print()
