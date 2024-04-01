import sys
sys.setrecursionlimit(10**7)

N,M = map(int, sys.stdin.readline().split())

graph = [set() for _ in range(N+ 1)]

for i in range(M):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].add(b)
    graph[b].add(a)

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i ,visited)

visited = [False] * (N+1)
count = 0

for i in range(1, N+1):
    if not visited[i]:
        dfs(graph, i, visited)
        count += 1

print(count)