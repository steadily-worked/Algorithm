# https://www.acmicpc.net/problem/1922
import sys
f = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(f())
m = int(f())
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

edges = []
for i in range(m):
    a, b, c = map(int, f().split())
    edges.append((c, a, b))

edges.sort()

result = 0
for i in edges:
    c, a, b = i
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += c

print(result)
