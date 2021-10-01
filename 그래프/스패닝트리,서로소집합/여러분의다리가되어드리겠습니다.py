# https://www.acmicpc.net/problem/17352
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
parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i

for i in range(n-2):
    a, b = map(int, f().split())
    union_parent(parent, a, b)

result = []
for i in range(1, n+1):
    result.append(find_parent(parent, i))

for i in range(1, len(result)):
    if result[i-1] != result[i]:
        if result.count(result[i-1]) > result.count(result[i]):
            print(result[i-1], result[i])
            break
        else:
            print(result[i], result[i-1])
            break
