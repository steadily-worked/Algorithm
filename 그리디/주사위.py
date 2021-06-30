# https://www.acmicpc.net/problem/1041

import sys
f = sys.stdin.readline

n = int(f())
dice = list(map(int, f().split()))
new_dice = []
new_dice.append(min(dice[0], dice[5]))
new_dice.append(min(dice[1], dice[4]))
new_dice.append(min(dice[2], dice[3]))
new_dice.sort()

result = 0
if n == 1:
    result += sum(dice) - max(dice)
else:
    for i in range(2):
        if i == 0:
            result += (new_dice[0] * (n ** 2) + new_dice[1] * 4 * (n-1) + new_dice[2] * 4)
        else:
            result += (new_dice[0] * 4 * (n-1) + new_dice[1] * 4) * (n-1)

print(result)
