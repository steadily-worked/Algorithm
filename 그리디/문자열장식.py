# https://www.acmicpc.net/problem/1294
import copy
from functools import cmp_to_key

n = int(input())
arr = list(input() for _ in range(n))

def compare(x, y):
    if x+y > y+x:
        return 1
    if x+y < y+x:
        return -1
    return 0

arr.sort(key=cmp_to_key(compare))
sorted_arr = copy.deepcopy(arr)

temp = ''
while len(temp) != len(''.join(sorted_arr)):
    elem = arr[0]
    temp = temp + elem[0]
    arr.pop(0)
    if len(elem) > 1:
        arr.insert(0, elem[1:])
    arr.sort(key=cmp_to_key(compare))
    if len(arr) == 0:
        break
    else:
        elem = arr[0]
print(temp)
