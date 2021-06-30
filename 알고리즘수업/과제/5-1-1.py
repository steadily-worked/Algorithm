import sys
sys.setrecursionlimit(10**6)


class Location:
    def __init__(self, row=0, col=0):
        self.row = row
        self.col = col


m, n = map(int, input().split())
map_example = [[0 for _ in range(n)] for _ in range(m)]
visited = [[False for _ in range(n)] for _ in range(m)]

for i in range(m):
    a = input()
    map_example[i] = list(map(int, list(str(a))))

dest = Location(m-1, None)

# map: 미로 정보를 저장하는 2차원 배열
# m, n: 미로의 열과 크기
# start, dest: 출발지와 목적지
# visited: 미로의 행과 열의 각 위치가 방문되었는지 아닌지를 확인하기 위한 2차원 배열
# 갈 수 있는 곳을 1로, 없는 곳을 0으로 만들어보자.


def findPath(map, m, n, start, dest, visited):
    next = Location()
    if map[start.row][start.col] == 1:  # 시작점이 1이라면
        # visited=True, 그러니까 방문을 했다고 표시하는 것
        visited[start.row][start.col] = True
    else:  # 그게 아니면 -1을 리턴하고 함수 종료
        return False
    # print("(",start.row,",",start.col,")") # 현재 위치 출력
    if start.row == dest.row:  # 현재 위치가 목적지와 같다면 1 리턴하고 함수 종료
        return True
    if start.col < n-1:  # 오른쪽으로 이동하는 경우
        if map[start.row][start.col+1] == 1 and not visited[start.row][start.col+1]:
            # 현재 지점에서 오른쪽으로 한 칸 옆의 값이 1이고 방문하지 않았다면,
            next.row = start.row  # row는 그대로
            next.col = start.col + 1  # col은 +1
            if findPath(map, m, n, next, dest, visited):  # findPath 함수를 실행할 수 있다면
                return True  # 1 리턴하고 함수 종료
    if start.row < m-1:  # 아래쪽
        if map[start.row+1][start.col] == 1 and not visited[start.row+1][start.col]:
            next.row = start.row + 1
            next.col = start.col
            if findPath(map, m, n, next, dest, visited):
                return True
    if start.col > 0:  # 왼쪽
        if map[start.row][start.col-1] == 1 and not visited[start.row][start.col-1]:
            next.row = start.row
            next.col = start.col - 1
            if findPath(map, m, n, next, dest, visited):
                return True
    if start.row > 0:  # 위쪽
        if map[start.row-1][start.col] == 1 and not visited[start.row-1][start.col]:
            next.row = start.row - 1
            next.col = start.col
            if findPath(map, m, n, next, dest, visited):
                return True
    return False  # 4가지 전부 이동할 수 없는 경우, False 리턴

# print(findPath(map_example, m, n, Location(1, 0), Location(5, 6), visited))


for i in range(n):
    result = findPath(map_example, m, n, Location(0, i), dest, visited)
    if result:
        break

if result:
    print(1)
else:
    print(-1)
