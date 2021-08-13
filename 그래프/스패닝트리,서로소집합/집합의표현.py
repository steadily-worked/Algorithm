# https://www.acmicpc.net/problem/1717
import sys
f = sys.stdin.readline
sys.setrecursionlimit(10**5)

n, m = map(int, f().split())
parent = [0] * (n+1)


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        # 더 작은 게 부모가 되어야 함
        parent[b] = a
    else:
        parent[a] = b


for i in range(1, n+1):
    parent[i] = i
    # 일단 본인의 부모 테이블의 값을 본인으로 설정

for i in range(m):
    x, y, z = map(int, f().split())
    if x == 0:
        union_parent(parent, y, z)
    else:
        if find_parent(parent, y) == find_parent(parent, z):
            print("YES")
        else:
            print("NO")
