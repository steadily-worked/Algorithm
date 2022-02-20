# https://www.acmicpc.net/problem/16496
from functools import cmp_to_key

n = int(input())
arr = list(map(int, input().split()))

def compare(x, y):
    if str(x)+str(y) > str(y)+str(x):
        return -1
    if str(x)+str(y) < str(y)+str(x):
        return 1
    return 0

arr.sort(key=cmp_to_key(compare))
count = 0
for elem in arr:
    if elem == 0:
        count += 1

if count == len(arr):
    print(0)
else:
    for elem in arr:
        print(elem, end='')
