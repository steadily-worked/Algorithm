# https://www.acmicpc.net/problem/2671
import re

a = re.compile('(100+1+|01)+')
b = input()
if a.fullmatch(b):
    print("SUBMARINE")
else:
    print("NOISE")