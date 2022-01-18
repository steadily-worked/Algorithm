# https://www.acmicpc.net/problem/15664
n, m = list(map(int, input().split()))
a = sorted(list(map(int, input().split())))
visited = [False] * n
s = []
def dfs():
    if len(s) == m and s == sorted(s):
        print(*s)
        return

    temp = 0
    for i in range(len(a)):
        if not visited[i] and temp != a[i]:
            visited[i] = True
            s.append(a[i])
            temp = a[i]
            dfs()
            visited[i] = False
            s.pop()

dfs()
