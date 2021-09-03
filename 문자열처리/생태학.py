# https://www.acmicpc.net/problem/4358
import sys
from collections import defaultdict
f = sys.stdin.readline

count = 0
result = defaultdict(int)
while True:
    a = f().rstrip()
    if not a:
        break
    result[a] += 1
    count += 1

result = sorted(result.items())

for i in result:
    print("%s %.4f" % (i[0], i[1]*100/count))
