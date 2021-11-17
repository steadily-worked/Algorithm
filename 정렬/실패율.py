# https://programmers.co.kr/learn/courses/30/lessons/42889
def solution(N, stages):
    temp = []
    answer= []
    stages.sort()
    length = len(stages)
    for i in range(1, N+1):
        count = 0
        for j in stages:
            if i == j:
                count += 1
        if length > 0:
            temp.append((count/length, i))
            length -= count
        else:
            temp.append((count/5, i))
    temp = sorted(temp, key=lambda x:(-x[0],x[1]))
    for i in temp:
        answer.append(i[1])
    return answer