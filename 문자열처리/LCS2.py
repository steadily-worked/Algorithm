# https://www.acmicpc.net/problem/9252
import sys
f = sys.stdin.readline

a = f().rstrip()
b = f().rstrip()

candidate = [[""]*(len(b)+1) for _ in range((len(a)+1))]
result = []
for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if a[i-1] == b[j-1]:
            candidate[i][j] = candidate[i-1][j-1] + a[i-1]
        else:
            candidate[i][j] = candidate[i-1][j] if len(candidate[i-1][j]) > len(
                candidate[i][j-1]) else candidate[i][j-1]

print(len(candidate[-1][-1]))
print(candidate[-1][-1])
