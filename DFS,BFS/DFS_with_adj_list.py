graph_list = {1: set([3, 4]),
              2: set([3, 4, 5]),
              3: set([1, 5]),
              4: set([1]),
              5: set([2, 6]),
              6: set([3, 5])}
root_node = 1


def DFS_with_adj_list(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()  # 뽑아냄
        if n not in visited:  # 방문되지 않았으면
            visited.append(n)
            stack += graph[n] - set(visited)
    return visited


print(DFS_with_adj_list(graph_list, root_node))

# 먼저 방문한 노드에 연결된 노드보다 현재 방문한 노드에 연결된 노드를 방문한다.
