import sys

n = int(sys.stdin.readline())


def dpstair(n):
    if 1 <= n <= 20:
        C = [0 for i in range(n+1)]
        if n == 1:
            C[0] = C[1] = 1
        elif n > 1:
            C[0] = C[1] = C[2] = 1
            C[3] = 2
        for i in range(4, n+1):
            C[i] = C[i-1] + C[i-3] + C[i-4]
        return C[n]


print(dpstair(n))
