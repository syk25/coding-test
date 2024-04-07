import sys

input = sys.stdin.readline

N = int(input())

classes = []

for i in range(N):
    start, end = map(int, input().split())
    classes.append((start,end))

classes.sort(key=lambda x:(x[1],x[0]))

k = 0

l = [classes[0]]

for i in range(1, N):
    if classes[k][1] <= classes[i][0]:
        l.append(classes[i])
        k = i

print(len(l))

