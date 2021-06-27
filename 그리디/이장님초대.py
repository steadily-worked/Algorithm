# https://www.acmicpc.net/problem/9237

n = int(input())
t = list(map(int, input().split()))

t.sort(reverse=True)
max_day = 0
for i in range(n):
    candidate = t[i] + i + 1
    if candidate > max_day:
        max_day = candidate

print(max_day + 1)
