a = int(input())
b = list(map(int, input().split()))
benefit = 0
b_max = b[-1]

if 2 <= a <= 100000:
    for i in range(a-2, -1, -1):
        if b[i] > b_max:
            b_max = b[i]
        else:
            benefit += b_max - b[i]

print(benefit)
