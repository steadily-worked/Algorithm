# 다익스트라 최단 경로 알고리즘: 방문하지 않은 노드 중에서 가장 최단 거리가 짧은 노드를 선택하는 과정을 반복함
# 다익스트라 알고리즘이 진행되면서 한단계당 하나의 노드에 대한 최단 거리를 확실히 찾는 것임

# 처음에 각 노드에 대한 최단거리를 담는 1차원 리스트를 선언하고, 그이후에
# '단계마다 방문하지 않은 노드중에 최단거리가 가장짧은 노드를 선택' 하기위해 매단계마다 1차원 리스트의 모든 원소를 확인(순차탐색)

import sys
f = sys.stdin.readline
INF = int(1e9)

# 노드의 개수. 간선의 개수를 입력받기
n, m = map(int, f().split())
# 시작노드 번호를 입력받기
start = int(f())
# 각 노드에 연결되어있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for _ in range(n+1)]
# 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
visited = [False] * (n+1)
# 최단거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선정보 입력받기
for _ in range(m):
    a, b, c = map(int, f().split())
    # a번 노드에서 b번 노드로 가는 비용이 c
    graph[a].append((b, c))

# 방문하지 않은노드중에서 가장 최단거리가짧은 노드의 번호를 반환


def get_smallest_node():
    min_value = INF
    index = 0  # 가장 최단거리가 짧은 노드(인덱스)
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    distance[start] = 0  # 시작노드 초기화
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[i]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost


# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기위한 최단 거리를 출력
for i in range(1, n+1):
    # 도달할 수 없는경우 무한(INFINITY)이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])

# 시간복잡도: O(V^2) (V: 노드의 개수)
# 노드의 개수가 10000개를 넘어간다면 이 코드로 해결하기 어려움
