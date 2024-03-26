import sys

N = int(sys.stdin.readline())
towers = [int(i) for i in sys.stdin.readline().split()]
stack = []
result = [0] * N

for i in range(N):
    tower = towers[i]
    while stack and tower > towers[stack[-1]]:
        stack.pop()
    
    if stack:
        result[i] = stack[-1] + 1
    
    stack.append(i)

print(*result)