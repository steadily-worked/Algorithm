import sys

n, m = map(int, sys.stdin.readline().split())

adj = [[] for _ in range(n)]

for _ in range(m):
    src, dest = map(int, sys.stdin.readline().split())
    adj[src].append(dest)
    adj[dest].append(src)

print(adj)
# 현재 adj는 이중 리스트 형태로 인접 리스트를 구현한 상태


def dfs(v, visited):
    people = 0
    stack = [v]
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = True
            people += 1
            for w in adj[v]:
                stack.append(w)
    return visited, people


visited = [False] * n
relationship = 0
result = []
for i in range(n):
    visited, people = dfs(i, visited)
    # print(visited, people)
    if people != 0:
        relationship += 1
        result.append(people)
print(relationship)
print(max(result), min(result))
