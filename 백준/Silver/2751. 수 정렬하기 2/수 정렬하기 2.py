from sys import stdin
input = stdin.readline

n = int(input())
my_list = [int(input()) for x in range(n)]

my_list.sort()

for number in my_list:
    print(number)
