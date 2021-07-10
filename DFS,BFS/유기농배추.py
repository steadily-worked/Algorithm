# https://www.acmicpc.net/problem/1012
import sys

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if 0 <= new_x < n and 0 <= new_y < m: # 범위 검사
            if matrix[new_x][new_y] == 1:
                matrix[new_x][new_y] = 2
                dfs(new_x, new_y)

t = int(input())
for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    matrix = [[0 for _ in range(m)] for _ in range(n)]
    # input 받고 행렬 생성

    for i in range(k):
        a, b = map(int, sys.stdin.readline().split())
        matrix[b][a] = 1

    count = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                dfs(i, j)
                count += 1

    print(count)
