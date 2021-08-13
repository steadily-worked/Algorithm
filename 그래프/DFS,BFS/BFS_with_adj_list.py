from collections import deque

graph_list = {1: set([3, 4]),
              2: set([3, 4, 5]),
              3: set([1, 5]),
              4: set([1]),
              5: set([2, 6]),
              6: set([3, 5])}
root_node = 1


def BFS_with_adj_list(graph, root):
    visited = []
    queue = deque([root])

    while deque:
        n = queue.poplert()
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)

    return visited


print(BFS_with_adj_list(graph_list, root_node))

# 노드를 방문하면서, 인접한 노드 중 방문하지 않았던 노드의 정보만 큐에 넣어
# 먼저 큐에 들어있던 노드부터 방문하면 된다.
# 너비 우선은, 매 단계에서 가능한 모든 경우의 수를 확인하는 과정이라고 생각하면 편하다.
