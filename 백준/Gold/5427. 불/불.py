import sys
from collections import deque
input = sys.stdin.readline
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def BFS(M, N, graph):
    start_R, start_C = 0, 0
    queue = deque()
    for i in range(N):
        for j in range(M):
            if graph[i][j] == '@':
                start_R, start_C = i, j
                queue.append((start_R, start_C, 0))
            elif graph[i][j] == '*':
                queue.appendleft((i, j, 0))
    while queue:
        row, col, time = queue.popleft()
        if (row == 0 or row == N-1 or col == 0 or col == M-1) and graph[row][col] == '@':
            return time+1
        if graph[row][col] == '*':
            for i in range(4):
                now_row, now_col = row+dr[i], col+dc[i]
                if now_row < 0 or now_row >= N or now_col < 0 or now_col >= M:
                    continue
                if graph[now_row][now_col] == '#':
                    continue
                if graph[now_row][now_col] == '.':
                    graph[now_row][now_col] = '*'
                    queue.append((now_row, now_col, time+1))
        else:
            for i in range(4):
                now_row, now_col = row+dr[i], col+dc[i]
                if now_row < 0 or now_row >= N or now_col < 0 or now_col >= M:
                    continue
                if graph[now_row][now_col] == '#' or graph[now_row][now_col] == '*':
                    continue
                if graph[now_row][now_col] == '.':
                    graph[now_row][now_col] = '@'
                    queue.append((now_row, now_col, time+1))
    return "IMPOSSIBLE"

T = int(input())
for _ in range(T):
    M, N = map(int, input().rstrip().split())
    graph = [list(input().rstrip()) for _ in range(N)]
    print(BFS(M, N, graph))