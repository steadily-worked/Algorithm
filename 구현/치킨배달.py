# https://www.acmicpc.net/problem/15686
from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
chicken = [list(map(int, input().split())) for _ in range(n)]

home_index = []
chicken_index = []
for i in range(len(chicken)):
    for j in range(len(chicken[i])):
        if chicken[i][j] == 1:
            home_index.append((i+1, j+1))
        elif chicken[i][j] == 2:
            chicken_index.append((i+1, j+1))

result = int(1e9)
for i in combinations(chicken_index, m):
    next_result = [int(1e9) for _ in range(len(home_index))]
    for j in range(len(i)):
        for k in range(len(home_index)):
            next_result[k] = min(next_result[k], abs(
                home_index[k][0]-i[j][0]) + abs(home_index[k][1]-i[j][1]))
        result = min(result, sum(next_result))

print(result)
