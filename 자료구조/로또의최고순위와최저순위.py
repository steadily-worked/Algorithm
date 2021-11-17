# https://programmers.co.kr/learn/courses/30/lessons/77484
def solution(lottos, win_nums):
    count = 0
    highest = 0
    lottos_copy = []
    for i in lottos:
        if i != 0:
            lottos_copy.append(i)
    zero = len(lottos) - len(lottos_copy)
    temp = []
    if sorted(lottos) == sorted(win_nums):
        answer = [1, 1]
    else:
        for i in win_nums:
            if i not in lottos_copy:
                temp.append(i)
            else:
                count += 1
        if zero > 0:
            for i in range(zero):
                lottos_copy.append(temp[i])
        for i in lottos_copy:
            if i in win_nums:
                highest += 1
        result1 = 6 if highest <= 1 else 7-highest
        result2 = 6 if count <= 1 else 7-count
        answer = [result1, result2]
    return answer