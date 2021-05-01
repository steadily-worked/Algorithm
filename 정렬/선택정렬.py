a = list(map(int, input().split()))

for i in range(len(a)):
    idx = i
    for j in range(i+1, len(a)):
        if a[idx] > a[j]:
            idx = j
    a[i], a[idx] = a[idx], a[i]

print(a)
