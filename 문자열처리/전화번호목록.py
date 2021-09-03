# https://www.acmicpc.net/problem/5052
import sys
f = sys.stdin.readline

T = int(f())
for _ in range(T):
    answer = True
    n = int(f())
    candidate = [f().rstrip() for _ in range(n)]
    candidate.sort()
    min_num = candidate[0]
    for i in range(len(candidate)-1):
        leng = len(candidate[i])
        if candidate[i+1][:leng] == candidate[i]:
            answer = False

    if answer:
        print("YES")
    else:
        print("NO")
