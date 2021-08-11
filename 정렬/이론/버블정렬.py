import sys

a = list(map(int, sys.stdin.readline().split()))

for i in range(len(a)-1, 0, -1):
    for j in range(i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

print(a)
