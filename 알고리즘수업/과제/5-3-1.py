from collections import deque

queue = deque()
n, m = list(map(int, input().split()))

adj = [[] for _ in range(n)]
for _ in range(m):
    src, dest = map(int, input().split())
    adj[src].append(dest)
    adj[dest].append(src)

start_station, final_station = map(int, input().split())


def bfs(start, destination, visited):
    distance = [0] * n
    queue.append(start)
    visited[start] = True
    while queue:
        start = queue.popleft()
        for w in adj[start]:
            if destination in adj[start]:
                w = destination
            if not visited[w]:
                visited[w] = True
                queue.append(w)
                distance[w] = distance[start] + 1
                if w == destination:
                    queue.clear()
                    return distance[w]
    return -1


visited = [False] * n
print(bfs(start_station, final_station, visited))
