# https://www.acmicpc.net/problem/5568
from itertools import permutations
import sys

f = sys.stdin.readline

a = int(f())
pick = int(f())
card_list = [int(f()) for _ in range(a)]

result_list = []
for i in permutations(card_list, pick):
    if i not in result_list:
        result_list.append(''.join(i))

print(len(set(result_list)))
