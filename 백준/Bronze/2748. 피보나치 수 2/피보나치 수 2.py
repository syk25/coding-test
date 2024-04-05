import sys
input = sys.stdin.readline

N = int(input())

fibos = [0] * 100
fibos[1] = fibos[2] = 1

for i in range(3, N + 1):
    fibos[i] = fibos[i-1] + fibos[i -2]

print(fibos[N])