import sys

input = sys.stdin.readline

K = int(input().strip())
stack = []
for i in range(K):
    v = int(input().strip())
    if v != 0:
        stack.append(v)
    else:
        stack.pop()

print(sum(stack))
