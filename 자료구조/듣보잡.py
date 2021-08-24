# https://www.acmicpc.net/problem/1764
import sys
f = sys.stdin.readline

n, m = map(int, f().split())

see = []
look = []
for i in range(n):
    see.append(f().rstrip())
for i in range(n+1, n+m+1):
    look.append(f().rstrip())

result = see + look
result.sort()
count = []
for i in range(1, len(result)):
    if result[i-1] == result[i]:
        count.append(result[i-1])

print(len(count))
for i in count:
    print(i)
