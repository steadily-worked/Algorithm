a = int(input())
b = list(map(int, input().split()))

result = 0
temp = 0
maximum = 0
if 2 <= a <= 100000:
    for i in range(1, len(b)):
        temp = temp + 1 if b[i] > b[i-1] else 0
        maximum = max(maximum, temp)
print(maximum)
