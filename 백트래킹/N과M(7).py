# # https://www.acmicpc.net/problem/15656
n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
s = []
result = []
def dfs():
    if len(s) == m and sorted(s) not in result:
        print(' '.join(map(str, s)))
        return

    for i in sorted(a):
        s.append(i)
        dfs()
        s.pop()

dfs()
