from sys import stdin

input = stdin.readline

n = int(input())
my_list = [list(map(int, input().split())) for x in range(n)]

my_list.sort(key=lambda x: x[1])
my_list.sort(key=lambda x: x[0])

for coord in my_list:
    print(coord[0], coord[1])
