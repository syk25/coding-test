import sys

x,y,w,h = map(int,sys.stdin.readline().strip().split())

distances = [x, y, w-x, h-y]

d = sys.maxsize

for i in distances:
    if d > i:
        d = i

print(d)
