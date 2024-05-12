import sys
input = sys.stdin.readline

my_list = [i for i in range(1, 21)]

for _ in range(10):
        start, end = map(int, input().split())
        my_list[start-1:end] = my_list[start-1:end][::-1]

print(*my_list)