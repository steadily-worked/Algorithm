# https://www.acmicpc.net/problem/9935
import sys
input = sys.stdin.readline

s = input().strip()
p = input().strip()

stack = []
for i in range(len(s)):
    stack.append(s[i])

    if len(stack) >= len(p):
        tmp = "".join(stack[-len(p):])
        if tmp == p:
            cnt = 0
            while cnt < len(p):
                stack.pop()
                cnt += 1
if len(stack) == 0:
    print("FRULA")
else:
    print("".join(stack))
