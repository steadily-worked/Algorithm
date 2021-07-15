# https://www.acmicpc.net/problem/10026
from collections import deque

n = int(input())
visited = [[False] * n for _ in range(n)]
map_example = [list(map(str, input())) for _ in range(n)]
queue = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue.append([x, y])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and map_example[nx][ny] == map_example[x][y]:
                queue.append([nx, ny])
                visited[nx][ny] = True


count = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            count += 1
print(count, end=' ')

# 색약자 케이스
for i in range(n):
    for j in range(n):
        if map_example[i][j] == 'R':
            map_example[i][j] = 'G'
visited = [[False] * n for _ in range(n)]  # 다시 초기화해주고 진행해야됨

count = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            count += 1
print(count)
