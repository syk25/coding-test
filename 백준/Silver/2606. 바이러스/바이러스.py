import sys
sys.setrecursionlimit(10**7)

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [set() for _ in range(N+1)]

for i in range(M):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].add(b)
    graph[b].add(a)

visited = [False] * (N+1)

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph, 1, visited)

count = 0
for x in visited:
    if x == True:
        count+= 1

print(count - 1)