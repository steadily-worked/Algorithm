# https://www.acmicpc.net/problem/1697
import sys
from collections import deque

f = sys.stdin.readline
n, k = map(int, f().split())

visited = [0] * 100001
def bfs(v, visited):
    queue = deque([v])
    while queue:
        a = queue.popleft()
        if a == k:
            print(visited[a])
            break
        else:
            for next in (a-1, a+1, a*2):
                if 0 <= next <= 100000 and visited[next] == 0:
                    queue.append(next)
                    visited[next] = visited[a] + 1

bfs(n, visited)