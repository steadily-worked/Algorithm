# https://www.acmicpc.net/problem/12852
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
visited = [False] * (n+1)

def bfs(v):
    q = deque([(v, [v])])
    while q:
        num, answer_arr = q.popleft()
        if num == 1:
            return len(answer_arr)-1, answer_arr
        if not visited[num]:
            visited[num] = True
            if num % 3 == 0:
                q.append((num//3, answer_arr+[num//3]))
            if num % 2 == 0:
                q.append((num//2, answer_arr+[num//2]))
            q.append((num-1, answer_arr+[num-1]))

ans = [bfs(n)]
print(ans[0][0])
print(*ans[0][1])