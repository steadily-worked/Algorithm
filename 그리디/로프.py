import sys

n = int(sys.stdin.readline())
a_list = []
for i in range(n):
    a_list.append(int(sys.stdin.readline()))

a_list.sort(reverse=True)

candidate = list()
for i in range(n):
    candidate.append(a_list[i] * (i+1))

print(max(candidate))
