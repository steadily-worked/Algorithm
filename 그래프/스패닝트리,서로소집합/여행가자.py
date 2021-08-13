# https://www.acmicpc.net/problem/1976
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
    elif a > b:
        parent[a] = b
    else:
        return


n = int(f())
m = int(f())
parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i

for i in range(1, n+1):
    graph = list(map(int, f().split()))
    for j in range(1, len(graph)+1):
        if graph[j-1] == 1:
            union_parent(parent, i, j)

candidate_list = list(map(int, f().split()))
result = []
for i in candidate_list:
    result.append(find_parent(parent, i))

if len(set(result)) == 1:
    print("YES")
else:
    print("NO")
