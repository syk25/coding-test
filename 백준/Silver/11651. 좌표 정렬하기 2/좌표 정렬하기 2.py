import sys

input = sys.stdin.readline

t = int(input())
my_coords = [list(map(int, input().split())) for x in range(t)]

my_coords = sorted(sorted(my_coords, key=lambda x: x[0]), key=lambda x: x[1])

for coord in my_coords:
    print(coord[0], coord[1])
