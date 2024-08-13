from sys import stdin

n, m = map(int, input().split())
my_list = sorted([x for x in map(int, input().split())] + [x for x in map(int, input().split())])
print(*my_list)