# https://www.acmicpc.net/problem/20365
import sys
input = sys.stdin.readline

a = int(input())
b = list(map(str, list(str(input().strip()))))
b_count = 0
r_count = 0
for i in range(len(b)):
    if i == 0:
        if b[i] == 'B':
            b_count += 1
        else:
            r_count += 1
    else:
        if b[i] != b[i-1]:
            if b[i-1] == 'B':
                r_count += 1
            else:
                b_count += 1

if r_count == b_count:
    print(r_count+1)
else:
    print(min(r_count, b_count) + 1)