# https://www.acmicpc.net/problem/1850
from math import gcd

a, b = map(int, input().split())
result = [a, b]
print('1' * gcd(*result))
