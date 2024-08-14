from sys import stdin

input = stdin.readline

my_list = [x for x in map(int, input().split())]

sum = 0

for e in my_list:
    sum += e * e

print(sum % 10)
