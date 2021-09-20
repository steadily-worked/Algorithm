# https://www.acmicpc.net/problem/17129
import sys
from collections import deque
input = sys.stdin.readline

q = deque()
n, m = map(int, input().split())
island = [list(map(int, list(str(input().rstrip())))) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    flag = False
    q.append([x, y])
    visited[x][y] = 1
    while q:
        if flag:
            break
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and island[nx][ny] != 1:
                visited[nx][ny] = visited[x][y]+1
                q.append([nx, ny])
                if island[nx][ny] == 3 or island[nx][ny] == 4 or island[nx][ny] == 5:
                    flag = True
                    count_result = visited[nx][ny]-1
                    break
    if flag:
        print("TAK")
        print(count_result)
    else:
        print("NIE")


for i in range(n):
    for j in range(m):
        if island[i][j] == 2:
            bfs(i, j)
