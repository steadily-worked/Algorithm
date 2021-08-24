# https://www.acmicpc.net/problem/9251
import sys
f = sys.stdin.readline

a = f().rstrip()
b = f().rstrip()

candidate = [[0]*(len(b)+1) for _ in range((len(a)))]
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            candidate[i][j] = candidate[i-1][j-1]+1
        elif a[i] != b[j]:
            candidate[i][j] = max(candidate[i][j-1], candidate[i-1][j])

print(max(candidate[-1]))
