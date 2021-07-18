# https://www.acmicpc.net/problem/18870
import sys
f = sys.stdin.readline

n = f()
a = list(map(int, f().split()))
a2 = list(sorted(set(a)))

dic = {a2[i]:i for i in range(len(a2))}
print(dic)
