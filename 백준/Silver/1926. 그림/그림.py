# 2024.05.31(금)
# 백준 1926: 그림 https://www.acmicpc.net/problem/1926
# 주제: bfs

from collections import deque
from sys import stdin

input = stdin.readline

# 입력받기
row, column = map(int, input().split())
graph = [[x for x in map(int, input().split())] for _ in range(row)]

# bfs 구현
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(graph, a, b):
    queue = deque()
    graph[a][b] = 0
    queue.append((a, b))
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= row or ny < 0 or ny >= column:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append(
                    (nx, ny)
                )  # bfs를 하되 내가 넣고 싶은 노드를 특정지을 수 있군
                count += 1
    return count


# 그림
paint = []
# 함수는 특정 지점에서 시작. 탐색은 전범위에서 할 수 있게끔 반복문 설정
for i in range(row):
    for j in range(column):
        if graph[i][j] == 1:
            paint.append(bfs(graph, i, j))


# 결과 출력
if len(paint) == 0:
    print(len(paint), 0, sep = "\n")
else:
    print(len(paint), max(paint), sep="\n")    
