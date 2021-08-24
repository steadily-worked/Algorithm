# https://www.acmicpc.net/problem/1958
import sys
f = sys.stdin.readline

a = f().rstrip()
b = f().rstrip()
c = f().rstrip()


def LCS(a, b, c):
    candidate = [[[0 for _ in range(len(a)+1)]
                  for _ in range((len(b)+1))] for _ in range((len(c)+1))]
    for z in range(1, len(c)+1):
        for y in range(1, len(b)+1):
            for x in range(1, len(a)+1):
                if a[x-1] == b[y-1] == c[z-1]:
                    candidate[z][y][x] = candidate[z-1][y-1][x-1] + 1
                else:
                    candidate[z][y][x] = max(candidate[z-1][y][x], candidate[z][y-1][x], candidate[z]
                                             [y][x-1], candidate[z-1][y-1][x], candidate[z-1][y][x-1], candidate[z][y-1][x-1])

    return candidate[-1][-1][-1]


print((LCS(a, b, c)))
