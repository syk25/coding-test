from collections import deque
from sys import stdin


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, v, visited):
    q = deque([v])
    visited[v] = True
    while q:
        v = q.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


def sol():
    n, m, v = map(int, input().split())
    graph = [[] for _ in range(1001)]
    for i in range(m):
        src, dst = map(int, input().split())
        graph[src].append(dst)
        graph[dst].append(src)

    for node in graph:
        node.sort()

    visited_dfs = [False for _ in range(1001)]
    visited_bfs = [False for _ in range(1001)]

    dfs(graph, v, visited_dfs)
    print()
    bfs(graph, v, visited_bfs)


sol()
