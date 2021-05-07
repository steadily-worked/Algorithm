# 필요한 것: a, t, e, x, n
# assembly line scheduling

n = int(input())
e1, e2, x1, x2 = 2, 4, 3, 2
f1, f2 = [0] * (n+1), [0] * (n+1)
a1 = list(map(int, input().split()))
a1.insert(0, 0)
a2 = list(map(int, input().split()))
a2.insert(0, 0)
t1 = list(map(int, input().split()))
t1.insert(0, 0)
t2 = list(map(int, input().split()))
t2.insert(0, 0)

f1[1] = e1 + a1[1]
f2[1] = e2 + a2[1]
fstar = 0
for i in range(2, n+1):
    f1[i] = min(f1[i-1] + a1[i], f2[i-1] + t2[i-1] + a1[i])
    f2[i] = min(f2[i-1] + a2[i], f1[i-1] + t1[i-1] + a2[i])
    if f1[i] + x1 > f2[i] + x2:
        fstar = f2[i] + x2
    else:
        fstar = f1[i] + x1
print(f1)
print(f2)
print(fstar)
