from collections import deque

m, n = map(int, input().split())
map_example = [[0 for _ in range(n)] for _ in range(m)]
distance = [[0 for _ in range(n)] for _ in range(m)]

for i in range(m):
    a = input()
    map_example[i] = list(map(int, list(str(a))))
queue = deque()

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(map, start_y, start_x):
    visited = [[False for _ in range(n)] for _ in range(m)]
    queue.append([start_x, start_y])
    distance[start_y][start_x] = 1
    while queue:
        x, y = queue.popleft()    # row와 col에 map_example[0][i]를 넣음
        for i in range(4):
            # 0일땐 서쪽, 1일땐 북쪽, 2일땐 동쪽, 3일땐 남쪽
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0 <= new_x < n and 0 <= new_y < m and not visited[new_y][new_x]:
                if map[new_y][new_x] == 1:
                    visited[new_y][new_x] = True  # 1
                    queue.append((new_x, new_y))
                    distance[new_y][new_x] = distance[y][x] + 1  # 2
                    if new_y == m-1:
                        a = distance[new_y][new_x]
                        queue.clear()
                        return a


new_list = []
for i in range(n):
    if map_example[0][i] == 1:
        new_list.append(bfs(map_example, 0, i))
res = list(filter(None, new_list))
if len(res) == 0:
    print(-1)
else:
    print(min(res))

# 6 10
# 0110000011
# 1101111101
# 1101010111
# 1111010111
# 0100111000
# 1011110111
