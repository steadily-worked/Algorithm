# https://www.acmicpc.net/problem/1647
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


n, m = map(int, f().split())
parent = [0] * (n+1)

edges = []
result = []

for i in range(1, n+1):
    parent[i] = i

for i in range(m):
    a, b, cost = map(int, f().split())
    edges.append((cost, a, b))

edges.sort()

for i in edges:
    cost, a, b = i
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result.append(cost)

print(sum(result) - max(result))
