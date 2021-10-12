# https://www.acmicpc.net/problem/1085
import sys
f = sys.stdin.readline

x, y, w, h = list(map(int, f().split()))

print(min(min(w-x, x), min(h-y,  y)))
