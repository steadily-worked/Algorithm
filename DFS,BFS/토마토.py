# https://www.acmicpc.net/problem/7576
from collections import deque
import sys
f = sys.stdin.readline

m, n = map(int, f().split())
a = [[int(x) for x in f().split()] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    count = 0
    while queue:
        count += 1
        for _ in range(len(queue)):
            pop_x, pop_y = queue.popleft()
            for i in range(4):
                new_x = pop_y + dy[i]
                new_y = pop_x + dx[i]
                if 0 <= new_x < m and 0 <= new_y < n and a[new_y][new_x] == 0:
                    a[new_y][new_x] = 1
                    queue.append([new_y, new_x])

    for i in a:
        if i.count(0) != 0:
            return -1
    else:
        return count - 1

queue = deque()
for i in range(n):
    for j in range(m):
        if a[i][j] == 1:
            queue.append([i, j])

print(bfs(m, n))