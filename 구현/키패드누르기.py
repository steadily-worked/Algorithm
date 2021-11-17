# https://programmers.co.kr/learn/courses/30/lessons/67256
def solution(numbers, hand):
    left, right = (4, 0), (4, 2)
    result = []
    for i in numbers:
        if i in [1, 4, 7]:
            result.append("L")
            if i == 1:
                left = (1, 0)
            elif i == 4:
                left = (2, 0)
            elif i == 7:
                left = (3, 0)
        elif i in [3, 6, 9]:
            result.append("R")
            if i == 3:
                right = (1, 2)
            elif i == 6:
                right = (2, 2)
            elif i == 9:
                right = (3, 2)
        else:
            if i == 2:
                center = (1, 1)
            elif i == 5:
                center = (2, 1)
            elif i == 8:
                center = (3, 1)
            elif i == 0:
                center = (4, 1)
            left_dist = ((left[0]-center[0])**2+(left[1]-center[1])**2)**0.5
            right_dist = ((right[0]-center[0])**2+(right[1]-center[1])**2)**0.5
            if left_dist == right_dist:
                if hand == 'right':
                    result.append('R')
                    right = center
                else:
                    result.append('L')
                    left = center
            elif left_dist > right_dist:
                result.append('R')
                right = center
            else:
                result.append('L')
                left = center

    return ''.join(result)
