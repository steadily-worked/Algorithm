# https://www.acmicpc.net/problem/15655
n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
s = []
result = []

def dfs():
    if len(s) == m and sorted(s) not in result:
        result.append(sorted(s))
        print(' '.join(map(str, sorted(s))))
        return

    for i in sorted(a):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()

dfs()
