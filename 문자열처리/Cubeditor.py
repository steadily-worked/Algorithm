# https://www.acmicpc.net/problem/1701
def makeLPS(x):
    leng = len(x)
    LPS_table = [0] * len(x)
    j = 0
    for i in range(1, leng):
        while j > 0 and x[i] != x[j]:
            j = LPS_table[j-1]
        if x[i] == x[j]:
            j += 1
            LPS_table[i] = j
    return max(LPS_table)


original_str = input()
result = 0

for i in range(len(original_str)):
    sub_str = original_str[i:len(original_str)]
    result = max(result, make_table(sub_str))

print(result)
