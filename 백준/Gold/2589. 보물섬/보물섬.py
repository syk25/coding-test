from collections import deque
from sys import stdin

input = stdin.readline

row, column = map(int, input().split())

treasure_map = [[0 if x == "W" else 1 for x in input().strip()] for x in range(row)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count = 0


def bfs(treasure_map, x, y):
    queue = deque()
    queue.append((x, y, 0))
    visited = [[-1] * column for _ in range(row)]
    visited[x][y] = 1
    count = 0
    

    while queue:
        x, y, count = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < row and 0 <= ny < column and visited[nx][ny] == -1:
                if treasure_map[nx][ny] == 1:
                    queue.append((nx, ny, count + 1))
                    visited[nx][ny] = 1
    return count


result = 0
for x in range(row):
    for y in range(column):
        if treasure_map[x][y] == 1:
            result = max(result, bfs(treasure_map, x, y))

print(result)
