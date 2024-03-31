import sys

N = int(sys.stdin.readline().strip())

cases = []

for i in range(N):
    a,b = map(int, sys.stdin.readline().strip().split())
    cases.append(a + b)

for i in cases:
    print(i)