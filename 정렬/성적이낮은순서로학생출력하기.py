import sys
f = sys.stdin.readline

n = int(f())
total_list = []
for i in range(n):
    a, b = map(str, input().split())
    total_list.append([a, int(b)])

total_list.sort(key=lambda x: x[1])

for i in total_list:
    print(i[0], end=' ')
